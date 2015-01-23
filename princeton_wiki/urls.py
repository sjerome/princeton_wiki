from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_protect


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'princeton_wiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'princeton_wiki.apps.princeton_wiki_app.views.index', name='index'),
    
    )
