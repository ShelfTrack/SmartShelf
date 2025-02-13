from django.http import JsonResponse
from .models import Student
from django.http import HttpResponse

def student_list(request):
    students = list(Student.objects.values())
    return JsonResponse({"students": students})

def home(request):
    return HttpResponse("<h1>Welcome to ShelfTrack - Library Management System</h1>")
