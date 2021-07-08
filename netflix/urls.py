from django.urls import path
from .views import IndexView, PlayView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('post/<int:pk>/', PlayView.as_view(), name='play_view'),
]
