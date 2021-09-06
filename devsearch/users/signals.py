# Signals can be called directly by implementing sender/receiver in models.py 
# as we have a separate file now, we need to connect signals.py inside apps.py

# import build in django user model 
from django.contrib.auth.models import User
from .models import Profile

# Signal for user create 
# Create signal and receiver once the user is created and saved 
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# receiver for user save method 
# sender : model that sends the signal
# instance : instance/object of the model that triggers it 
# created : true/false value - if the user/model is added to the database or it was simple saved again. i.e. a new entry or not. 

# using decorators 
@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print ('profile saved')
    print('Sender : ', sender)
    print('instance : ', instance)
    print('created : ', created)

# delete user if the profile is deleted
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# we can also use decorators instead of below method
# connect the receiver 
#post_save.connect(profileUpdated, sender=Profile)
#post_delete.connect(deleteUser, sender=Profile)

# receiver to automatically create a profile on user creation 
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
