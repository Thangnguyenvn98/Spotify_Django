from django.db import models
import string
import random
#Create a functio for random room code
def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase,k=length))
        #checking if the room has this code yet
        if Room.objects.filter(code=code).count()==0:   #The first code is refer to the code in the room model, equal to the code above
            break
    return code  


# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8,default="",unique=True)
    host = models.CharField(max_length=50,unique=True)
    guest_can_pause = models.BooleanField(null = False, default=False)  #Must pass a value which is null
    votes_to_skip = models.IntegerField(null =False,default=1)
    created_at = models.DateTimeField(auto_now_add=True) #Automatically adding time and date whenever room is created

    #Put most of login on your model
  

