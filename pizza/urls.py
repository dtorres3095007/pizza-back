from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

apiv1 = "api/v1.0/"

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
