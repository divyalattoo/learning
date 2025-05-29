from django.http import HttpResponse
from tryhello.models import Students
import datetime


# Creating a method (function)
def hello_world(request,name : str, dob :datetime.date):


    # getting data of all student
    all_students = Students.objects.all()

    #getting specific student by name and updating a column
    if name in [student.name for student in all_students]:
        student_1 = Students.objects.get(name=name)
        return HttpResponse("Hello, your details are " + student_1.name + " Age " + str(student_1.age) + " dob " + str(student_1.dob))
    else:
        # to save in DB
        dob = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
        age = datetime.date.today().year - dob.year
        student_1 = Students(name = name, age = age, dob = dob)
        student_1.save() #
        return HttpResponse( "Hello, your details are added in DB " + student_1.name + " Age " + str(student_1.age) + " dob " + str(student_1.dob))
    # return HttpResponse("Hello, your name is" + name)
