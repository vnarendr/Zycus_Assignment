from flask import Flask 
from flask import request, jsonify , render_template, url_for
import simplejson

app = Flask(__name__) # Creates the Flask application object
# Starts the debugger. Otherwise will see a generic message such as Bad Gateway in the browser when there is a problem with your code.
app.config["DEBUG"] = True 

#html = '''<h3>Customer on Boarding Application  </h3>''' 
# Create some test data for our catalog in the form of a list of dictionaries.
customers = [  {'id': 1,
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

@app.route('/', methods=['GET'])
def home():
    return '''<h2>Customer on Boarding </h2>
<p>A prototype API for customers view .</p>
   ''' 
# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/customers/all', methods=['GET'])
def api_all():
    #status_code = 200
    if(customers == None or customers == 'null' or customers == []):
        #"status code = 200"
        return '''<h3>Customer on Boarding Application  </h3>
        <p> No customers are exit, Please create the user .</p>
       '''
    else: 
        return jsonify(customers)
    
@app.route('/api/v1/resources/customers', methods=['GET'])
def api_id():
    exit_id = []
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    
    if 'id' in request.args:
        id = int(request.args['id'])
        for i in range(len(customers)):
            exit_id.append(customers[i]['id'])
            #exit_id.append(customers[i]['id'])
        #print id , exit_id
        if id not in exit_id: 
            return (" Not - Found", 404)
        else:
            # Create an empty list for our results
            results = []
            for custid in customers:
                if custid['id'] == id:
                    results.append(custid)
        return jsonify(results)
            #return ("status :", 200)
    '''
    # Create an empty list for our results
    results = []
    
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for custid in customers:
        if custid['id'] == id:
            results.append(custid)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
    '''
@app.route('/api/v1/resources/customers/create',methods = ['POST', 'GET'])
def api_create():
    
    exit_id = [] 
    
    if request.method == 'POST':
        result = simplejson.loads(request.form['id'])
        #print type(result), result 

        for i in range(len(customers)):
            #exit_id.append(customers[i]['id'])
            exit_id.append(customers[i]['id'])
        print "final" ,exit_id, result
     
        if result not in exit_id:
            exit_id.append(result)
            stri = simplejson.dumps(exit_id)
            result = {
                    'id':int(request.form['id']),
                    'name': request.form['name'],
                    'address': request.form['address'],
                    'status':request.form['status'],
                    'viewId': int(request.form['viewId']),
                    'workflowId': int(request.form['workflowId']),
                    'onboarded': request.form['onboarded']
                 }
            customers.append(result)
            return ('Status: ' , 201) 
            #return 'Created = ', 201
        else:
            return ("status :", 403)
         
        #return <h3>Customer is Not created </p>

app.run()
