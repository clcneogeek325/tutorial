from django.db import models

class alumno(models.Model):
	 nombre = models.CharField(max_length=50)
	 apellidos = models.CharField(max_length=50)
	 edad = models.IntegerField(max_length=3)
	 status = models.BooleanField(default=True)
	 def __unicode__(self):
		 return self.nombre


