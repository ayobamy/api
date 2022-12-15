from django.urls import path
from .views import dashboard, profile_list, profile, team, signup, base

app_name = "commulator"

urlpatterns = [
    path("", base, name="base"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("team/", team, name="team"),
    path("signup/", signup, name="signup"),
]
