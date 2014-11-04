from django.conf.urls import patterns, url
from diaries.views import DiaryView, DiariesView

urlpatterns = patterns('',
        url(r'^$', DiariesView.as_view()),
        url(r'^diary/$',DiaryView.as_view()),
        url(r'^diary/(?P<diary_id>[0-9]*)/$',DiaryView.as_view())
        )
