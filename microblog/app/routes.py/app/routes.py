from flask import render_template, flash, redirect
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Nikhil'}
    posts = [
        {
            'author': ('username': 'John'),
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': ('username': 'Susan'),
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
<html>
    <head>
        <title>Home Page = Microblog</title>
    </head>
    <body>
        <h1>Hello''' + user['username'] + '''!</h1>
    </body>
</html>

@app.route('/login', methods= ['GET','POST'])
def login():
    form = LoginForm()
    if form.validates_on_submit():
        flash('Login requested for user (), remember_me=()' .format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title= 'Sign In', form=form)
