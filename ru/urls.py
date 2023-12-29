from django.urls import path
from . import views
from ru.views import IndexView



urlpatterns = [
    path('', IndexView.as_view()),
]