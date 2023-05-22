from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='measurements/', blank=True, null=True)

    def __str__(self):
        return f'{self.sensor} - {self.temperature} at {self.created_at}'