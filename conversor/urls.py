from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name='conversor'
urlpatterns = [
    path('converter/', views.converter_video, name='converter_video'),
    path('sucesso/', views.sucesso, name='sucesso'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
