from django.shortcuts import render,redirect
import csv
import os
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def student(request):
        return render(request,'student.html')
def record(request):
        StudentId=request.POST['id']
        StudentName=request.POST['studentname']
        Gender=request.POST['gender']
        DateOfBirth=request.POST['dob']
        City=request.POST['city']
        State=request.POST['state']
        EmailId=request.POST['mail']
        Qualification=request.POST['qualification']
        Stream=request.POST['stream']

        details=[StudentId,StudentName,Gender,DateOfBirth,City,State,EmailId,Qualification,Stream]

        with open('students.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(details)
            return redirect('http://127.0.0.1:8000/')

def find(request):
    Id=request.POST['id']
    path =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(path, 'students.csv')
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == Id:
                StudentId=row[0]
                StudentName=row[1]
                Gender=row[2]
                DateOfBirth=row[3]
                City=row[4]
                State=row[5]
                EmailId=row[6]
                Qualification=row[7]
                Stream=row[8]

                return render(request,'result.html', {'id' : StudentId,'name' : StudentName,'gen' : Gender,'dob' : DateOfBirth,'cit' : City ,'sta' : State,'mai' : EmailId,'qua' : Qualification, 'str' : Stream} )

def ret(request):
    return redirect('http://127.0.0.1:8000/')







def search(request):
    return render(request,'search.html')
def display(request):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(path, 'students.csv')
    rows=[]
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            StudentId=row[0]
            StudentName=row[1]
            Gender=row[2]
            DateOfBirth=row[3]
            City=row[4]
            State=row[5]
            EmailId=row[6]
            Qualification=row[7]
            Stream=row[8]
            rowdict = {'id' : StudentId,'name' : StudentName,'gen' : Gender,
                        'dob' : DateOfBirth,'cit' : City ,'sta' : State,'mai' : EmailId,'qua' : Qualification, 'stream' : Stream}
            rows.append(rowdict)

    return render(request,'display.html',{'rows' : rows} )
