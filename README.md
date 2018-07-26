#Assignment


api-test
It contains a demo of a Customer Onboard app for testing purpose. This demo uses springboot framework to build and mock a prototype of the Customer App for testing.

The Customer Onboarding Application enable customization and a tenant who buys this application can customize the fields to be captured, the validations to be performed, number of views, sub Views, and the workflow for approval. The entire configuration is stored as json in Mongo. When a user logs in based on this configuration dynamic views are presented so that the Customers can be onboarded.


Prerequisites

Python 2.7.14, Postman for creating API mock server, 

package
requests 

The integration test covers the two APIs

/customers used to create a customer
/customers/{id} used to get a customer record

It covers all possible positive and negative scenarios with HTTP Status code validations.

It will generate different test report (JSON, HTML etc) inside build folder as target/ and target/reports

Run Customer App
We can do manual testing as well by running the py file.

Customer on boarding Root directory 
http://127.0.0.1:5000/

will listout all the users in the customers table 
http://127.0.0.1:5000/api/v1/resources/customers/all


Output:
[
   {'id': 1,
     'name':'User 1',
      'address':'Bangalore, Karnataka',
      'status':'INACTIVE',
      'viewId':1,
      'workflowId':1,
      'onboarded':'true'},
    {'id': 2,
     'name':'User 2',
      'address':'Chennai, ThamilNadu',
      'status':'ACTIVE',
      'viewId':1,
      'workflowId':1,
      'onboarded':'false'},
    {'id': 3,
     'name':'User 3',
      'address':'Kolkata, West Bengal',
      'status':'BLOCKED',
      'viewId':1,
      'workflowId':1,
      'onboarded':'false'}
]

by using speicific id 

http://127.0.0.1:5000/api/v1/resources/customers?id=1
 json Response : output 
[
  {
    "address": "Bangalore, Karnataka", 
    "id": 1, 
    "name": "User 1", 
    "onboarded": "true", 
    "status": "INACTIVE", 
    "viewId": 1, 
    "workflowId": 1
  }
]

Error if ID not found in Customer table 

http://127.0.0.1:5000/api/v1/resources/customers?id%20=%2010

{
  "Status": "Not Found", 
  "code": 404
}



