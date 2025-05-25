from django.urls import path
from tryhello import views

urlpatterns = [path('hello/<str:name>', views.hello_world, name='hello'),]