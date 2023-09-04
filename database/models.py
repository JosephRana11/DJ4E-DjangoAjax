from django.db import models
from django.contrib.auth.models import User

class Msg(models.Model):
  sender = models.ForeignKey(User , on_delete=models.CASCADE)
  text = models.TextField()
  time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.text}--{self.sender}"