from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import requests

# Create your views here.
CLIENT_ID = '1083501548325326949'
CLIENT_SECRET = '1J5Rg9nHZpGxTenHUfIhj1AOyyhmcag-'

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=1083501548325326949&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"

def discord_login(request: HttpRequest):
  return redirect(auth_url_discord)

def discord_login_redirect(request: HttpRequest):
  code = request.GET.get('code')
  print(code)
  user = exchange_code(code)
  print(f'{user=}')
  discord_user = authenticate(request, user=user)
  print(f'{discord_user=}')
  login(request, discord_user)
  return redirect("/")

def exchange_code(code: str):
  data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:8000/oauth2/login/redirect",
    "scope": "identify"
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
  credentials = response.json()
  access_token = credentials['access_token']
  response = requests.get("https://discord.com/api/v6/users/@me", headers={
    'Authorization': 'Bearer %s' % access_token
  })

  user = response.json()
  return user