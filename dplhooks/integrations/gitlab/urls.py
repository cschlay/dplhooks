from django.urls import path

from dplhooks.integrations.gitlab import views

urlpatterns = [
    path('integrations/gitlab/webhooks', views.DeployWebhook.as_view())
]
