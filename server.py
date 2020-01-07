from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def roll_dice():
    rolls= np.random.randint(1,6,3)
    output = f'You rolled {rolls[0]}, {rolls[1]}, and {rolls[2]}'
    return output


if __name__ == '__main__':
    print(roll_dice())