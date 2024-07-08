# Describe admin side that has CRUD access to the DB
from django.contrib import admin
from python_django_backend.models import Customer

admin.site.register(Customer)