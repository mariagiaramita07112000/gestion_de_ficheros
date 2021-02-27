from flask import render_template, flash, redirect, url_for
from movements import app
from movements.forms import LoginForm
from movements import app
import requests
from movements import login


@app.route('/')
@app.route('/index.html')
def index():
    user = {'username': 'nombre'}
    return  render_template('index.html', title='Home', user=user)


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)



