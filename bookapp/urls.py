from django.conf.urls import patterns, include, url
from bookapp.views import archive
urlpatterns = patterns('',
                       url(r'^$',archive),
# (r'book/create/$', create_book),
# (r'book/list/$', list_book ),
# (r'book/edit/(?P<id>[^/]+)/$', edit_book),
# (r'book/view/(?P<id>[^/]+)/$', view_book),
)