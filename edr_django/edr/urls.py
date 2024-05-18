from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("assess/", views.assess, name="assess"),
    path("assess/<int:valid_input>", views.assess, name="invalid_input"),
    path("faq/", views.faq, name="faq"),
    path("list/", views.list, name="list"),
    path("library/", views.dis_library, name="library"),
    path("assess/results/<str:filename>", views.results, name="results"),
]
