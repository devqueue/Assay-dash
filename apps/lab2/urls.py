from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.indexpage, name='home_lab2'),
    path('samples', views.sample, name='sample_lab2'),
    path('revenue', views.revenue, name='revenue_lab2'),
    path('util', views.util, name='utilization_lab2'),
    path('upload', views.upload_file, name="upload_lab2"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
