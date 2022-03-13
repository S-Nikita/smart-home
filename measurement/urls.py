from django.urls import path

from measurement.views import SetAndGetSensors, AddMeasurment, SingleSensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SetAndGetSensors.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
    path('measurements/', AddMeasurment.as_view()),
]
