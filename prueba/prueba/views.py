from django.http import HttpResponse


def home(request):
    return HttpResponse("Usted esta en la página de Inicio")