from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Sensor_id', related_name='sensor')
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Temperature')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date_created')
    image = models.ImageField(blank=True, null=True, verbose_name='Image')

    def __str__(self):
        return f'Sensor Id: {self.sensor}, temperature:{self.temperature} at {self.created_at}'
