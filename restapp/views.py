import logging
# import json

from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status


from .models import Student
from .serializers import Testserializers



logger=logging.getLogger('django')
class FirstApiTestView(APIView):
    authentication_classes=[]
    permission_classes=[]
    
    def get(self,request):
        # print(request.headers)
        try:
            data=[]
            students=Student.objects.filter(is_user1=True)
            # print(type(students))
            # for student in students:
            #     data.append({
            #         "name": student.name,  # Iterate through students to access individual student objects
            #         "address": student.address,
            #         "is_admin": student.is_user1,  # Corrected field name
            #     })
            serializer=Testserializers(students,many=True)
            print(serializer)
            msg={
                'request':"name is my done",
                'data':serializer.data
                
            }
            return JsonResponse(msg,status=status.HTTP_200_OK)
        except Exception as e:
            logger.info(str(e),exec_info=True)
               
    def post(self,request):
            data=request.data
            # print(data)
            serializer=Testserializers(data=data)
            if serializer.is_valid():
                serializer.save()
                msg={
                    'code':"200",
                    'msg':'success'                
                }
                return JsonResponse(msg,status=200)
            return JsonResponse(msg,status=status.HTTP_200_OK)
    