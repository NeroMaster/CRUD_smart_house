from django.urls import path
from .views import SensorListView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/<pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]


