from django.db import models

class Planta(models.Model):
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    deInterior = models.CharField(max_length=40)
    
    def __str__(self):             #Con esa funcion puedo ver mas datos desde el admin
        texto = "({0}) ({1}) ({2})"
        return texto.format(self.nombre, self.nombreCientifico,self.deInterior)
    
class Arbol(models.Model):   
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    alturaMax = models.IntegerField()

    def __str__(self):             #Con esa funcion puedo ver mas datos desde el admin
        texto = "({0}) ({1}) ({2})"
        return texto.format(self.nombre, self.nombreCientifico,self.alturaMax)

class Cactus(models.Model):
    nombre = models.CharField(max_length=30)
    nombreCientifico = models.CharField(max_length=40)
    diasSinAgua = models.IntegerField()

    def __str__(self):             #Con esa funcion puedo ver mas datos desde el admin
        texto = "({0}) ({1}) ({2})"
        return texto.format(self.nombre, self.nombreCientifico,self.diasSinAgua)


class PlantaFormulario(models.Model):
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    deInterior = models.CharField(max_length=40)


class ArbolFormulario(models.Model):   
    nombre = models.CharField(max_length=40)
    nombreCientifico = models.CharField(max_length=40)
    alturaMax = models.IntegerField()

class CactusFormulario(models.Model):
    nombre = models.CharField(max_length=30)
    nombreCientifico = models.CharField(max_length=40)
    diasSinAgua = models.IntegerField()