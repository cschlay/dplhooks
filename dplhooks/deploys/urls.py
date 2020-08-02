from django.urls import path

from dplhooks.deploys import views

urlpatterns = [
    path('p/deploy', views.DeployView.as_view())
]
