'''
Created on Jul 27, 2018

@author: narendra_v
'''
import simplejson
import unittest
from APIservices import APIservices

class Customer(unittest.TestCase):
    def __init__(self):
        self.ser = APIservices()
        self.host = 'http://localhost:5000'
        self.allcustomer = 'http://localhost:5000/api/v1/resources/customers/all'
        self.id = '0'
        
        self.url_id = 'http://localhost:5000/api/v1/resources/customers?id='
        self.url_create = 'http://localhost:5000/api/v1/resources/customers/create'
        self.id = 4
        self.name = 'Narendra'
        self.workflowid = 1 
        self.viewId = 2 
        self.address = 'Bangalore' 
        self.onboarded = 'true' 
        self.status = 'Active'
        
    def home_screen(self,url):
        
        result = self.ser.get_method(url)
        return  result.content  
    
    def customer_all(self, url):
    
        response = self.ser.get_method(url)
        #print response.status_code
        result = response.json()
        #print len(result), result, response.status_code -- gives the information of the customer
        return  result
    
    def customer_id(self, id):
        uri = self.url_id + str(id)  #-----concating 'ID' with 'url' 
        #print uri
        response = self.ser.get_method(uri)
        #print response.status_code
        #result = response.json()
        
        if(response.status_code == 200):
            return "Status: 200  --- OK" 
        else: 
            return "Status: 404 -  'Not found'"
         
    
    def customer_create(self, name, id, workflowid, address, viewId, onboarded, status):
        
        body = {
            'id': 4,
            'name': name,
            'address': address,
            'status':status,
            'viewId': int(viewId),
            'workflowId': int(workflowid),
            'onboarded':onboarded
            }

        result = self.ser.post_method(body)
        
        if (result.status_code == 403):
            return "Status: 403 -  'Forbidden'"
        else:
            return "Sucessfully Created the User with Id = "+str(id )+" and Status Code = " +str(result.status_code)  
    
    
if __name__ == '__main__':
    #unittest.main() 
    cus = Customer()
#-- Home Screen -------
    cus.home_screen(cus.host)
#--- List out all the customer --------
    cus.customer_all(cus.allcustomer)
#--- customer based on given id --------
#print cus.customer_id(1)
#--- creating New customer --------
    cus.customer_create(cus.name, cus.id, cus.workflowid, cus.address,cus.viewId, cus.onboarded, cus.status) # -- will sucessfully create the user '4' 
#------ verify the created user with id 4 
    cus.customer_id(id = 4)

