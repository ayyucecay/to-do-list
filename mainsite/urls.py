
from django.contrib import admin
from django.urls import path
from day.views import random_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('day/', random_view),
]
