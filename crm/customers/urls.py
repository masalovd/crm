from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("help/", views.contacts, name="help"),
    path("records/", views.UserRecordListView.as_view(), name="user-record-list"),
    path("records/create/", views.RecordCreateView.as_view(), name="record-create"),
    path(
        "records/<int:pk>/update/",
        views.RecordUpdateView.as_view(),
        name="record-update",
    ),
    path(
        "records/<int:pk>/delete/",
        views.RecordDeleteView.as_view(),
        name="record-delete",
    ),
]
