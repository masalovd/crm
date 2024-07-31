from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import RecordModelForm
from .models import Record


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "customers/home.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "customers/about.html")


def contacts(request: HttpRequest) -> HttpResponse:
    return render(request, "customers/contacts.html")


def help(request: HttpRequest) -> HttpResponse:
    return render(request, "customers/help.html")


class UserRecordListView(LoginRequiredMixin, ListView):  # type: ignore
    model = Record
    template_name = "customers/user_record_list.html"
    context_object_name = "records"

    def get_queryset(self) -> QuerySet[Record]:
        return Record.objects.filter(user=self.request.user)


class RecordCreateView(LoginRequiredMixin, CreateView):  # type: ignore
    model = Record
    form_class = RecordModelForm
    template_name = "customers/record_create_form.html"

    def form_valid(self, form: RecordModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("user-record-list")


class RecordUpdateView(UserPassesTestMixin, UpdateView):  # type: ignore
    model = Record
    form_class = RecordModelForm
    template_name = "customers/record_update_form.html"

    def get_success_url(self) -> str:
        return reverse("user-record-list")

    def test_func(self) -> bool | None:
        record = self.get_object()

        if record.user == self.request.user:
            return True
        return False


class RecordDeleteView(UserPassesTestMixin, DeleteView):  # type: ignore
    model = Record
    success_url = "/records/"

    def test_func(self) -> bool | None:
        record = self.get_object()

        if record.user == self.request.user:
            return True
        return False
