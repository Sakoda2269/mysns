from django.urls import path
from . import views


app_name = "sns"


urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("post/<int:pk>", views.DetailView.as_view(), name = "post"),
]