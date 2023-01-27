from flask import Flask, request, make_response, redirect, render_template
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    user_ip = request.cookies.get('user_ip')
    return render_template('hello.html', user_ip=user_ip)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


if __name__ == '__main__':
    app.run()
