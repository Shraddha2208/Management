from django.db import models

# Create your models here.


# Create your models here.

class StudentModel(models.Model):
    id = models.IntegerField(primary_key = True)
    student_name = models.CharField(max_length=80)
    rollnumber = models.CharField(max_length=10)
    student_class = models.IntegerField()
    student_age = models.IntegerField()
    student_marks = models.IntegerField()
    student_attendance = models.IntegerField()
 
    def __str__(self):
        return f"{self.student_name} : {self.rollnumber} : {self.student_class} : {self.student_age} : {self.student_marks} : {self.student_attendance}"