import flask
from flask import request, jsonify 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Create some test data for our catalog in the form of a list of dictionaries.
customers = [
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

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Customer on Boarding </h1>
<p>A prototype API for customers view .</p>
   ''' 
# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/customers/all', methods=['GET'])
def api_all():
    #status_code = 200
    return jsonify(customers)
    '''({
             'Json' : customers,
             
             'Status' : 'OK',
             'code': 200  
             }) 
    '''
@app.route('/api/v1/resources/customers', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return jsonify({
                'Status' : 'Not Found',
                'code' : 404}) 

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

@app.route('/api/v1/resources/customers/',methods = ['POST', 'GET'])
def api_create():
    #return  '''<h1>Creating user screen </h1>'''
    if request.method == 'POST':
        
        #r = request.args.get('name', '')
        #print r 
        result = request.form['id']
        result = {
                    'id':int(request.form['id']),
                    'name': request.form['name'],
                    'address': request.form['address'],
                    'status':request.form['status'],
                    'viewId': int(request.form['viewId']),
                    'workflowId': int(request.form['workflowId']),
                    'onboarded': request.form['onboarded']
                 }
        print result 
        id =request.form['id']
        #print type(result), result
        #res = result.encode("ascii","replace")
        #print type(result), result 
                
        #results.append(result)  
        #self.resource.append(name.encode("utf-8"))
        jsonify(customers.append(result))
        #print request.form['id']
        return(id)
        #return render_template("result.html",result = result)

app.run()
