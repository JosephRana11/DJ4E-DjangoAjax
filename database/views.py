from django.shortcuts import render 
from django.http import JsonResponse
from .models import Msg

def get_msg_view(request):
  obj = Msg.objects.all().values()
  return JsonResponse({'obj':list(obj)})