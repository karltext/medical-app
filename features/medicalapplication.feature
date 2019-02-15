Feature: Patient Management using Flask 

Scenario: Get the Patient records for PatientID from Browser
	Given Request for Patients information for PatientID
	Then Have Patients information available from application
	
Scenario: Add Patient Details using Browser
	Given a set of patients for HTML Form
	|name		|age	|gender	|height	|weight	|location	|
	|Jimmy		|21		|Male	|123	|123	|Leeds		|
	Then increases patient Count from Browser
	
Scenario: Get the Patients report for PatientID from Browser
	Given Request for Patient reports for PatientID
	Then Have Patient reports available from application

Scenario: Add Report using Browser
	Given information for report form
	|patient_id	|lm_id	|created	|description	|
	|1			|1		|10/10/2010	|n/a			|
	Then increases report Count from Browser
