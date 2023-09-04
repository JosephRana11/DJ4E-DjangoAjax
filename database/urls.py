from django.urls import path
from .views import get_msg_view

urlpatterns = [
  path('get-msg/', get_msg_view , name = 'getmsg'),
]