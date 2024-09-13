from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>", views.get_month_by_number),
    path("<str:month>", views.get_month)
]