from django.conf.urls import patterns, include, url


urlpatterns = patterns('quickstart.views',
    # Examples:
    url(r'^alumnos/$', 'alumno_list',name='vista_alumnos'),
    url(r'^alumnos/(?P<pk>.*)/$', 'alumno_proces',name='procesando_alumnos'),
)
