from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
import datetime
from forms_django import settings


# Create your models here.

def mage(self,filename):
    ruta = "img/%s/%s"%(self.name,str(filename))
    return ruta

def get_default_my_hour():
    hora_actual = datetime.datetime.now()
    formatedHour = hora_actual.strftime("%H:%M:%S")
    return formatedHour

class Contact1(models.Model):
    YES_CHOICES = (       # example of 1, there can be only one selection
    ('CONDICIÓNSUBESTÁNDAR', 'Condición Sub-estándar'),
    ('ACTOSUBESTÁNDAR', 'Acto Sub-estándar'),
    )
    EMPRESA = (       # example of 1, there can be only one selection
    ('FAMESAEXPLOSIVOS', 'Famesa Explosivos'),
    ('TERCEROS', 'Terceros'),
    )
    RIESGO = (       # example of 1, there can be only one selection
    ('BAJO', 'Bajo'),
    ('MEDIO', 'Medio'),
    ('ALTO', 'Alto'),
    )

   
    def imagen1(self):
        return mark_safe('<a href="/media/%s"> <img src="/media/%s" width=50px height=50px /> </a>'%(self.imagen, self.imagen))
    name = models.CharField(max_length=70, verbose_name='Nombre y Apellido', blank=True) #null=True (para datos fechas o números)
    lugar = models.CharField(max_length=100,verbose_name="Lugar")
    fecha = models.DateField(verbose_name="Fecha", default=datetime.date.today)
    area = models.CharField(max_length=100,verbose_name="Área")
    hora = models.TimeField( verbose_name="Hora") 
    #email = models.EmailField(verbose_name='Correo electrónico')
    subestandar = models.CharField(max_length=80, choices=YES_CHOICES, verbose_name="Tipo De Evento")
    empresa = models.CharField(max_length=80, choices=EMPRESA, verbose_name="Empresa")
    riesgo = models.CharField(max_length=80, choices=RIESGO, verbose_name="Riesgo")
    #actosubestandar = models.BooleanField(default=False, verbose_name='Acto Sub-estándar')
    #condicionsubestandar = models.BooleanField(default=False, verbose_name='Condición Sub-estándar')
    descripcion = models.TextField(max_length=100,verbose_name='Descripción De Lo Sucedido')
    accion = models.TextField(max_length=100,verbose_name='Plan De Acción')
    recomendacion = models.TextField(max_length=80,verbose_name='Recomendación')
    codigo = models.IntegerField(verbose_name='Código/DNI', null=True)
    areareportante = models.CharField(max_length=50, verbose_name='Área Reportante', blank=True)

    imagen = models.ImageField(upload_to=mage)
    #firma = models.ImageField(upload_to=mage)

    class Meta:      
        verbose_name_plural = 'Contact1s'



   
