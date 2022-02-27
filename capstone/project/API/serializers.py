from rest_framework import serializers
from . models import *

class VeteranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veteran
        fields = [
            "veteranID",
            "veteranFirstName",
            "veteranLastName",
        ]

"""
class VeteranListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veteran
        fields = [
            "veteranID",
            "veteranFirstName",
            "veteranLastName",
        ]

"""

class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = [
            "interviewerID",
            "interviewerFirstName",
            "interviewerLastName",
        ]


"""
class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = [
            "interviewerID",
            "interviewerFirstName",
            "interviewerLastName",
        ]
"""

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = [
            "audioID",
            "audioLength",
        ]

class InterviewSerializer(serializers.ModelSerializer):
    veteran = VeteranSerializer()
    interviewer = InterviewerSerializer()
    audio = AudioSerializer()

    class Meta:
        model = Interview
        fields = [
            "interviewID",
            "interviewDate",
            "veteran",
            "interviewer",
            "audio",
        ]

"""
class InterviewSerializer():
    veteran = VeteranSerializer()
    interviewer = InterviewerSerializer()
    audio = AudioSerializer()

    class Meta:
        model = Interview
        fields = [
            "interviewID",
            "interviewDate",
            "veteran",
            "interviewer",
            "audio",
        ]
"""