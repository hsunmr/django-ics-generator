from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.generate_ics_file, name='generate')
]