# patients/urls.py
from django.urls import path
from .views import PatientCreateView, PatientListView, DoctorCreateView, DoctorListView, PatientDoctorMappingCreateView, PatientDoctorMappingListView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/create/', PatientCreateView.as_view(), name='patient-create'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor-create'),
    path('mappings/', PatientDoctorMappingCreateView.as_view(), name='mapping-create'),
    path('mappings/', PatientDoctorMappingListView.as_view(), name='mapping-list'),
]
