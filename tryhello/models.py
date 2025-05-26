from django.db import models
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_days = models.IntegerField()
    max_capacity = models.IntegerField()
    is_active = models.BooleanField(default=True) # added for updating model, created 0002


class StudentCourse(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled = models.BooleanField(default=False)
    enroll_date = models.DateField()

class TestTable(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Test_Table'
        ordering = ['-name'] #desending ordering
    # study in details models.<parameters>
    # for eg instead of foreignkey you can have onetomany, manytomany parameters



