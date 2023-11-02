import logging
import json

from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status
from restpro import global_msg

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
            students=Student.objects.all()
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
           
            if not request.body:
                  return JsonResponse({
                "response_code": global_msg.UNSUCCESS_RESPONSE_CODE,
                "response": "Body is required",
               
                })
                
            serializer=Testserializers(data=data)
            if serializer.is_valid():
                serializer.save()
                msg={
                    'code':global_msg.SUCCESS_RESPONSE_CODE,
                    'msg':'success'                
                }
                return JsonResponse(msg,status=200)
            # return JsonResponse(msg,status=status.HTTP_200_ACCEPTED)
           
            return JsonResponse({
                "response_code": global_msg.UNSUCCESS_RESPONSE_CODE,
                "response": "Something Were Wrong",
                "error": serializer.errors
            })
    