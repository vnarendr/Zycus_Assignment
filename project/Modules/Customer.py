'''
Created on Jul 27, 2018

@author: narendra_v
'''
from Modules.APIservices import APIservices

ser = APIservices()

class Customer():
    def __init__(self):
        self.host = 'http://localhost:5000'
        self.allcustomer = 'http://localhost:5000/api/v1/resources/customers/all'
        self.id = '0'
        
        self.url_id = 'http://localhost:5000/api/v1/resources/customers?id='
        self.name = 'Narendra'
        self.workflowid = 1 
        self.viewId = 2 
        self.address = 'Bangalore' 
        self.onboarded = 'true' 
        self.status = 'Active'
        
    def home_screen(self,url):
        
        result = ser.get_method(url)
        return  result.content  
    
    def customer_all(self, url):
    
        response = ser.get_method(url)
        result = response.json()
        #print len(result), result, response.status_code -- gives the information of the customer 
        return  result
    
    def customer_id(self, id):
        uri = self.url_id + str(id)  #-----concating 'ID' with 'url' 
        print uri
        response = ser.get_method(uri)
        result = response.json()
        return result
    
    def customer_create(self, name, workflowid, address, viewId, onboarded, status):
        
        body = {
            'id': 4,
            'name': name,
            'address': address,
            'status':status,
            'viewId': int(viewId),
            'workflowId': int(workflowid),
            'onboarded':onboarded
            }
        
        result = ser.post_method(body)
        #print result.content 
        return "Sucessfully Created the User with Id = " +str(result.content)+" and Status Code = " +str(result.status_code)  
    
    
cus = Customer()
#-- Home Screen -------
cus.home_screen(cus.host)
#--- List out all the customer --------
cus.customer_all(cus.allcustomer)
#--- customer based on given id --------
#cus.customer_id(1)
#--- creating New customer --------
cus.customer_create(cus.name, cus.workflowid, cus.address,cus.viewId, cus.onboarded, cus.status) # -- will sucessfully create the user '4' 
#------ verify the created user with id 4 
cus.customer_id(id = 4)

