from django.http import JsonResponse
from .models import Student

def student_list(request):
    students = list(Student.objects.values())
    return JsonResponse({"students": students})
