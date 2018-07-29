from flytrap.base.view import BaseModeView

from .serializers import ForumCategorySerializer, ForumSerializer, ForumThreadSerializer, \
    ForumReplySerializer, SubscriptionSerializer
from .filters import ForumThreadFilter, CategoryFilter, PostFilter

from .models import (
    Forum,
    ForumCategory,
    ForumReply,
    ForumThread,
    ThreadSubscription,
    UserPostCount,
)


class CategoryView(BaseModeView):
    queryset = ForumCategory.objects.all()
    serializer_class = ForumCategorySerializer
    filter_class = CategoryFilter


class ForumView(BaseModeView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class ForumThreadView(BaseModeView):
    queryset = ForumThread.objects.select_related("forum")
    serializer_class = ForumThreadSerializer
    filter_class = ForumThreadFilter

    def get_queryset(self):
        qs = super(ForumThreadView, self).get_queryset()
        if self.kwargs:
            qs = qs.filter(**self.kwargs)
        return qs

    def subscribe(self, request):
        thread = self.get_object()
        thread.subscribe(request.user, "email")
        return self.resp_ok('subscribe Ok')

    def unsubscribe(self, request):
        thread = self.get_object()
        thread.unsubscribe(request.user, "email")
        return self.resp_ok('unSubscribe Ok')


class ForumReplyView(BaseModeView):
    lookup_field = 'thread_id'
    queryset = ForumReply.objects.all()
    serializer_class = ForumReplySerializer

    def get_queryset(self):
        qs = super(ForumReplyView, self).get_queryset()
        return qs.filter(**self.kwargs)


class PostView(BaseModeView):
    filter_class = PostFilter

    def get_serializer_class(self):
        if self.request.query_params.get('kind', 'reply'):
            return ForumReplySerializer
        return ForumThreadSerializer

    def get_queryset(self):
        if self.request.query_params.get('kind', 'reply'):
            return ForumReply.objects.all()
        return ForumThread.objects.all()


class ThreadSubscriptionView(BaseModeView):
    queryset = ThreadSubscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return ThreadSubscription.objects.filter(
            user=self.request.user, kind="onsite"
        ).select_related("thread")

    def thread_updates(self, request):
        self.get_queryset().filter(thread_id=request.POST["thread_id"]).delete()
        return self.resp_ok('update ok')


def forums():
    categories = ForumCategory.objects.filter(parent__isnull=True)
    categories = categories.order_by("title")

    most_active_forums = Forum.objects.order_by("-post_count")[:5]
    most_viewed_forums = Forum.objects.order_by("-view_count")[:5]
    most_active_members = UserPostCount.objects.order_by("-count")[:5]

    latest_posts = ForumReply.objects.order_by("-created")[:10]
    latest_threads = ForumThread.objects.order_by("-last_modified")
    most_active_threads = ForumThread.objects.order_by("-reply_count")
    most_viewed_threads = ForumThread.objects.order_by("-view_count")

    return {
        "categories": categories,
        "most_active_forums": most_active_forums,
        "most_viewed_forums": most_viewed_forums,
        "most_active_members": most_active_members,
        "latest_posts": latest_posts,
        "latest_threads": latest_threads,
        "most_active_threads": most_active_threads,
        "most_viewed_threads": most_viewed_threads,
    }
