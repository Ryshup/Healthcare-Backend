from django.contrib import admin
from .models import Doctor, Patient, PatientDoctorMapping

# Register the models to be visible in Django Admin
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientDoctorMapping)
