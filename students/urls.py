from django.urls import path
from . import views   # ✅ ADD THIS

urlpatterns = [
    path('', views.students),
]
