from django import forms


class formAlumno(forms.Form):
	 id = forms.IntegerField()
	 nombre = forms.CharField()
	 apellidos = forms.CharField()
	 edad = forms.IntegerField()

	


