from django.urls import path
from .views import registerUser, registerRest

urlpatterns = [
    path("registerUser/", view=registerUser, name="register_user"),
    path("registerRes", view=registerRest, name="register_res")
]