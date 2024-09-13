from django.urls import path

from . import views

urlpatterns = [
    path("<month>", views.get_month)
]