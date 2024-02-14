from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('add-expense', views.add_expense, name='harcama_ekle'),
]
