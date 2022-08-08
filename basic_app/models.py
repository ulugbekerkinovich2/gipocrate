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
class Болезни1(models.Model):
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

class Лекарства1(models.Model):
    name = models.TextField(verbose_name="описание")
    character = models.TextField(verbose_name="характеристика")
    instruction = models.TextField(verbose_name="инструкция")

    def __str__(self):
        return self.name


class Kasallik_nomi(models.Model):
    kasallik_nomi = models.TextField()

    def __str__(self):
        return self.kasallik_nomi


class Kasallik_haqida(models.Model):
    kasallik_haqida = models.TextField()

    def __str__(self):
        return self.kasallik_haqida


class Kasalikk_sabablari(models.Model):
    kasallik_sabablari = models.TextField()

    def __str__(self):
        return self.kasallik_sabablari


class Kasallik_asoratlari(models.Model):
    kasallik_asoratlari = models.TextField()

    def __str__(self):
        return self.kasallik_asoratlari


class Diagnostika(models.Model):
    diagnostika = models.TextField()

    def __str__(self):
        return self.diagnostika


class Davolanish(models.Model):
    davvolanish = models.TextField()

    def __str__(self):
        return self.davvolanish
