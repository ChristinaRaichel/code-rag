from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import asyncio
import os
from django.shortcuts import render
import json
from .query_vector_DB import queryVectorDB
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def get_code_and_data(request):
    """
    Args:
        request (file): File object of form data

    Returns:
        JsonResponse: Formatted JsonResponse object on success
        """
    logger.info("get code views up and running")
                
    if request.method == 'POST':
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
    else:
        return HttpResponseBadRequest("Invalid request method")
    