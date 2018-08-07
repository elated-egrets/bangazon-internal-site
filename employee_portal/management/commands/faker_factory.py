from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from employee_portal import models


class Command(BaseCommand):
    """Allows command line integration for faker_factory.py"""

    def handle(self, *args, **options):
        """uses faker to generate fake data.  First arg = model, second arg = number of entries to create"""

        # the number argument is the total num of rows you want created

        seeder.add_entity(models.training_programs, 12)
        seeder.add_entity(models.training_program_events, 12)
        seeder.add_entity(models.employees, 12)
        seeder.add_entity(models.departments, 12)
        seeder.add_entity(models.employee_trainings, 12)

        inserted_pks = seeder.execute()
