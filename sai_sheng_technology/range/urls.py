from django.urls import path
from range import views

urlpatterns = [
    path('show/',views.show),
    path('add/',views.add),
]