#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from rest_framework import serializers
from .models import Forum, ForumCategory, ForumReply, ForumThread, ThreadSubscription, UserPostCount


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'


class ForumCategorySerializer(serializers.ModelSerializer):
    forums = ForumSerializer(serializers.SerializerMethodField(method_name='_get_forums', read_only=True),
                             many=True, read_only=True)

    class Meta:
        model = ForumCategory
        fields = ('id', 'title', 'forums')

    @staticmethod
    def _get_forums(obj):
        return obj.forums.order_by("title")


class ForumReplySerializer(serializers.ModelSerializer):
    subscribe = serializers.BooleanField(write_only=True)

    class Meta:
        model = ForumReply
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        thread = ForumThread.objects.filter(**self.context.get('kwargs', {})).first()
        subscribe = validated_data.pop('subscribe')

        validated_data['author'] = request.user
        validated_data['thread'] = thread

        reply = super(ForumReplySerializer, self).create(validated_data)

        thread.new_reply(reply)
        thread.subscribe(reply.author, "email")

        if subscribe:
            thread.subscribe(reply.author, "email")

        thread.subscribe(reply.author, "onsite")
        return reply


class ForumThreadSerializer(serializers.ModelSerializer):
    subscribe = serializers.BooleanField(write_only=True)
    posts = ForumReplySerializer(serializers.SerializerMethodField(method_name='_get_posts'), many=True, read_only=True)

    class Meta:
        model = ForumThread
        fields = '__all__'

    def _get_posts(self, obj):
        request = self.context.get('request')
        order_type = request.query_params.get("order_type", "asc")
        order_by = '-created' if order_type == "desc" else 'created'
        posts = obj.replies.order_by(order_by)
        obj.inc_views()
        return posts

    def create(self, validated_data):
        subscribe = validated_data.pop('subscribe')
        request = self.context.get('request')
        validated_data['author'] = request.user
        forum = Forum.objects.filter(**self.context.get('kwargs', {})).first()
        validated_data['forum'] = forum
        thread = super(ForumThreadSerializer, self).create(validated_data)
        forum.new_post(thread)

        if subscribe:
            thread.subscribe(thread.author, "email")

        thread.subscribe(thread.author, "onsite")
        return thread


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadSubscription
        fields = '__all__'
