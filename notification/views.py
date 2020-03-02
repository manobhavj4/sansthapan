from django.shortcuts import render
from django.http import Http404,JsonResponse,HttpResponse

from django.shortcuts import render,redirect
from notification.forms import ContactForm

from django.views.generic import ListView
from .models import Notification, Gallery
from django.core.mail import send_mail,EmailMessage

from django.utils.http import is_safe_url
from django.conf import settings

from django.core.paginator import Paginator

# Create your views here.


def HomeView(request):
	
	context = {
	"title":"WELCOME TO SANSTHAPAN",
	}
	return render(request,'homepage/home.html', context)

def AboutView(request):
	context = {"title":"About Us",
	 }
	return render(request,'homepage/about.html', context)

def ContactView(request):
	contact_form = ContactForm()
	context = {"title":"Contact Us",
	"form": contact_form
	}

	if request.method=='POST':
		contact_form=ContactForm(request.POST)
		if contact_form.is_valid():
			if request.is_ajax():
				
				fullname= contact_form.cleaned_data['fullname']
				phone = contact_form.cleaned_data['phone']
				email = contact_form.cleaned_data['email']
				content = contact_form.cleaned_data['content']

				send_mail('user want to know about sansthapan and here is their details : '+str(fullname),
	                "name : "+str(fullname)+"\n"
	                "email : "+str(email)+"\n"
	                "phone no : "+str(phone)+"\n"
	                "content : "+ str(content),
	                settings.EMAIL_HOST_USER,
	                ['sansthapanodisha@gmail.com'],
	                fail_silently=False )
				return JsonResponse({"message":"Thank You for your submission..:-)"})

		if contact_form.errors:

			errors = contact_form.errors.as_json()
			if request.is_ajax():
				return HttpResponse(errors, status=400, content_type='application/json')

	return render(request,'contact/contactview.html', context)


class NotificationView(ListView):
	template_name = "notification/notification.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Notification.objects.all().order_by("-uploaded_at")
		


class GalleryView(ListView):
	template_name = "gallery/gallery.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Gallery.objects.all().order_by("-uploaded_at")
		


