from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')




@app.route('/', methods=['POST'])
def validate_entry(): 
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email= request.form['email']


    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) == 0 or len(username) < 3 or len(username) >20 or " " in username:
        username_error = 'Not a valid username'

        

    else:
        username = username

    if len(password) == 0 or len(password) < 3 or len(password) >20 or " " in password:
       password_error= "Not a valid password"


    else:
        password = password

    
    if len(verify) == 0:
        verify_error = "Invalid password"

    if verify != password:

        verify_error = 'Passwords dont match'
        verify = " "
        password =" "
    else:
        verify = verify

    if email == "":
        email = email

    else:

        if '@' not in email or '.' not in email  or " " in email  or len(email)>20 or len(email) < 3 :
            email_error = 'Not valid email'

            email = email

        

    
    if not username_error and not password_error and not verify_error and not email_error:

        return render_template('welcome.html', username = username)   

    else:
        return render_template('forms.html', 
            username_error = username_error, 
            password_error = password_error,
            verify_error = verify_error,
            email_error = email_error,
            username = username,
            email = email)



app.run()