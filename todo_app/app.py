
from flask import Flask,render_template, request, redirect, url_for
from todo_app.flask_config import Config
from todo_app.data import session_items
import operator

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=sorted(session_items.get_items(),key = operator.itemgetter('status')), route='display')

@app.route('/add', methods=['GET','POST'])
def addtodo():
    if (request.method == 'GET'):
        return render_template('index.html',route='add')
    else:
        taskname = request.form.get('taskname')
        session_items.add_item(taskname)
        return redirect('/')
    
@app.route('/update', methods=['GET','POST'])
def updatetodo():
    if (request.method == 'GET'):
        id = request.values.get("id","")
        item = session_items.get_item(id)
        return render_template('index.html',route='update', item = item)
    else:
        id = int(request.form.get('id'))
        taskname = request.form.get('taskname')
        status = request.form.get('status')
        item = {'id':id, 'title':taskname, 'status':status}
        print (item)
        session_items.save_item(item)
        return redirect('/')
    
@app.route('/delete')
def deletetodo():
    id = int(request.values.get("id",""))
    session_items.delete_item(id)
    return redirect('/')

    