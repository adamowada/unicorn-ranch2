from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.forms import ModelForm
from django.contrib import messages
from .models import Unicorn
from .forms import InputForm

# Create your views here.


class UnicornList(ListView):
    model = Unicorn
    context_object_name = "unicorns"


# class UnicornUpdate(UpdateView):
#     model = Unicorn
#     fields = ['location'] # breakout to list
#     success_url = reverse_lazy("unicorns")


def unicorn_update(request, pk):
    print(request)
    if request.method == "POST":
        unicorn = get_object_or_404(Unicorn, id=pk)
        unicorn.location = request.POST['location']
        unicorn.save()
        return render(request, 'base/unicorn_list.html')
