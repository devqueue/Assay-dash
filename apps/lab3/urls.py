from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.indexpage, name='home_lab3'),
    path('samples', views.sample, name='sample_lab3'),
    path('revenue', views.revenue, name='revenue_lab3'),
    path('util', views.util, name='utilization_lab3'),
    path('upload', views.upload_file, name="upload_lab3"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
