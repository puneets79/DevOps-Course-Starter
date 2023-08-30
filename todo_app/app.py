
from flask import Flask,render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data import session_items,trello_items
import operator

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=trello_items.get_items(), route='display')

@app.route('/add', methods=['GET','POST'])
def addtodo():
    if (request.method == 'GET'):
        return render_template('index.html',route='add',statuses=trello_items.get_lists())
    else:
        item = {}
        item['name'] = request.form.get('taskname')
        item['idList'] = request.form.get('status')
        trello_items.add_item(item)
        return redirect('/')
    
@app.route('/update', methods=['GET','POST'])
def updatetodo():
    if (request.method == 'GET'):
        id = request.values.get("id","")
        item = trello_items.get_item(id)
        statusList = trello_items.get_lists()
        return render_template('index.html',route='update', item = item, statuses = statusList)
    else:
        id = request.form.get('id')
        taskname = request.form.get('taskname')
        status = request.form.get('status')
        item = {'id':id, 'name':taskname, 'status':status}
        print (item)
        trello_items.save_item(item)
        return redirect('/')
    
@app.route('/delete')
def deletetodo():
    id = request.values.get("id","")
    trello_items.delete_item(id)
    return redirect('/')

    