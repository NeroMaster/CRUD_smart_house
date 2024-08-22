from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

class SensorListView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer