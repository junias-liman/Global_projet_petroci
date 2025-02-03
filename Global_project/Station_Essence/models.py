from django.db import models

# Super.
class Essence(models.Model):  
      veille=models.IntegerField()
      jour=models.IntegerField()
      quantite=models.IntegerField()
      valeur=models.IntegerField()
      date=models.DateField()
      type=models.CharField(max_length=50)
      
class Super(models.Model):  
      veille=models.IntegerField()
      jour=models.IntegerField()
      quantite=models.IntegerField()
      valeur=models.IntegerField()
      date=models.DateField()
      type=models.IntegerField()
       
class Gazoil(models.Model):  
      veille=models.IntegerField()
      jour=models.IntegerField()
      quantite=models.IntegerField()
      valeur=models.IntegerField()
      date=models.DateField()
      type=models.IntegerField()
      
class Mairie(models.Model):
      veille=models.IntegerField()
      jour=models.IntegerField()
      quantite=models.IntegerField()
      valeur=models.IntegerField()
      date=models.DateField()
      type=models.CharField(max_length=50)
      type_pay=models.CharField(max_length=50)

class Livraison(models.Model):
      quantite=models.IntegerField()
      valeur=models.IntegerField()
      date=models.DateField()
      Cuve=models.CharField(max_length=50)
      
class User(models.Model):
   
    
    Identifiant=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
   
      
      

      
       

      



      

   
