from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print(kwargs)
        print(kwargs.get('id'))
        id = kwargs.get('id')

        if id:
            result = Students.objects.get(id=id)
            serializers = StudentSerializer(result)
            return Response({'status':'success', 'students':serializers.data}, status=200)
        else:
            result = Students.objects.all()
            serializers = StudentSerializer(result, many=True)
            return Response({'status': 'success', 'students':serializers.data}, status=200)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data': serializer.data}, status = status.HTTP_200_OK)
        else:
            return Response({'status':'success', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,  *args, **kwargs):
        id = kwargs.get('id')
        student = Students.objects.filter(id=id)
        student.delete()
        return Response({"status":"success", "data":"record deleted"})