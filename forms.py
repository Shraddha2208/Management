from django import forms
from .models import StudentModel




class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ('id','student_name','rollnumber','student_class','student_age','student_marks','student_attendance')