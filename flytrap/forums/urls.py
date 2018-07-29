#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from django.conf.urls import url

from .views import (
    forums,
    ForumView, CategoryView, ForumThreadView, ForumReplyView, ThreadSubscriptionView
)

urlpatterns = [
    url(r"^test$", forums, name="forums"),
    url(r'^$', ForumView.as_view({'get': 'list', 'post': 'create'})),
    url(r"^(?P<forum_id>\d+)/thread/$", ForumThreadView.as_view({'post': 'create', 'get': 'list'})),
    url(r"^(?P<pk>\d+)/$", ForumView.as_view({'get': 'retrieve', 'put': 'update'})),
    url(r'^categories/$', CategoryView.as_view({'post': 'create', 'get': 'list'})),
    url(r'^category/(?P<pk>\d+)/$', CategoryView.as_view({'get': 'retrieve', 'put': 'update'}), name='category'),
    url(r'^thread/(?P<pk>\d+)/$', ForumThreadView.as_view({'get': 'retrieve'})),
    url(r"^thread/(?P<pk>\d+)/subscribe/$", ForumThreadView.as_view({'post': 'subscribe'})),
    url(r"^thread/(?P<pk>\d+)/unsubscribe/$", ForumThreadView.as_view({'post': 'unsubscribe'})),
    url(r'^thread/(?P<thread_id>\d+)/reply/$', ForumReplyView.as_view({'get': 'retrieve', 'post': 'create'})),
    url(r"^thread_updates/$", ThreadSubscriptionView.as_view({'post': 'thread_updates'})),
    url(r'^subscriptions/$', ThreadSubscriptionView.as_view({'get': 'list'}), ),
]
