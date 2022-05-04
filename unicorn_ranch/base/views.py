from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Unicorn


# Create your views here.


class UnicornList(ListView):
    model = Unicorn
    context_object_name = "unicorns"


# class UnicornUpdate(UpdateView):
#     model = Unicorn
#     fields = ['location'] # breakout to list
#     success_url = reverse_lazy("unicorns")


def unicorn_update(request):
    if request.method == "POST":
        name = "Adam"
        color = "Tan"
        location = "Seattle"

        unicorn = Unicorn.objects.create(name=name, color=color, location=location)
        unicorn.save()
        res = {"error": False, "msg": "Successfully Submited."}
        return JsonResponse(res)
