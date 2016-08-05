from django.conf.urls import url, include
from blog import views as blog_views
from settings.base import MEDIA_ROOT

urlpatterns = [
    url(r'^$', blog_views.post_list, name='index'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    url(r'^(?P<id>\d)/$', blog_views.post_details, name='post_details'),
    url(r'^(?P<id>\d)/edit$', blog_views.edit_post, name='edit_post'),
    url(r'^post/new/$', blog_views.new_post, name='new_post'),
    url(r'', include('accounts.urls'))
]
