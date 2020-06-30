from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testemailblah123@gmail.com'
app.config['MAIL_PASSWORD'] = 'Testemail123!'
app.config['MAIL_DEFAULT_SENDER'] ='testemailblah123@gmail.com'
app.config['MAIL_USE_SSL'] = True
mail= Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        msg = Message(request.form.get("name"), recipients=['csarjaramillo89@yahoo.com'])
        msg.body = 'Name: ' + name + '\n Email: ' + email + '\n Message: ' + message
        mail.send(msg)
        return render_template('result.html', result="Success!")
    else:
        return render_template('result.html', result="Failure!")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
