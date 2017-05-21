import flask
import datetime
import requests
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
    time = []
    name = []
    service = []
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc("schedForToday")
    data = cursor.fetchall()
    return render_template('index.html', data = data)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/messageAlert')
def messageAlert():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('getToday')
    name = []
    cn = []
    startTime = []
    data = cursor.fetchall()
    user = 'TeraxxQ'
    passw = 'Renzo123'
    service = []
    for row in data:
        serve = str(row[4])
        served = serve.replace(" ","%20")
        time = str(row[1])
        trueTime = time.replace(" ","%20")
        name.append(row[2])
        cn.append(row[3])
        startTime.append(trueTime)
        service.append(served)
    i=0
    while i < len(name):
        msg = 'Good%20Day!%20This%20is%20Dental%20Care%20Plus.%20You%20have%20an%20appointment%20today%20at%20our%20clinic%20at%20' + startTime[i] + '%20for%20' + service[i] + '.%20Thank%20You.'
        url = 'http://www.isms.com.my/isms_send.php?un=%s&pwd=%s&dstno=%d&msg=%s&type=1&sendid=DentalCarePlus'%(user,passw,cn[i],msg)
        print(url)
        r = requests.get(url)
        print(r.text)
        i += 1
    return ('', 204)

@app.route('/addProcess' , methods = ['POST'])
def addProcess():
    Fname = request.form['FName']
    Minit = request.form['Minit']
    Lname = request.form['LName']
    Age = request.form['Age']
    Cn = request.form['ContactNumber']
    Address = request.form['Address']
    if Fname and Minit and Lname and Age and Cn and Address:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('insertPersonalInfo',(Fname,Minit,Lname,Age,Cn,Address))
        return redirect('/add')
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

    cursor.close()
    conn.close()

@app.route('/updateProcess', methods = ['POST'])
def updateProcess():
    Fname = request.form['FName']
    Minit = request.form['Minit']
    Lname = request.form['LName']
    Age = request.form['Age']
    Cn = request.form['ContactNumber']
    Address = request.form['Address']
    id = request.form['id']
    if Fname and Minit and Lname and Age and Cn and Address:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('updatePersonalInfo',(Fname,Minit,Lname,Age,Cn,Address,id))
        conn.commit()
    return ('', 204)
    cursor.close()
    conn.close()

@app.route('/deleteProcess', methods = ['POST'])
def deleteProcess():
    id = request.form['id']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('deletePatient',(id,))
    conn.commit()
    return redirect('/home')


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
        return redirect('/home')
    else:
        return json.dumps({'html': '<span>Incorrect Email or Password.</span>'})

@app.route('/addAppt', methods = ['POST'])
def addAppt():
    date = request.form['Date']
    startTime = request.form['startTime']
    startTime = datetime.datetime.strptime(startTime,'%H:%M')
    print(startTime)
    one = datetime.datetime.strptime('1:00','%H:%M')
    five = datetime.datetime.strptime('5:00','%H:%M')
    if startTime >= one and startTime <= five:
        startTime = ("%s:%s"%(startTime.hour,startTime.minute))
        startTime = ("""%s%s""" % (startTime, " PM"))
        print(startTime)
        startTime = datetime.datetime.strptime(startTime, '%I:%M %p')
        startTime = startTime.strftime("%H:%M %p")
    endTime = request.form['endTime']
    endTime = datetime.datetime.strptime(endTime, '%H:%M')
    if endTime >= one and endTime <= five:
        endTime = ("%s:%s" % (endTime.hour, endTime.minute))
        endTime = ("""%s%s""" % (endTime, " PM"))
        endTime = datetime.datetime.strptime(endTime, '%I:%M %p')
        endTime = endTime.strftime("%H:%M %p")
    service = request.form['service']
    name = request.form['Fullname']
    if date and startTime and endTime and service and name:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('setAppointment',(startTime,endTime,name,service,date))
        conn.commit()
    return redirect('/home')


@app.route('/customers/<name>' , methods = ['GET','POST'])
def customerPage(name):
    fullName = str(name)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('searchPatient', (name,))
    data = cursor.fetchone();
    id = data[4]
    address = str(data[1])
    age = data[2]
    contNum = int(data[3])
    cursor.callproc('appointmentsByPatID', (name,))
    data = cursor.fetchall()
    return render_template('customerPage.html', Name = fullName, Age = age, ContactNumber = contNum, address = address, ID = id, data = data)

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

@app.route('/updateAppt', methods = ['POST'])
def updateAppt():
    id = request.form['id']
    date = request.form['Date']
    startTime = request.form['startTime']
    startTime = datetime.datetime.strptime(startTime, '%H:%M')
    print(startTime)
    one = datetime.datetime.strptime('1:00', '%H:%M')
    five = datetime.datetime.strptime('5:00', '%H:%M')
    if startTime >= one and startTime <= five:
        startTime = ("%s:%s" % (startTime.hour, startTime.minute))
        startTime = ("""%s%s""" % (startTime, " PM"))
        print(startTime)
        startTime = datetime.datetime.strptime(startTime, '%I:%M %p')
        startTime = startTime.strftime("%H:%M %p")
    endTime = request.form['endTime']
    endTime = datetime.datetime.strptime(endTime, '%H:%M')
    if endTime >= one and endTime <= five:
        endTime = ("%s:%s" % (endTime.hour, endTime.minute))
        endTime = ("""%s%s""" % (endTime, " PM"))
        endTime = datetime.datetime.strptime(endTime, '%I:%M %p')
        endTime = endTime.strftime("%H:%M %p")
    service = request.form['service']
    if date and startTime and endTime and service and id:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('updateAppoint', (startTime, endTime, date, service, id))
        conn.commit()
    return redirect('/home')

@app.route('/cancelAppt', methods = ['POST'])
def cancelAppt():
    conn = mysql.connect()
    cursor = conn.cursor()
    id = request.form['id']
    cursor.callproc('cancelAppointment',(id,))
    return redirect('/home')

@app.route('/tableRenderer', methods = ['POST'])
def tableRenderer():
    date = request.form['date']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('appointByDate',(date,))
    data = cursor.fetchall()
    return render_template('calendarTemp.html',data = data)

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
