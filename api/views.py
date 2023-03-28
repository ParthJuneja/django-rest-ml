from requests import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ml import predict

# def getData(request):
#     return Response(predict('Hello, i am a test string, how are you?'))


@api_view(['GET'])
def getPred(request):
    text = request.GET['text']
    return Response(predict())