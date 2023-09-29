
from flask import Flask,render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data import trello_items, ViewModel
import operator

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    cards = trello_items.get_items()
    view_model = ViewModel.ViewModel(cards)
    return render_template('index.html', viewmodel=view_model, route='display')

@app.route('/add', methods=['GET','POST'])
def addtodo():
    if (request.method == 'GET'):
        return render_template('add.html',statuses=trello_items.get_lists())
    else:
        item = {}
        item['name'] = request.form.get('taskname')
        item['idList'] = request.form.get('status')
        item['desc'] = request.form.get('taskdesc')
        trello_items.add_item(item)
        return redirect('/')
    
@app.route('/update', methods=['GET','POST'])
def updatetodo():
    if (request.method == 'GET'):
        id = request.values.get("id","")
        item = trello_items.get_item(id)
        statusList = trello_items.get_lists()
        return render_template('update.html', item = item, statuses = statusList)
    else:
        id = request.form.get('id')
        taskname = request.form.get('taskname')
        status = request.form.get('status')
        desc = request.form.get('taskdesc')
        item = {'id':id, 'name':taskname, 'status':status, 'desc':desc}
        print (item)
        trello_items.save_item(item)
        return redirect('/')
    
@app.route('/delete')
def deletetodo():
    id = request.values.get("id","")
    trello_items.delete_item(id)
    return redirect('/')

    