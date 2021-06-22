from django.contrib import admin
from .models import StudentModel
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','student_name','rollnumber','student_class','student_age','student_marks','student_attendance']


admin.site.register(StudentModel,StudentAdmin)
