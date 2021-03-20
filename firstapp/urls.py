from django.urls import path
from . views import StudentLC, StudentRUD

urlpatterns = [
    path('students/', StudentLC.as_view()),
    path('students/<int:pk>/', StudentRUD.as_view())
]