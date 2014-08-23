from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render_to_response
from django.template  import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from quickstart.serializers import AlumnoSerializer
from quickstart.models import alumno

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def alumno_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    #mostrando todos los datos
    if request.method == 'GET':
        alumnos = alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return JSONResponse(serializer.data)
    #agregando un nuevo registro
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = alumnoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def alumno_proces(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Alumno = alumno.objects.get(pk=pk)
    except alumno.DoesNotExist:
        return HttpResponse(status=404)

     #comprobando la existencia del registro
    if request.method == 'GET':
        serializer = AlumnoSerializer(Alumno)
        return JSONResponse(serializer.data)
    #actualizando el dato
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AlumnoSerializer(Alumno, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    #eliminado
    elif request.method == 'DELETE':
        Alumno.delete()
        return HttpResponse(status=204)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

