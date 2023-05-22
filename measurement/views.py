from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sensor, Measurement
from .serializers import SensorListSerializer, SensorDetailSerializer, SensorCreateUpdateSerializer, MeasurementSerializer


class SensorListView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorCreateView(generics.CreateAPIView):
    serializer_class = SensorCreateUpdateSerializer


class SensorUpdateView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateUpdateSerializer


class MeasurementCreateView(generics.CreateAPIView):
    serializer_class = MeasurementSerializer
    parser_classes = [MultiPartParser, FormParser]


class MeasurementListView(generics.ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor']
