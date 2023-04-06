from django.contrib import admin
from .models import Category, Product, Tournament, Match, Participant, TournamentTeam

# Register your models here.
_models = (Category, Product, Tournament, Match, Participant, TournamentTeam)
admin.site.register(_models)