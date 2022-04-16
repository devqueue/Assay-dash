from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.indexpage, name='home_lab1'),
    path('samples', views.sample, name='sample_lab1'),
    path('revenue', views.revenue, name='revenue_lab1'),
    path('util', views.util, name='utilization_lab1'),
    path('upload', views.upload_file, name="upload_lab1"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
