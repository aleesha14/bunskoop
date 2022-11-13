from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("my_runs", views.my_runs, name="my_runs"), 
    path("add_run", views.add_run, name="add_run"),
    path("records", views.records, name="records"),
    path("training", views.training, name="training"),
    path("completed_training", views.completed_training, name="completed_training"),
    path("air", views.air, name="air"),
    path("air_js", views.air_js, name="air_js")
 ]