from django.urls import path
from .views import UnicornList
from . import views

urlpatterns = [
    path("", UnicornList.as_view(), name="unicorns"),
    # path("unicorn-update/<int:pk>", UnicornUpdate.as_view(), name="unicorn-update"),
    path("unicorn-update/<int:pk>", views.unicorn_update, name="unicorn-update"),
]
