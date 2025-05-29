from django.http import HttpResponse
from tryhello.models import Students
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Creating a method (function)
@api_view(['GET','POST'])
def hello_world(request,name : str, age : int ,dob :datetime.date):


    # getting data of all student
    all_students = Students.objects.all()

    #geeting specific student and updating a column
    if name in [student.name for student in all_students]:
        student_1 = Students.objects.get(name=name)
        return HttpResponse("Hello, your details are " + student_1.name + " Age " + str(student_1.age) + " dob " + str(student_1.dob))
    else:
        # to save in DB
        student_1 = Students(name = name, age = age, dob = dob)
        student_1.save() #
        return HttpResponse( "Hello, your details are added in DB " + student_1.name + " Age " + str(student_1.age) + " dob " + str(student_1.dob))
    return Response({"message": "Hello, your name is " + name}, status=status.HTTP_200_OK)
    # return HttpResponse("Hello, your name is" + name)
