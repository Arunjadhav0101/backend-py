from flask import Flask, request, render_template_string

app = Flask(__name__)

users = {
    'arun' : '1234',
    'jadhav': 'abcd'
}
login_form = '''
     <h2>Login</h2>
    <form method="POST">
        Username: <input type="text" name="username"/><br>
        Password: <input type="password" name="password"/><br>
        <input type="submit" value="Login"/>
    </form>
    <p>{{ message }}</p>
'''
@app.route('/')
def home():
    return '<h2>Welcome! Go to <a href="/login">Login Page</a></h2>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == "POST":
        uname = request.form['username']
        passwd = request.form['password']
        
        if uname in users and users[uname] == passwd:
            message = f"welcome, {uname}! Login successful ...."
        else:
            message = "Invalid username or password ....."

    return render_template_string(login_form, message=message)

if __name__ == '__main__':
    app.run(debug=True)