from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Organization,SubOrganization,Division,SubDivision,Employee])



