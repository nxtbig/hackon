from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'newsletter.views.home', name='home'),
     url(r'^leaderboard/', 'newsletter.views.display_leaderboard'),
     # url(r'^blog/', include('blog.urls')),

    url(r'^level/(?P<level>\d+)$', 'newsletter.views.display_level', name='level_url'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('^markdown/', include( 'django_markdown.urls')),
]
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)