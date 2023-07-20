from django.contrib import admin
from django.urls import path, include
from .views import hello_world

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', hello_world)
    path('', include('invoices.urls', namespace='invoices')),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Invoice admin system"
admin.site.index_title = "Management"