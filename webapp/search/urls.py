from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results, name='results')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)