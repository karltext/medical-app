import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("Request for All Patients")
def fetch_patients_from_api(context):
    context.pts = requests.get("http://localhost:8000/patients/list").json()
    
@then("Have all Patients available from application")
def check_all_patients_present(context):
    ok_(len(context.pts)>0,"Patients Not Available")