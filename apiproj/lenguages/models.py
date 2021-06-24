from django.db import models


class Paradigm(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.RESTRICT)

    def __str__(self):  # para que muestre el nombre en el dashboard del admin al  mostrar todos los datos
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SaleDetail(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField
    sale = models.ManyToManyField(Sale)

    def __str__(self):
        return self.name
