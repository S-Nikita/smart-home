# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from unicodedata import name
from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurmentSerializer, SensorSerializer


class SetAndGetSensors(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        sensor = Sensor(name=request.data.get('name'), description=request.data.get('description'))
        sensor.save()
        return Response({'status': 'OK'})

class AddMeasurment(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurmentSerializer

class SingleSensorView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
