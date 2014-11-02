from django.conf.urls import url, patterns
from accounts.views import WriterView, SessionView

urlpatterns = patterns('',
        url(r'^writer/$',WriterView.as_view()),
        url(r'^session/$', SessionView.as_view()),
        url(r'^session/(?P<session_key>.*)/$',SessionView.as_view())
        )
