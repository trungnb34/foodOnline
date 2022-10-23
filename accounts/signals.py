from .models import User, UserProfile
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_profile_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            userProfile = UserProfile.objects.get(user=instance)
            userProfile.save()
        except:
            UserProfile.objects.create(user=instance)
