from django.urls import path
from .views import dashboard

app_name = "commulator"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]