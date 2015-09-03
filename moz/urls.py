from django.conf.urls import patterns, include, url
from django.contrib import admin
import web.urls as w_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web/', include(w_urls)),
)
