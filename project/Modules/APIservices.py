'''
Created on Jul 27, 2018

@author: narendra_v
'''

import requests
import pdb


class APIservices():
    
    
    def get_method(self,url):
        
        response = requests.get(url)     #print " Content = ", response.content
        return response
    
    def post_method(self, body):
        
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
        
        post_url = 'http://localhost:5000/api/v1/resources/customers/create'
        #self.url_create = 'http://localhost:5000/api/v1/resources/customers/create'
        response = requests.post(post_url, body, headers)
        return response
    
    def put_method(self, body):
        #pdb.set_trace()
        put_url = 'http://localhost:5000/api/v1/resources/customers/update'
        
        response = requests.put(put_url, body)
        #pdb.set_trace()
    
        
        return response
    
    def delete_method(self, id):
        #pdb.set_trace()
        
        url = 'http://localhost:5000/api/v1/resources/customers?id='+str(id)
        response = requests.get(url, '')
        #print response.status_code, url 
        
        if response.status_code == 200:
            result = requests.delete(url)
            #print result.status_code 
            return result 
        else:
            print "Not Found -", response.status_code
        #return response
        
   
ser = APIservices()
