# patients/models.py
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    medical_history = models.TextField(default="No medical history provided.")  # Added default value

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
    

