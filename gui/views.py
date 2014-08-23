from django.shortcuts import render_to_response
from django.template import RequestContext
from gui.forms import formAlumno


def view_home(request):
	return render_to_response("home.html",
		context_instance=RequestContext(request))

def view_form(request,id):
	form = formAlumno(initial={'id':id})
	ctx = {'form':form}
	return render_to_response("form.html",ctx,
		context_instance=RequestContext(request))
