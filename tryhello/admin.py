from django.contrib import admin

from tryhello.models import Students, Course, StudentCourse

# Register your models here.
# admin.site.register(Students)
admin.site.register(Course)
admin.site.register(StudentCourse)

# Modifying Student class and customizing the panel for editing and adding student
class StudentAdmin(admin.ModelAdmin):
    list_filter = (('name'),) #Tuple
    list_display = ('id', 'name', 'age')
    # list_display_links = (('name'),)
    list_editable = (('name'),)
    search_fields = ('name',)
admin.site.register(Students, StudentAdmin)
