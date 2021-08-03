# To create the signals.py if not able to open, right click and choose override
# choose python format
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# When a user save, it sends a signal that is a post_save
# that a @receiver takes a signal
# and the receiver is the create_profile function takes any of those arguments below
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Import signals to apps.py to work
