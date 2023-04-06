from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser
from django.contrib.auth.models import User

class DiscordAuthenticationBackend(BaseBackend):
  def authenticate(self, request, user):
    find_user = DiscordUser.objects.filter(discord_id=user['id'])
    print('lyaps')
    if not find_user:
      print('User was not found. Saving...')
      new_user = User(username=user['username'])
      new_user.save()
      discord_tag = '%s#%s' % (user['username'], user['discriminator'])
      new_user = DiscordUser(
        user=new_user,
        discord_id=user['id'],
        avatar=user['avatar'],
        public_flags=user['public_flags'],
        flags=user['flags'],
        locale=user['locale'],
        mfa_enabled=user['mfa_enabled'],
        discord_tag=discord_tag
      )
      new_user.save()
      print(new_user)
      return new_user
    print('User was found. Returning...')
    return find_user[0]

  def get_user(self, user_id):
    try:
      return DiscordUser.objects.get(pk=user_id)
    except DiscordUser.DoesNotExist:
      return None