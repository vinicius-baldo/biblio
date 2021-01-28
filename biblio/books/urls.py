
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:id>/books', views.reserve.as_view(), name='reserve'),
]