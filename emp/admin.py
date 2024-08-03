from django.contrib import admin
# from emp.models import emp,Testimonial
from emp import models
from emp.models import Testimonial

# Register your models here.

class empAdmin(admin.ModelAdmin):
    list_display=('name','working','department')
    search_fields=['name']


admin.site.register(models.emp,empAdmin) 
admin.site.register(Testimonial)