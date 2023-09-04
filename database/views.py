from django.shortcuts import render  , redirect , HttpResponse
from django.http import JsonResponse
from .models import Msg
from django.contrib.auth.models import User

def get_msg_view(request):
    msg_list = []
    obj = Msg.objects.all().order_by('-id')[:15]
    reversed_obj = obj[::-1]
    for msg in reversed_obj:
        person = User.objects.get(pk=msg.sender_id)
        msg_dict = {
            'text': msg.text,
            'sender': person.username,
            'time': msg.time
        }
        msg_list.append(msg_dict)

    return JsonResponse({'obj': msg_list})



def reset_global_view(request):
    if request.user.username == 'admin':
     obj = Msg.objects.all()
     obj.delete()
     return redirect('home')
    else:
        return HttpResponse('You do not have the authorized access to this page')
