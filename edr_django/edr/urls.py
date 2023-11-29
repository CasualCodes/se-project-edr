from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("assess/", views.assess, name="assess")
]