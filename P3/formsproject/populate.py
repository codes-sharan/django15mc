import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "formsproject.settings")
import django
django.setup()
from faker import *
from random import *
from firstapp.models import *
faker = Faker("ne_Np")


def populate(n):
    for i in range(n):
        feno = randint(1000,2000)
        fename = faker.name()
        fesal = randint(100000, 200000)
        feaddr = faker.city()
        emp_record = Employee.objects.create(ename=fename, eno=feno, esal=fesal, eaddr=feaddr)



populate(10)