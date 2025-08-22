from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def studentsView(req):
    if req.method == "GET":
        # get all students from table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == "POST":
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def studentDetailView(req, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(
            {"message": f"No student present with id {id}"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if req.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif req.method == "PUT":
        student_data = StudentSerializer(student).data
        data = {**student_data, **req.data}
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
