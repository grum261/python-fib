from django.urls import path
from .views import FibonacciSequenceCreateView, FibonacciTaskListView


urlpatterns = [
    path('', FibonacciSequenceCreateView.as_view()),
    path('task/<str:taskID>', FibonacciTaskListView.as_view())
]
