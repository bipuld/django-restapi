import logging
import json
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status
from restpro import global_msg

from restapp.models import Student,Course
# from .serializers import Testserializers



logger=logging.getLogger('django')
# class FirstApiTestView(APIView):
#     authentication_classes=[]
#     permission_classes=[]
    
#     def get(self,request):
#         # print(request.headers)
#         try:
#             data=[]
#             students=Student.objects.all()
#             serializer=Testserializers(students,many=True)
#             print(serializer)
#             msg={
#                 'request':"name is my done",
#                 'data':serializer.data  
#             }
#             return JsonResponse(msg,status=status.HTTP_200_OK)
#         except Exception as e:
#             logger.info(str(e),exec_info=True)
               
#     def post(self,request):
#             data=request.data
           
#             if not request.body:
#                   return JsonResponse({
#                 "response_code": global_msg.UNSUCCESS_RESPONSE_CODE,
#                 "response": "Body is required",
               
#                 })
                
#             serializer=Testserializers(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 msg={
#                     'code':global_msg.SUCCESS_RESPONSE_CODE,
#                     'msg':'success'                
#                 }
#                 return JsonResponse(msg,status=200)
#             # return JsonResponse(msg,status=status.HTTP_200_ACCEPTED)
           
#             return JsonResponse({
#                 "response_code": global_msg.UNSUCCESS_RESPONSE_CODE,
#                 "response": "Something Were Wrong",
#                 "error": serializer.errors
#             })


class StudentCreateApiView(APIView):
    '''this class view basically create the new student'''
    authentication_classes=[]
    permission_classes=[]
    def post(self,request):
        if not request.body:
            message={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY:"For Creating Student Body Is Required"
            }
            return JsonResponse(message,status=status.HTTP_404_NOT_FOUND)
        try:
            error_list=[]
            data=request.data
            # name=str(data['name']).strip() if 'name' in data else ''
            # if not name:
            #     error_list.append("Name is required for the user")        
            # name=str(data['name']).strip() if 'name' in data else ''
            # if not name:
            #     error_list.append("Name is required for the user")          
            # address=str(data['address']).strip() if 'address' in data else ''
            # if not address:
            #     error_list.append("address is required for the user")     
            # mobile_num=(data['name']).strip() if 'mobile_num' in data else ''
            # if not mobile_num:
            #     error_list.append("mobile_num is required for the user")      
            # roll_number=(data['name']).strip() if 'roll_number' in data else ''
            # if not roll_number:
            #     error_list.append("roll_number is required for the user")
            # if error_list:
            #     message={
            #     global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
            #     global_msg.RESPONSE_MSG_KEY:"Invalid data !!!!!",
            #     global_msg.ERROR_KEY:error_list
            #             }
            #     return JsonResponse(message,status=status.HTTP_404_NOT_FOUND)
            # user=User.objects.get(username="Bipul")
            # Student.objects.create(name=name,address=address,age=age,mobile_num=mobile_num,roll_number=roll_number,created_by=user)
            message={
                global_msg.RESPONSE_CODE_KEY:global_msg.SUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY:"Success !!!!!"
            }
            return JsonResponse(message,status=status.HTTP_202_ACCEPTED)
        except Exception as exe:
            logger.error(str(exe),exc_info=True)
            
class StudentListeApiView(APIView):
    def get(self,request):
        pass
    
class StudentEditApiView(APIView):
    def put(self,request):
        pass
class StudentDeleteApiView(APIView):
    def delete(self,request):
        pass