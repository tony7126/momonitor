from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
                       url('', include('momonitor.main.urls',namespace="main")),
                       url('auth', include('momonitor.auth.urls',namespace="auth")),
                       url('^mobile/', include('momonitor.mobile.urls',namespace="mobile")),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}),
                       )

urlpatterns += staticfiles_urlpatterns()
