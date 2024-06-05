from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class ReactView(APIView):
    def get(self,request):
        output = 'hi all'
        return Response(output)
    
    def post(self,request):
        result = {'update added to json request'}
        response_data = {
                        'output': 'success',
                        'explanation': 'File received and processed successfully',
                        'pesudo_code': result
                    }
        return Response(response_data)
    