from django.urls import path

from . import views

urlpatterns = [
    path('<int:month>', views.all_months_by_num),
    path('<str:month>', views.all_months)
]