from flask import Flask,render_template,request,redirect,url_for,session
import ibm_db
import re
app=Flask(__name__)
app.secret_key='a'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;PROTOCOL=TCPIP;UID=MKNNkE7PzFz6U9yg;PWD=trd81711",'','')

@app.route('/insert')
def home():

    msg=""

    if request.method=="POST":
        username=request.form['email']
        password=request.form['pass']
        sql="SELECT * FROM Login Details where username='USERNAME' AND password='PASSWORD'
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg="Account already exists"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            msg="Invalid email address"

        elif not re.match(r'[A-Za-z0-9]+',username):
            msg="name must contain only characters and numbers"
        else:
            insert_sql="INSERT INTO Login Details VALUES(username,password)"
            prep_stmt-ibm_db.prepare(conn,insert_sql)
            ibm_db.bind_param(stmt,1,username)
            ibm_db.bind_param(stmt,2,password)
            ibm_db.execute(prep_stmt)
            msg='You have logged in '
        elif request.method=='POST":
            msg="Please Fill the required data field'
            return render_template('login2.html',msg=msg)
            
        
    return render_template('login2.html')



@app.route("/login",methods=['GET',"POST"])
def login():
    global userid
    msg=""

    if request.method=="POST":
        username=request.form['email']
        password=request.form['pass']
        sql="SELECT * FROM Login Details where username="USERNAME" AND password="PASSWORD"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['Loggedin']=True
            session['id']=account['USERNAME']
            userid=account["USERNAME"]
            session['username']=account["USERNAME"]
            msg='Login Successfull!'
            return render_template('login1.html',msg=msg)
        else
            msg="Invalid credentials"


    return render_template('login1.html',msg=msg)
