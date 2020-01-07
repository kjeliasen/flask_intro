from flask import Flask
from flask import render_template
from random import randint

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


if __name__ == '__main__':
    print(roll_dice())