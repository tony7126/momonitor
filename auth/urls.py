from django.conf.urls.defaults import *

urlpatterns = patterns('momonitor.auth.views',
                       url('^$','index',name="index"),
                       url('login', "login_view", name = 'login'),
                       url('logout', "logout_view", name = 'logout'),

)
