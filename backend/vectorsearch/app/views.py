from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import viewsets
import asyncio
import os
from django.shortcuts import render
import json
from .query_vector_DB import queryVectorDB
import logging
from .models import Task


from .serializer import *
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class TaskQueryClass(APIView):
    def __init__(self):
        self.qvb = None
        self.class_init_bool = False

    @csrf_exempt
    def get(self,request):
        self.qvb = queryVectorDB()
        if self.qvb == False : return
        self.class_init_bool = self.qvb.initiate_weaviate_class()
        return HttpResponseBadRequest("hello world")

    @csrf_exempt
    def post(self,request):
        try:
            data = json.loads(request.body)
            task = data.get('task')
            print(task)
            logging.info('Obtained task input')

            if task is not None:
                
                if self.class_init_bool :
                    result = self.qvb.get_data(task)

                    if result is not None:
                        response_data = {
                            'status': 'success',
                            'message': 'File received and processed successfully',
                            'data': result
                        }
                        print(response_data)
                        return JsonResponse(response_data)
                    else:
                        return HttpResponseBadRequest("Failed to GET the data from vector database")
                else:
                    return HttpResponseBadRequest("Error initiating weaviate collection")
            else:
                return HttpResponseBadRequest("No input received")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")
        
