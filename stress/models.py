from django.db import models

class StressInput(models.Model):
    snoring_rate = models.FloatField()
    respiratory_rate = models.FloatField()
    body_temperature = models.FloatField()
    limb_movement = models.FloatField()
    blood_oxygen_level = models.FloatField()
    eye_movement = models.FloatField()
    sleeping_hours = models.FloatField()
    heart_rate = models.FloatField()

    stress_level = models.IntegerField(choices=[(0, "No Stress"), (1, "Stress")])
