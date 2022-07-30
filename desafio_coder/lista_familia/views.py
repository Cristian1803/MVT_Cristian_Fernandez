from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from lista_familia.models import familiar


# Create your views here.

#def familiares(request):

#    datos = {"familiares": ["Cristian","Marcelo","Miguel","Carmen"], "apellido":["Fernandez","Rios","Lopez","Rodriguez"]}

#    plantilla = loader.get_template("familiares.html")

#    documento = plantilla.render(datos)



#    return HttpResponse(documento)


def familiares(request):
    famil = familiar.objects.all()

    return render(request,"familiares.html", {"familiares": famil})





