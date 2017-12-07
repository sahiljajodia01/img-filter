from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
import cloudinary
from .models import Pic
from .forms import PicForm

def upload(request):
	# Cloud.uploader.upload("/home/jajodia/PycharmProjects/img_con/img_con/car.jpg", public_id="car")
	# car = Cloud.CloudinaryImage('car.jpg')
	# print(car.url)
	if request.method == 'POST':
		form = PicForm(request.POST, request.FILES)
		if form.is_valid():
			image = request.FILES['image']
			name = request.POST['name']
			filter = request.POST['filter']
			cloudinary.uploader.upload(image, public_id=name, effect=filter)
			instance = Pic(name=name)
			instance.save()

			return HttpResponseRedirect('show')
	else:
		form = PicForm()

	context = { 'backend_form': form }
	return render(request, "index.html", context)

def show(request):
	photo = Pic.objects.all()
	context = { 'photo': photo }
	return render(request, 'show.html', context)










