from django.http import HttpResponse
from tryhello.models import Students
import datetime

def hello_world(request,name):
    # adding in DB
    # s1 = Students(name = name, age = 10, dob = datetime.date.today())
    # s1.save() # to save in DB

    # getting data of all student
    all_students = Students.objects.all()

    #geeting specific student and updating a column
    student_1 = Students.objects.get(name=name)
    student_1.age = 15
    student_1.save()
    return HttpResponse("Hello, your details are " + student_1.name + " updated age " + str(student_1.age) + " dob " + str(student_1.dob))

