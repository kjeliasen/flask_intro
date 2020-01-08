from flask import Flask, render_template, request
from random import randint
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice/')
def roll_dice():
    rolls = [randint(1,6) for _ in range(int(3))]
    output = f'You rolled {rolls[0]}, {rolls[1]}, and {rolls[2]}'
    return output

@app.route('/roll-dice/<int:ndice>')
def roll_ndice(ndice):

    rolls = [str(randint(1,6)) for _ in range(int(ndice))]

    ### return through template
    return render_template(
        'roll-dice.html',
        rolls=rolls,
        dice=ndice
    )

    ### original return
    rollstr = ', '.join(rolls)
    output = f'You rolled: {rollstr}'
    return output


###### Zach's Code ######
######
######
@app.route('/i-can-html')
def htmlpage():
    rolls = [randint(1, 6) for _ in range(10)]
    return render_template(
        'my-html-page.html',
        rolls=rolls
    )
######
######
###### Zach's Code ######


@app.route('/hello/<name>')
def say_hello(name):
    output = f'Hello, {name}!'
    return output


@app.route('/greeting')
def show_greeting_form():
    ### return through template
    return render_template(
        'greeting.html'
    )


@app.route('/greeting-result', methods=['POST'])
def show_greeting_result():
    first_name = request.form['first_name']
    return render_template(
        'greeting-result.html',
        first_name=first_name
    )


@app.route("/predict-spam")
def show_spam_form():
    return render_template("predict-spam.html")


@app.route("/predict-spam-result", methods=["POST"])
def show_spam_result():
    message = request.form["message"]
    return render_template(
        "predict-spam-result.html", message=message, prediction=predict(message)
    )


if __name__ == '__main__':
    print(roll_dice())