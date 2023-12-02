from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("assess/", views.assess, name="assess"),
    path("list/", views.list, name="list"),
    path("results/", views.results, name="list"),
    # path('my_view/', views.my_view, name='my-view'),
]