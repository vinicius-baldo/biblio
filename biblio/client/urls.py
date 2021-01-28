
from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/books', views.client_books.as_view(), name='client_books'),
]