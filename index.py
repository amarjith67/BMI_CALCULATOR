
from email import message
from flask import Flask,render_template,request, url_for
from db_operations import bmi_db
import cx_Oracle

app=Flask(__name__)
db=bmi_db('amar','amar')

@app.route("/")
def landing():
    return render_template("index.html");

@app.route("/home")
def home():
    return render_template("index.html");


@app.route("/send", methods = ['GET', 'POST'])
def send():
    if(request.method=='POST'):
        user_id = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')
        data,message=db.insert_data(user_id,name,age,height,weight)      
    return render_template('insert.html',data=data,message=message)

@app.route("/existing_user")
def existing_user():
    return render_template('existing_user.html')

@app.route("/view_user",methods = ['GET', 'POST'])
def view():
    if(request.method=='POST'):
        user_id = request.form.get('id')
        name = request.form.get('name')
        data=db.view_data(user_id,name)
    return render_template('user_view.html',data=data)

@app.route("/update_user")
def update_user():
    return render_template('update.html')
    
@app.route("/send_update", methods = ['GET', 'POST'])
def send_update():
     if(request.method=='POST'):
        user_id = request.form.get('id')
        name = request.form.get('name')
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')
        db.update_data(user_id,name,age,height,weight)
     return render_template('success.html')    
app.run(debug=True)