from django.http import JsonResponse
from students.models import Student


def studentsView(req):
    students = Student.objects.all()
    # result = []
    # for student in students:
    #     result.append(
    #         {
    #             "id": student.student_id,
    #             "name": student.name,
    #             "branch": student.branch,
    #         }
    #     )
    result = list(students.values())
    return JsonResponse(result, safe=False)
