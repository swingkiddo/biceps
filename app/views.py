from django.shortcuts import render, redirect
from django.http import HttpRequest
from users.models import DiscordUser

# Create your views here.
def home(request: HttpRequest):
    user = request.user
    if hasattr(user, 'is_anonymous') and user.is_anonymous:
        return redirect('oauth2/login')
    
    user = DiscordUser.objects.get(user=user.id)
    avatar_url = f'https://cdn.discordapp.com/avatars/{user.discord_id}/{user.avatar}'
    context = {'avatar_url': avatar_url}
    return render(request, 'app/index.html', context)