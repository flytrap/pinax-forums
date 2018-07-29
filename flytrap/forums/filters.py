#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
import django_filters
from .models import Forum, ForumCategory, ForumThread, ForumPost


class ForumFilter(django_filters.FilterSet):
    class Meta:
        model = Forum
        fields = {
            'title': ['exact']
        }


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ForumCategory
        fields = {
            'title': ['exact'],
            'parent_id': ['exact'],
            'parent__title': ['exact']
        }


class ForumThreadFilter(django_filters.FilterSet):
    order_type = django_filters.CharFilter(name='order_type')

    class Meta:
        model = ForumThread
        fields = {}


class PostFilter(django_filters.FilterSet):
    kind = django_filters.CharFilter(name='kind')

    class Meta:
        model = ForumPost
        fields = {}
