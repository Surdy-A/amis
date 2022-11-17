from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('member/', include('member.urls', namespace='member')),
    path('', home, name='home'),
    path('admin/', admin.site.urls)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)