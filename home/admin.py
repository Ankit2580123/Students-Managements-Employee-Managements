from django.contrib import admin
from home.models import *

# Register your models here.


# class Employee_Info(admin.ModelAdmin):
  
#   list_display = ("Employee_name","Employee_email", "Employee_age",)


admin.site.register(Students)
admin.site.register(Subject)
admin.site.register(Subject_Marks)



admin.site.register(EmployeeID)
admin.site.register(Department)
admin.site.register(Employees)
