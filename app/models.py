from django.db import models
from users.models import DiscordUser


class Category(models.Model):
    name = models.TextField(max_length=20)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField(max_length=30, null=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=150)
    start_time = models.DateTimeField()
    picture = models.ImageField()
    participants = models.ManyToManyField(DiscordUser, through='Participant', through_fields=('tournament', 'discord_user'))

    def __str__(self):
        return self.name

class Participant(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    discord_user = models.ForeignKey(DiscordUser, on_delete=models.CASCADE)

class TournamentTeam(models.Model):
    pass

class Match(models.Model):
    index = models.SmallIntegerField()
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.tournament.name} Match {self.index}'
