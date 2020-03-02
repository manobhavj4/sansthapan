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
	
	#if not request.user.is_authenticated:
	#	return redirect('/login')
	#print(request.session.get("first_name","unknown")) #it is getter
	context = {
	"title":"WELCOME TO SANSTHAPAN",
	}
	# if request.user.is_authenticated:
	# 	context["premium_content"] = "Yeahhh it is a premium content"
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
				# contact_form.save(commit=True)
				print("Data inserted into Database Successfullly..!!")

				fullname= contact_form.cleaned_data['fullname']
				phone = contact_form.cleaned_data['phone']
				email = contact_form.cleaned_data['email']
				content = contact_form.cleaned_data['content']

				send_mail('user want to know about sansthapan and here is their details : '+str(fullname),
	                "name : "+str(fullname)+"\n"
	                # "person's photo :"+ attach(personimage)+"\n"
	                "email : "+str(email)+"\n"
	                "phone no : "+str(phone)+"\n"
	                "content : "+ str(content),
	                settings.EMAIL_HOST_USER,
	                ['sansthapanodisha@gmail.com'],
	                fail_silently=False )
				return JsonResponse({"message":"Thank You for your submission..:-)"})

		if contact_form.errors:
			# print(contact_form.cleaned_data)
			errors = contact_form.errors.as_json()
			if request.is_ajax():
				return HttpResponse(errors, status=400, content_type='application/json')

	# if request.method=='POST':
	# 	contact_form=ContactForm(request.POST)
	# 	if contact_form.is_valid():
	# 		print(contact_form.cleaned_data)
	# 		if request.is_ajax():
	# 			return JsonResponse({"message":"Thank You for your submission..:-)"})

	# 	if contact_form.errors:
	# 		# print(contact_form.cleaned_data)
	# 		errors = contact_form.errors.as_json()
	# 		if request.is_ajax():
	# 			return HttpResponse(errors, status=400, content_type='application/json')
	# if request.method=='POST':
	# 	contact_form=ContactForm(request.POST)
	# 	if contact_form.is_valid():
	# 		print(contact_form.cleaned_data)
	# 		return render(request,'homepage.html', {"title":"Thank you for submitting the data","content":"contact page is waiting for u and shortly we are contacting u"})

	return render(request,'contact/contactview.html', context)


class NotificationView(ListView):
# queryset = Product.objects.all()
	template_name = "notification/notification.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(NotificationView, self).get_context_data(*args, **kwargs)
	# 	notification = Notification.objects.get(self.request)
	# 	context['notification'] = notification
	# 	return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Notification.objects.all().order_by("-uploaded_at")
		


class GalleryView(ListView):
# queryset = Product.objects.all()
	template_name = "gallery/gallery.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(NotificationView, self).get_context_data(*args, **kwargs)
	# 	notification = Notification.objects.get(self.request)
	# 	context['notification'] = notification
	# 	return context

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Gallery.objects.all().order_by("-uploaded_at")
		



# from django.core.paginator import Paginator
# from django.shortcuts import render

# from myapp.models import Contact

# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'list.html', {'page_obj': page_obj})






		# next_url= None
		# next_ = request.GET.get('next')
		# redirect_path 	= next_ or None
		# if is_safe_url(redirect_path, request.get_host()):
		# 	return Notification.objects.all().order_by("-uploaded_at")	
		# else:
		# 	return redirect("/")




# def NotificationView(request):

# 	context = {"title":"Hello World!! this is Notification page",
# 	"content":"Notification page is waiting for u",
# 	"form": contact_form
# 	}

# 	return render(request,'notification/notification.html', context)