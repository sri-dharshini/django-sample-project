from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student/record',views.record,name='record'),
    path('search/find',views.find,name='find'),
    path('search/ret',views.ret,name='ret'),
    path('display/ret',views.ret,name='ret'),
    # path('search/find/result',views.find,name='find'),

    path('student/',views.student,name='home'),
    path('search/',views.search,name='search'),

    path('display/',views.display,name='display'),

]
