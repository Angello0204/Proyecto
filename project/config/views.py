from django.http import HttpResponse 
from django.template import Context , Template
from django.shortcuts import render

def saludo(request):
    return HttpResponse ("Hola django")


def probando_template(request):
    mi_html = open("./templates/template1.html") 
    mi_template = Template(mi_html.read()) 
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)


def mis_notas(request):
    
    return render(request ,"notas.html")