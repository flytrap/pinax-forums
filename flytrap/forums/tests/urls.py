from django.conf.urls import include, url

urlpatterns = (
    url(r"^", include(("flytrap.forums.urls", "forums"), namespace="flytrap_forums")),
)
