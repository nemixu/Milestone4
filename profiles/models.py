from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """A user profile to maintain user information and store order history"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    default_full_name = models.CharField(max_length=40, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        UserProfile.objects.create(user=instance)
    # If user is existing - save the profile change
    instance.userprofile.save()    
    
    
class Diary(models.Model):
    """A diary to maintain a users workout diary on their profile."""   
    task_name = models.CharField(max_length=100, null=False, blank=False)
    diary_text = models.TextField(null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return 'Diary #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'diaries'     