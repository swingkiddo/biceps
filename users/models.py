from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiscordUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  discord_id = models.BigIntegerField(primary_key=True)
  discord_tag = models.CharField(max_length=100)
  avatar = models.CharField(max_length=100)
  public_flags = models.IntegerField()
  flags = models.IntegerField()
  locale = models.CharField(max_length=100)
  mfa_enabled = models.BooleanField()
  last_login = models.DateTimeField(null=True)
  is_banned = models.BooleanField(default=False)

  def __str__(self):
    return self.user.username

#   def is_authenticated(self, request):
#     return True

#   def has_module_perms(self, request):
#     return True

#   def has_perm(self, request):
#     return True
