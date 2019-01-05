#User admin models

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from .models import Customer

@admin.register(Customer)
class ProfileAdmin(UserAdmin):
	#Profile Admin
	list_display = ('pk','first_Name','last_Name','city','state')
	list_display_links = ('pk','first_Name')
	search_fields = (
		'user__first_name',
		'user__last_name',
	)

	list_filter = (
		'created',
		'modified',
	)

	fieldsets = (
		('Profile',{
			'fields':(('first_Name','last_Name'),),
		}),
		('Extra Info',{
			'fields':(
				('city','state'),
				('zipNumber')
				)
		}),
		('Metadata',{
			'fields':(('created','modified'),),
		})
	)

admin.site.unregister(Customer)
admin.site.register(Customer)
