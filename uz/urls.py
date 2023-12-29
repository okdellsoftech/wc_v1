from django.urls import path
from . import views
from uz.views import IndexView



urlpatterns = [
    path('', IndexView.as_view()),
   
]