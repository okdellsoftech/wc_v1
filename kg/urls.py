from django.urls import path
from . import views
from kg.views import IndexView



urlpatterns = [
    path('', IndexView.as_view()),
   
]