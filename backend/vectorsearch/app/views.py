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
    def post(self,request):
        try:
            data = json.loads(request.body)
            task = data.get('task')

            if task is not None:
                data = task 
                vector_db_endpoint = "http://localhost:8080"
                qvb = queryVectorDB(vector_db_endpoint)
                query = task
                result = qvb.get_data(query)

                if result is not None:
                    response_data = {
                        'status': 'success',
                        'message': 'File received and processed successfully',
                        'data': result
                    }
                    return JsonResponse(response_data)
                else:
                    return HttpResponseBadRequest("Failed to GET the data from vector database")
            else:
                return HttpResponseBadRequest("No input received")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")
        

class SampleClass(APIView):
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)
        