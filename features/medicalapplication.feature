Feature: Patient Management using Flask 

Scenario: Get the Patient records for PatientID from Browser
	Given Request for Patients information for PatientID
	Then Have Patients information available from application
	
Scenario: Add Patient Details using Browser
	Given a set of patients for HTML Form
	|patient_id	|name		|age	|gender	|height	|weight	|location	|
	|123		|Jimmy		|21		|Male	|123	|123	|Leeds		|
	Then increases patient Count from Browser