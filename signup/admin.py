from django.contrib import admin
from .models import Register,AdminRegister,FacultyRegister
# Register your models here.

admin.site.register(Register)
admin.site.register(AdminRegister)
admin.site.register(FacultyRegister)
