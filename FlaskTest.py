from flask import Flask, jsonify,request
app = Flask(__name__)

@app.route('/')
def hello_world():     # http://127.0.0.1:5000/
    return 'Hello World!123'

@app.route('/user/<username>')
def show_user_profile(username):  # http://127.0.0.1:5000/user/RickyS
    # show the user profile for that user
    return 'User %s' % username
@app.route('/hello')
def hello():         # http://127.0.0.1:5000/hello
    return 'Hello Python'
#########################################################################
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])  # http://127.0.0.1:5000/todo/api/v1.0/tasks
def get_tasks():
    return jsonify({'tasks': tasks})

###############################POST##########################################
    
@app.route('/register', methods=['POST'])   # http://127.0.0.1:5000/register
def register():
    print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    
    password_num= request.form['password']
    print(password_num)
    print(type(password_num))
    
    password_num1 = int(password_num)+20
    
    return str(password_num1 )



def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])  # http://127.0.0.1:5000/shutdown
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run()
    
# Crtl+C to stop 
    
    
    