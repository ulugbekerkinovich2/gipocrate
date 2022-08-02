from django.contrib import admin

# Register your models here.
from basic_app import models

admin.site.register(models.Болезни)
admin.site.register(models.Лекарства)

