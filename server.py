from flask import Flask, jsonify, request, render_template, redirect #Flask: class, jsonify: function, request: object, render_template: function
import json

app = Flask(__name__) #Flask initialization, name: name of the module or package of the application
@app.route('/') #Decorator: wraps a function, route: URL rule as string, 
#Function: function to be executed when URL is called, need to be unique and must be there for every route
def index(): #Making a function
    return 'Hello World!'

@app.route('/about') #Static route: URL without variable parts
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

@app.route('/users') # JSON: json file imported and then jsonify() it
def users():
    print(request.cookies) #request: object, cookie: attribute
    with open('users.json') as file: #with: context manager, automatically closes the file once the indent is finished
        users = json.load(file) #json.load(): loads the json file
    return jsonify(users) #jsonify(): converts the json object to a response object with application/json mimetype

# OTHER METHOD
@app.route('/users2/')
def users2():
    file = open('users.json') #open(): opens the file
    users = json.load(file) #json.load(): loads the json file
    file.close() #close(): closes the file
    return jsonify(users)

# RETURNING USERS FROM ID
@app.route('/user/<int:id>') #Dynamic route: URL with variable parts
def user(id): #Making a function and passing id as parameter
    with open('users.json') as file:
        users = json.load(file)
    for user in users['users']: #users['users']: list of users
        if user['id'] == id: #user['id']: id of the user
            return jsonify(user) #if matches return the user
    return jsonify({}) #if not matches return empty json object



#Methods: GET: to get data, POST: to submit data, PUT: to update data, DELETE: to delete data, HEAD, OPTIONS
# POST request can be sent from javascript or HTML form or from a python script or from a REST client(postman)
# By default it is get request
@app.route('/method', methods=['GET', 'POST']) 
def method():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'

#RETURNING HTML
#---By writing it on own
@app.route('/page1')
def page1():
    return "<h1>HTML</h1>"

@app.route('/page2')
def page2():
    return "<script>alert('Hello')</script>"

@app.route('/page3')
def page3():
    return """
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <h1>HTML</h1>   
            <p>Paragraph</p>
        </body>
    </html>
    """

#---By using templates
@app.route('/page4')
def page4():
    return render_template('page4.html')

#---By using templates and passing variables
@app.route('/page/<id>')
def page(id):
    with open('users.json') as file:
        users = json.load(file)
    for user in users['users']:
        if user['id'] == int(id):
            return render_template('page.html', user=user)
    return render_template('page.html', user={})


#---By using templates and passing variables: Form post method
@app.route('/saveuser', methods=['POST', 'GET'])
def saveuser():
    if request.method == 'GET':
        user = request.args.get('user') #request.args.get(): gets the value of the key
        #Example: http://127.0.0.1:5000/saveuser?user=himanshu, will create a new user with name himanshu
    elif request.method == 'POST':
        user = request.form['user'] #request.form['user']: gets the value of the key
    file = open('users.json')
    users = json.load(file)
    id = len(users['users']) + 1
    users["users"].append({"id": id, "name": user})
    file.close()
    file = open('users.json', 'w') #w: write mode
    json.dump(users, file, indent=4) #json.dump(): writes the json file, users: json object, file: file object, indent: indentation and will save the file with indentation
    file.close()
    return redirect(f'/page/{id}') #redirect(): redirects to the given URL, f: string formatting














if __name__ == '__main__':
    app.run(debug=True) #Debug mode: server will reload itself on code changes, and provide a debugger
