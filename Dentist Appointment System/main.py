from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/signin')
def signIn():
    return render_template('signin.html')

@app.route('/login' , methods = ['POST'])
def logIn():
    email = request.form['email']
    password = request.form['pass']
    if email == 'renzo@gmail.com' and password == '123':
        return render_template('index.html')
    else:
        logIn()

@app.route('/<name>')
def customerPage(name):
    return render_template('customerPage.html')


if __name__ == '__main__':
    app.run(debug=True)
