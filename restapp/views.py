from django.shortcuts import render
from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
import logging

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import status

# import logger
# Create your views here.
logger=logging.getLogger('django')
class FirstApiTestView(APIView):
    authentication_classes=[]
    permission_classes=[]
    
    def get(self,request):
        try:
            msg={
                'request':"Sucess",
                'data':[{"name":"Bipul",
                         'age':24,
                         'address':"Chitwan"
                         }
                        ]
                
            }
            return JsonResponse(msg,status=status.HTTP_200_OK)
        except Exception as e:
            logger.info(str(e),exec_info=True)
    