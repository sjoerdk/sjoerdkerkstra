from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  
    url(r'^$', 'sjoerdkerkstra_site.views.home', name='home'),
)
