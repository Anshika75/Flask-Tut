from flask import Flask, jsonify, request

app = Flask(__name__) #Flask initialization, name: name of the module or package of the application
@app.route('/') #Decorator: wraps a function, route: URL rule as string, 
#Function: function to be executed when URL is called, need to be unique and must be there for every route
def index(): #Making a function
    return 'Hello World!'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/hello/<name>') #Dynamic route: URL with variable parts
def hello(name):
    return 'Hello %s!' % name

@app.route('/post/<int:post_id>') #Converter: <converter:variable_name>
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>') #Converter: <converter:variable_name>
def show_subpath(subpath):
    return 'Subpath %s' % subpath

@app.route('/projects/') #Trailing slash: URL with or without trailing slash
def projects():
    return 'The project page'

@app.route('/getusers') #JSON: jsonify() function, created object and then jsonify() it
def getusers():
    return jsonify({'users': [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Susan'}]})

@app.route('/users', methods=['GET', 'POST']) #Methods: GET: to get data, POST: to submit data, PUT: to update data, DELETE: to delete data, HEAD, OPTIONS
# POST request can be sent from javascript or HTML form or from a python script or from a REST client(postman)
# By default it is get request
def users():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'

if __name__ == '__main__':
    app.run(debug=True) #Debug mode: server will reload itself on code changes, and provide a debugger
