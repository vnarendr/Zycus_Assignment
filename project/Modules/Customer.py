'''
Created on Jul 27, 2018

@author: narendra_v
'''
import simplejson
import unittest
from APIservices import APIservices
import pdb

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
            # excluded the condition 
            return "Status: 404 -  'Not found'" # pragma: no cover
         
    
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
        result = self.ser.get_method(self.allcustomer)
        
        for id in result.json():
            if id['id'] == body['id']:
                result.status_code = 403
        else:
            result = self.ser.post_method(body)
        if (result.status_code == 403):
            # excluded the condition 
            return "Status: 403 -  'Forbidden/Not Created'"  # pragma: no cover
        else:
            # excluded the condition in code coverage report 
            return "Sucessfully Created the User with Id = "+str(body['id'])+" and Status Code = " +str(result.status_code)     # pragma: no cover
    
    def customer_update(self, *args):
        result = self.ser.get_method(self.allcustomer)
        json = {
                    'id' : int(args[0]),
                    'name' : args[1],
                    'workflowId': args[2],
                    'address': args[3],
                    'viewId': args[4],
                    'onboarded':args[5],
                    'status':args[6],
                }
        #jsonData = 
        #print type(result)
        for index in result.json():
            jsonid = index.get('id', 'unkown')
            if jsonid == args[0]:
                #print "Id exist with Existing detail" ,index
                index.update(json) # merging 2 json Disctionary
                result = self.ser.put_method(index)
                #print result.json() 
                #print result
                break;
        else:
            #print "will create New record" , json 
            result = self.ser.post_method(json)
        
        if (result.status_code == 201):
            # excluded the condition 
            return "New record is inserted for the User with Id = "+str(args[0])+" and Status Code = " +str(result.status_code)
        elif (result.status_code == 202):
            # excluded the condition 
            return "Record Accepted for the Id = "+str(args[0])+" and Status Code = " +str(result.status_code)
        else:
            # excluded the condition in code coverage report 
            return "Sucessfully updated the details for the given UserId = "+str(args[0])+" and Status Code = " +str(result.status_code)     # pragma: no cover
        
    def customer_delete(self, id):
        url = 'http://localhost:5000/api/v1/resources/customers?id='+str(id)
        id_ = self.ser.get_method(url)
        if (id_.status_code  == 404):
            return str(id_.status_code), id_.content     # pragma: no cover
        else:
            result = self.ser.delete_method(id)
            return "record is sucessfully removed for the Id = "+str(id)+" and Status Code = " +str(result.status_code)
       
            
        
            
if __name__ == '__main__':
    #unittest.main() 
    cus = Customer()
#-- Home Screen -------
    cus.home_screen(cus.host)
#--- List out all the customer --------
    cus.customer_all(cus.allcustomer)
#--- customer based on given id --------
    cus.customer_id(1)
#--- creating New customer --------
    cus.customer_create(cus.name, cus.id, cus.workflowid, cus.address,cus.viewId, cus.onboarded, cus.status) # -- will sucessfully create the user '4' 
    #------ verify the created user with id 4 
    #cus.customer_id(id = 4)
    cus.customer_update(cus.id, 'Himesh', cus.workflowid, cus.address, cus.viewId, cus.onboarded, cus.status)
    
    cus.customer_delete(cus.id)
    
    #cus.dict()

