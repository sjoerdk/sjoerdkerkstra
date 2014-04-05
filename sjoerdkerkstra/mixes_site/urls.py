from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       
    url(r'^$', 'mixes_site.views.mainpage', name='mainpage'),
)
