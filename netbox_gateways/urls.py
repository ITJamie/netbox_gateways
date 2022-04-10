from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views


urlpatterns = (
    # Gateway lists
    path("gateways-list/", views.GatewayListView.as_view(), name="gateway_list"),
    path("gateway/add/", views.GatewayEditView.as_view(), name="gateway_add"),
    path("gateway/<int:pk>/", views.GatewayView.as_view(), name="gateway"),
    path("gateway/<int:pk>/edit/", views.GatewayEditView.as_view(), name="gateway_edit"),
    path(
        "gateway/<int:pk>/delete/",
        views.GatewayDeleteView.as_view(),
        name="gateway_delete",
    ),
    path(
        "gateway/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="gateway_changelog",
        kwargs={"model": models.Gateway},
    ),
)
