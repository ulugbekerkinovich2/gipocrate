from django.db import models


# Create your models here.
class Болезни(models.Model):
    title = models.TextField(verbose_name='название')
    description = models.TextField(verbose_name="описание")
    description1 = models.TextField(verbose_name="Причин_возникновения")
    description2 = models.TextField(verbose_name="Cимптом")
    description3 = models.TextField(verbose_name="Диагностика")
    description4 = models.TextField(verbose_name="Лечение")
    # description5 = models.TextField(verbose_name="Препарат")

    def __str__(self):
        return self.title


class Лекарства(models.Model):
    name = models.TextField(verbose_name="описание")
    character = models.TextField(verbose_name="характеристика")
    instruction = models.TextField(verbose_name="инструкция")

    def __str__(self):
        return self.name
