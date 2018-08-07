from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from employee_portal.models import Training_Programs_Model, Employee_Model, Departments, Employee_Trainings_Model


class Command(BaseCommand):
    """Allows command line integration for faker_factory.py"""

    def handle(self, *args, **options):
        """uses faker to generate fake data.  First arg = model, second arg = number of entries to create"""

        # the number argument is the total num of rows you want created

        seeder.add_entity(Training_Programs_Model, 12)
        seeder.add_entity(Departments, 12)
        seeder.add_entity(Employee_Model, 12)
        seeder.add_entity(Employee_Trainings_Model, 12)

        inserted_pks = seeder.execute()
