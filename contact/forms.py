from django import forms
from .models import Contact1
from django.forms import ModelForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

TIME_FORMAT = "h:mm:ss A"
DATE_FORMAT = 'dd mmm yyyy'

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact1
        #fields = '__all__' # PARA MOSTRAR TODOS LOS CAMPOS
        fields = ("name","codigo","areareportante","lugar","fecha","area","hora","subestandar","empresa","riesgo","descripcion", "accion","recomendacion","imagen" )
    
    fecha = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class" :"form-control",
               "type":"date"
    
          }
        )
   )

    hora = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class" :"form-control",
               "type":"time"
    
          }
        )
   )



    descripcion = forms.CharField(
        widget= forms.TextInput(attrs={'style': 'text-align:left;','class':'input-control'}))

    accion = forms.CharField(
        widget= forms.TextInput(attrs={'style': 'text-align:left;','class':'input-control'}))
    
    recomendacion = forms.CharField(
        widget= forms.TextInput(attrs={'style': 'text-align:left;','class':'input-control'}))
    
    #hora = forms.TimeField(input_formats=[TIME_FORMAT],
    #                                widget=TimePickerInput(format=TIME_FORMAT)
    #                                )
    #fecha = forms.DateField(input_formats=[DATE_FORMAT],
    #                                widget=DatePickerInput(format=DATE_FORMAT)
    #                                )
        