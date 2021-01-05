from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from syms_marketplace import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clients.urls')),
    path('api/v1/client/', include('client_api.urls')),
]

if settings.DEBUG:
    # import debug_toolbar

    urlpatterns = [
        # path('__debug__/', include(debug_toolbar.urls)),
        # path('silk/', include('silk.urls', namespace='silk'))
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
