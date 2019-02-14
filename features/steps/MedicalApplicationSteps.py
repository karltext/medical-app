import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("Request for Patients records for PatientID")
def fetch_patient_records_from_api(context):
    context.pts = requests.get("http://localhost:8000/patients/view/1")
    
@then("Have Patients records available from application")
def check_patient_records_present(context):
    ok_(len(context.pts)>0,"Patient Records Not Available")