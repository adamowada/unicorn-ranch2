from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import Unicorn

# Create your views here.


class UnicornList(ListView):
    model = Unicorn
    context_object_name = "unicorns"


def unicorn_update(request, pk):
    print(request)
    if request.method == "POST":
        unicorn = get_object_or_404(Unicorn, id=pk)
        unicorn.location = request.POST['location']
        unicorn.save()
        # return render(request, 'base/unicorn_list.html')
        return JsonResponse({}, status=200)
