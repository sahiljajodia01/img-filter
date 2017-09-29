from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
import cloudinary as Cloud
from .models import Pic
from .forms import PicForm
from django import forms
from cloudinary.forms import cl_init_js_callbacks

def upload(request):
	# Cloud.uploader.upload("/home/jajodia/PycharmProjects/img_con/img_con/car.jpg", public_id="car")
	# car = Cloud.CloudinaryImage('car.jpg')
	# print(car.url)
	backend_form = PicForm(request.POST, request.FILES)
	if backend_form.is_valid():
		instance = backend_form.save(commit=False)
		instance.save()
		return redirect("show")

	context = { 'backend_form': backend_form }
	return render(request, "index.html", context)

def show(request):
	photo = Pic.objects.all()
	photo_pic = Cloud.CloudinaryImage(photo)
	url = photo_pic.url
	context = { 'photo': photo_pic, 'photo_url': url }
	return render(request, 'show.html', context)










