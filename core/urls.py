from django.conf.urls import patterns, url, include

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),
    url(r'^login/$', 'login', name='login'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^(?P<id>[a-zA-Z0-9]+)$', 'redirect', name='redirect'),
    url(r'^shorten/$', 'shorten', name='shorten'),
)