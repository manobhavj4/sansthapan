from django.contrib import admin

from .models import Notification, Gallery

class NotificationAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'title']
	class Meta:
		model = Notification

admin.site.register(Notification, NotificationAdmin)


class GalleryAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'title']
	class Meta:
		model = Gallery


admin.site.register(Gallery, GalleryAdmin)
