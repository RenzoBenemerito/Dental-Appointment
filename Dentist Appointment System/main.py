import flask
import pymysql
from flask import Flask, render_template, request, redirect, session, url_for, json, jsonify
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)
app.secret_key = 'abc'

app.config['MYSQL_DATABASE_USER'] = 'Renzo'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Renzo123'
app.config['MYSQL_DATABASE_DB'] = 'mydentap'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addProcess' , methods = ['POST'])
def addProcess():
    Fname = request.form['FName']
    Minit = request.form['Minit']
    Lname = request.form['LName']
    Age = request.form['Age']
    Cn = request.form['ContactNumber']
    Address = request.form['Address']
    print(Fname,Minit,Lname,Age,Cn,Address)
    if Fname and Minit and Lname and Age and Cn and Address:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('insertPersonalInfo',(Fname,Minit,Lname,Age,Cn,Address))
        return redirect('/'+Fname)
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

    cursor.close()
    conn.close()


@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/')
def signIn():
    return render_template('signin.html')

@app.route('/login' , methods = ['POST'])
def logIn():
    email = request.form['email']
    password = request.form['pass']
    if email == 'renzo@gmail.com' and password == '123':
        session['email'] = email
        return render_template('index.html')
    else:
        return json.dumps({'html': '<span>Incorrect Email or Password.</span>'})

@app.route('/<name>' , methods = ['GET','POST'])
def customerPage(name):
    fullName = request.args.get('name')
    print(name)
    #render_template('customerPage.html', fullName = fullName, Age = 19, ContactNumber = 90)
    return 

@app.route('/_search' , methods = ['GET' , 'POST'])
def search():
    conn = mysql.connect()
    cursor = conn.cursor()
    searchItem = request.form.get('search')
    cursor.callproc('searchPatient' , (searchItem,))
    data = cursor.fetchall()
    names = []
    address = []
    for name in data:
        names.append(name[0])
        address.append(name[1])
    return jsonify({'names' : names, 'addresses' : address})

@app.route('/logout')
def logout():
    session.pop('email',None)
    conn = mysql.connect()
    cursor = conn.cursor()
    conn.close()
    cursor.close()
    return redirect(url_for('signIn'))

if __name__ == '__main__':
    app.run(debug=True)
