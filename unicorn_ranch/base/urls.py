from django.urls import path
from .views import UnicornList, UnicornUpdate

urlpatterns = [
    path("", UnicornList.as_view(), name="unicorns"),
    path("unicorn-update/<int:pk>", UnicornUpdate.as_view(), name="unicorn-update"),
]