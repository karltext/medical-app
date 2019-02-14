import behave
from pip._vendor import requests
from nose.tools.trivial import ok_
from selenium import webdriver

@given("Request for Patients information for PatientID")
def fetch_patient_information_from_api(context):
#    context.pts = requests.get("http://localhost:8000/patients/view/1")
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/patients/view/1")
    context.countText = context.driver.find_element_by_id("info").text
    print(context.countText)
    
@then("Have Patients information available from application")
def check_patient_information_present(context):
    ok_(len(context.countText)>0,"Patient Info Found")
    
@given("a set of patients for HTML Form")
def submit_html_patient_form(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/patients/register")
    context.driver.find_element_by_id("name").send_keys("George")
    context.driver.find_element_by_id("age").send_keys("age")
    context.driver.find_element_by_id("gender").send_keys("gender")
    context.driver.find_element_by_id("height").send_keys("height")
    context.driver.find_element_by_id("weight").send_keys("weight")
    context.driver.find_element_by_id("location").send_keys("location")
    context.driver.find_element_by_id("submit").click()
        
@then("increases patient Count from Browser")
def check_patient_information_added(context):
    pass