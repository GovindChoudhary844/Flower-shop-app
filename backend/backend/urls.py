# urls.py
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path("api/products/", include("base.urls.product_urls")),
    path("api/users/", include("base.urls.user_urls")),
    path("api/orders/", include("base.urls.order_urls")),
    path("api/events/", include("base.urls.event_urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
