from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),  # Include cart app URLs before the shop app URLs
    path('', include('shop.urls')),
]

# Serve static and media files during development when DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
