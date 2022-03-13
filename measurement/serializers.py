from measurement.models import Measurement, Sensor
from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurmentSerializer(read_only=True, many=True)
    class Meta():
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']