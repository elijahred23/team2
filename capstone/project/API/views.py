#from django.shortcuts import render

from rest_framework import generics

from .models import *
from .serializers import *


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class VeteranList(generics.ListAPIView):
    queryset = Veteran.objects.all()
    serializer_class = VeteranSerializer


class VeteranDetail(APIView):
    """queryset = Veteran.objects.all()
    serializer_class = VeteranSerializer"""

    def get_object(self, pk):
        try:
            return Veteran.objects.get(veteranID=pk)
        except Veteran.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        veteran = self.get_object(pk)
        serializer = VeteranSerializer(veteran)
        return Response(serializer.data)


class InterviewerList(generics.ListAPIView):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

    #figure out query params

class InterviewerDetail(APIView):
    """queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer"""

    def get_object(self, pk):
        try:
            return Interviewer.objects.get(interviewerID=pk)
        except Interviewer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        interviewer = self.get_object(pk)
        serializer = InterviewerSerializer(interviewer)
        return Response(serializer.data)


class InterviewList(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class InterviewDetail(APIView):
    """queryset = Interview.objects.all()
    serializer_class = InterviewSerializer"""

    def get_object(self, pk):
        try:
            return Interview.objects.get(interviewID=pk)
        except Interview.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        interview = self.get_object(pk)
        serializer = InterviewSerializer(interview)
        return Response(serializer.data)

class AudioList(generics.ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

class AudioDetail(APIView):
    """queryset = Audio.objects.all()
    serializer_class = AudioSerializer"""

    def get_object(self, pk):
        try:
            return Audio.objects.get(audioID=pk)
        except Audio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        audio = self.get_object(pk)
        serializer = AudioSerializer(audio)
        return Response(serializer.data)

    
