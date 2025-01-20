from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:month>', views.all_months_by_num),
    path('<str:month>', views.all_months, name="monthly-task")
]