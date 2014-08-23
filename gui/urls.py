from django.conf.urls import patterns, include, url


urlpatterns = patterns('gui.views',
    # Examples:
    url(r'^home/$', 'view_home', name='vista_home'),
    url(r'^form/(?P<id>.*)/$', 'view_form', name='vista_form'),
)
