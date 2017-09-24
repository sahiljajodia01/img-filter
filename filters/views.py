from django.shortcuts import render
import cloudinary as Cloud

def home_page(request):
	Cloud.uploader.upload("/home/jajodia/PycharmProjects/img_con/img_con/car.jpg", public_id="car")
	car = Cloud.CloudinaryImage('car.jpg')
	print(car.url)

	return render(request, "index.html")






