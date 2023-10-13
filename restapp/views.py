import logging


from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status


from .models import Teacher,Student





logger=logging.getLogger('django')
class FirstApiTestView(APIView):
    authentication_classes=[]
    permission_classes=[]
    
    def get(self,request):
        # print(request.headers)
        try:
            data=[]
            students=Student.objects.all()
            for student in students:
                data.append({
                    "name": student.name,  # Iterate through students to access individual student objects
                    "address": student.address,
                    "is_admin": student.is_user1,  # Corrected field name
                })
            msg={
                'request':"name is my done",
                'data':data
                
            }
            return JsonResponse(msg,status=status.HTTP_200_OK)
        except Exception as e:
            logger.info(str(e),exec_info=True)
               
    # def post(self,request):
