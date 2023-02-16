from flask import Flask, request, make_response, redirect, render_template, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar solicitud de compra']



class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Sign In', render_kw={"class": "btn btn-primary"})


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error), 500


@app.route('/hello')
def hello_world():
    login_form = LoginForm()
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': session.get('username')
    }
    return render_template('hello.html', **context)


@app.route('/login', methods=['POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session['username'] = login_form.username.data
        return redirect(url_for('index'))
    return redirect('/hello')


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response


if __name__ == '__main__':
    app.run()
