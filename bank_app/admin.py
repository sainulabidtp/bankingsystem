from django.contrib import admin
from . models import District,Branch,ApplicationForm,MaterialProvided



# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # Display 'name' and 'slug' fields in the admin list view
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(District,DistrictAdmin)
admin.site.register(Branch)
admin.site.register(MaterialProvided)
admin.site.register(ApplicationForm)