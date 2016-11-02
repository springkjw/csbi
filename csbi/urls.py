from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import home, profile
from member.views import member
from publication.views import publication, pub_detail
from notice.views import list, notice_detail
from research.views import research
from protocol.views import protocol_list

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'prof/profile/$', profile, name='profile'),
    url(r'members/$', member, name='member'),
    url(r'researches/$', research, name='research'),
    url(r'pub/(?P<type>[\w-]+)/$', publication, name='publication'),
    url(r'pub/detail/(?P<pub_id>\d+)/$', pub_detail, name='pub_detail'),
    url(r'notice/list/(?P<type>[\w-]+)/$', list, name='notice_list'),
    url(r'notice/detail/(?P<notice_id>\d+)/$', notice_detail, name='notice_detail'),
    url(r'protocol/list/$', protocol_list, name="protocol_list"),

    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
