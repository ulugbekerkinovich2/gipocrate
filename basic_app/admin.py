from django.contrib import admin

# Register your models here.
from basic_app import models

admin.site.register(models.Болезни)
admin.site.register(models.Лекарства)
admin.site.register(models.Kasallik_nomi)
admin.site.register(models.Kasallik_haqida)
admin.site.register(models.Kasalikk_sabablari)
admin.site.register(models.Kasallik_asoratlari)
admin.site.register(models.Diagnostika)
admin.site.register(models.Davolanish)
admin.site.register(models.Болезни1)
admin.site.register(models.Лекарства1)


