from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from .models import Resolution, Recipient, RecipientCollection


class ResolutionListView(generic.ListView):
    def get_queryset(self):
        return Resolution.objects.all().order_by("-date_submitted")


class ResolutionView(generic.DetailView):
    model = Resolution


def send_resolution(request, reso_id):
    return HttpRequest("works")


class RecipientListView(generic.ListView):
    def get_queryset(self):
        return Recipient.objects.all()#.order_by("-name")


class RecipientView(generic.DetailView):
    model = Recipient
