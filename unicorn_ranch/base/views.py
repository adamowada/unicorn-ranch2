from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Unicorn


# Create your views here.


class UnicornList(ListView):
    model = Unicorn
    context_object_name = "unicorns"


class UnicornUpdate(UpdateView):
    model = Unicorn
    fields = ['location'] # breakout to list
    success_url = reverse_lazy("unicorns")


