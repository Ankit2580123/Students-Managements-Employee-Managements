from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=18)
    branch=models.TextField(max_length=100)
    roll_no=models.IntegerField()
    random_count=models.IntegerField(default=1)
    

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

class Subject_Marks(models.Model):
    student=models.ForeignKey(Students,related_name="student_marks" , on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)


    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class meta:
        unique_together=['student','subject']

class Students_Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, help_text='Enter phone number')
    photo=models.ImageField(upload_to="Images")





class Cars(models.Model):
    car_name=models.CharField(max_length=100)
    top_speed=models.CharField(default=50)
    color=models.TextField(max_length=15)

    def __str__(self):
        return self.car_name



class Department(models.Model):
    department=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']

class EmployeeID(models.Model):
    employee_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.employee_id
    
class Employees(models.Model):
    department=models.ForeignKey(Department,related_name='depart', on_delete=models.CASCADE)
    employee_id=models.OneToOneField(EmployeeID,related_name='employeeid', on_delete=models.CASCADE)
    employee_name=models.CharField(max_length=100)
    employee_email=models.EmailField(unique=True)
    employee_age=models.IntegerField(default=18)
    employee_address=models.TextField()

    def __str__(self) -> str:
        return self.employee_name
    
    class meta:
        ordering=['-employee_name']
        verbose_name="employees"



   