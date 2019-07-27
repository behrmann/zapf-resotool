from django.urls import path

from . import views

app_name = "resoapp"
urlpatterns = [
    path("", views.ResolutionListView.as_view(), name="index"),
    path("<int:pk>/", views.ResolutionView.as_view(), name="resolution"),
    path("sendreso/<int:reso_id>/", views.send_resolution, name="send_reso"),
    path("recipients/", views.RecipientListView.as_view(), name="recipients"),
]
