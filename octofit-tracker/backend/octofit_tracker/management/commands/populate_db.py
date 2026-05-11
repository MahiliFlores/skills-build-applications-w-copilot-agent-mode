from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Crear equipos
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234', first_name='Tony', last_name='Stark', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='1234', first_name='Peter', last_name='Parker', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='1234', first_name='Bruce', last_name='Wayne', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='1234', first_name='Diana', last_name='Prince', team=dc),
        ]

        # Crear actividades
        activities = [
            app_models.Activity.objects.create(user=users[0], type='Running', duration=30, calories=300),
            app_models.Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400),
            app_models.Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=500),
            app_models.Activity.objects.create(user=users[3], type='Yoga', duration=50, calories=200),
        ]

        # Crear workouts
        workouts = [
            app_models.Workout.objects.create(name='Full Body', description='Entrenamiento completo', difficulty='Medium'),
            app_models.Workout.objects.create(name='Cardio Blast', description='Cardio intenso', difficulty='Hard'),
        ]

        # Crear leaderboard
        app_models.Leaderboard.objects.create(user=users[0], points=1000)
        app_models.Leaderboard.objects.create(user=users[1], points=800)
        app_models.Leaderboard.objects.create(user=users[2], points=1200)
        app_models.Leaderboard.objects.create(user=users[3], points=950)

        self.stdout.write(self.style.SUCCESS('Base de datos poblada con datos de prueba.'))
