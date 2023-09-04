from django.contrib.auth.models import User
from .models import Msg
from django.forms import ModelForm
class MsgForm(ModelForm):
 class Meta:
  model = Msg
  fields = '__all__'