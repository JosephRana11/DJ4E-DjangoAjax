from django.urls import path
from .views import get_msg_view , reset_global_view

urlpatterns = [
  path('get-msg/', get_msg_view , name = 'getmsg'),
  path('reset/' , reset_global_view , name='reset')
]