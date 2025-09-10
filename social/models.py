from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create A User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )
    date_modified = models.DateTimeField(_("Date Modified"), auto_now=True, auto_now_add=False)
    avatar = models.ImageField(upload_to='profile/user_avatar/')

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})

# Create Profile When New User Sign Up
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user= instance)
        user_profile.save()
        # Have The User Follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

