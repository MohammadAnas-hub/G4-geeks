from tkinter.messagebox import RETRY
from API.models import Word
from API.serializers import WordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from difflib import SequenceMatcher

def scoringFunction(correct, test):
    return SequenceMatcher(None, correct, test).ratio()

@api_view(['POST'])
def CreateWordView(request):

    ReqData = request.data

    try:
        print(1111, ReqData["pronunciation"])
        ReqData["score"] = str(scoringFunction("hello", ReqData["pronunciation"]))
        serializers = WordSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)