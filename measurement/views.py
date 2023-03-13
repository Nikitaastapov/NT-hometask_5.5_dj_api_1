# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from datetime import date
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
class MeasurementCreateView(CreateAPIView):
      queryset = Measurement.objects.all()
      serializer_class = MeasurementSerializer

      def measure_create(self, request, serializer_class):
          sensor_id = Sensor.objects.filter(id = self.request.data.get('sensor'))
          return serializer_class.save(sensor_id = sensor_id)
      

      
      
