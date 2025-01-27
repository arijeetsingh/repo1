from django.shortcuts import render, get_object_or_404
from .models import Hotel , City , GalleryPic , Profile , HotelImage
from django.shortcuts import redirect
from .forms import ClientRequestForm 
from django.contrib import messages


def home(request):
	cities=City.objects.all()
	pics=GalleryPic.objects.all()
	profiles=Profile.objects.all()
	title= "Home"
	return render(request,'blog/home.html',{'cities':cities ,'pics':pics ,'profiles':profiles,'title':title})


def about(request):
	title="About Us"
	profiles=Profile.objects.all()
	return render(request,'blog/about.html',{'title':title , 'profiles':profiles})


def city_detail(request,pk):
	city=get_object_or_404(City,pk=pk)
	hotels=Hotel.objects.filter(city_id=city.id)
	title= city.name
	return render(request,'blog/city.html',{'city':city , 'hotels':hotels, 'title':title})
	
def hotel_detail(request,pk):
	hotel=get_object_or_404(Hotel,pk=pk)
	hotel_images=HotelImage.objects.filter(name_id=hotel.id)
	if request.method=='POST':
		form= ClientRequestForm (request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.hotel_name = hotel
			post.save()
			username=form.cleaned_data.get('client_name')
			#messages.success(request,f' {username},we thank u for applying to us! Your request has been successfully generated.' )
			return redirect('blog-home')

	else :
		form= ClientRequestForm ()
	return render(request,'blog/hotel.html',{ 'hotel':hotel, 'form':form, 'hotel_images':hotel_images})


	
