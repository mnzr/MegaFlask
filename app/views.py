# Views are where the routes are defined
import pprint
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


# Root for the test site
@app.route('/')
@app.route('/index')
def index():
    # Returns whatever is returned by the return for index()
    # need to create db connection here
    # return "Hello, World!"

    users = {  # face user
               'nickname': 'Minhaz',
               'fullname': 'Ratul Minhaz',
               'email': 'm@ratul.xyz'
               }

    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Mahmud'},
            'body': 'Je mange riz!'
        }
    ]

    pprint.pprint(users, indent=4, depth=1)

    return render_template('index.html',
                           title='Home',
                           users=users,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # after the submit button is pressed, if anything wrong the last return
    # will work.
    if form.validate_on_submit():
        # show a message on next page
        
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
