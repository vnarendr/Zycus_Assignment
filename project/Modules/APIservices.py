'''
Created on Jul 27, 2018

@author: narendra_v
'''

import requests


class APIservices():
    
    
    def get_method(self,url):
        
        response = requests.get(url)     #print " Content = ", response.content
        return response
    
    def post_method(self, body):
        
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
        
        post_url = 'http://localhost:5000/api/v1/resources/customers/'
        response = requests.post(post_url, body, headers)
        return response
   
ser = APIservices()
