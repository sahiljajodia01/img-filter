from django import forms

class PicForm(forms.Form):
	name = forms.CharField(max_length=100)
	image = forms.FileField()
	filter = forms.CharField(max_length=55)


