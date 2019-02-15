import behave
import requests
from selenium import webdriver

@given("Request for Patients information for PatientID")
def fetch_patient_information_from_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/patients/view/1")
    context.countText = context.driver.find_element_by_id("info").text
    print(context.countText)
    
@then("Have Patients information available from application")
def check_patient_information_present(context):
    assert len(context.countText)>0,"Patient Info Found"
    
@given("a set of patients for HTML Form")
def submit_html_patient_form(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/patients/register")
    context.currentCount = len(requests.get(
        "http://localhost:8000/patients/list").json())
    context.driver.find_element_by_id("name").send_keys("George")
    context.driver.find_element_by_id("age").send_keys("12")
    context.driver.find_element_by_id("gender").send_keys("Male")
    context.driver.find_element_by_id("height").send_keys("12")
    context.driver.find_element_by_id("weight").send_keys("33")
    context.driver.find_element_by_id("location").send_keys("location")
    context.driver.find_element_by_id("submit").click()
        
@then("increases patient Count from Browser")
def check_patient_information_added(context):
    assert context.currentCount<len(requests.get(
        "http://localhost:8000/patients/list").json()),"Patient Registration Failed"
    
@given("Request for Patient reports for PatientID")
def fetch_patient_reports_from_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/reports/view/1")
    context.countText = context.driver.find_element_by_id("patient_report").text
    print(context.countText)
    
@then("Have Patient reports available from application")
def check_patient_report_present(context):
    assert len(context.countText)>0,"Patient Info Found"
    
@given("information for report form")
def add_patient_report(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/reports/register")
    context.currentCount = len(requests.get(
        "http://localhost:8000/reports/list").json())
    context.driver.find_element_by_id("patient_id").send_keys("1")
    context.driver.find_element_by_id("lm_id").send_keys("1")
    context.driver.find_element_by_id("created").send_keys(" 10102010")
    context.driver.find_element_by_id("description").send_keys("n/a")
    context.driver.find_element_by_id("submit").click()
    
@then("increases report Count from Browser")
def check_report_information_added(context):
    assert context.currentCount<len(requests.get(
        "http://localhost:8000/reports/list").json()),"Report Registration Failed" 
    