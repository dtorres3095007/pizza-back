from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

apiv1 = "api/v1.0/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(apiv1, include("apps.pizzas.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
