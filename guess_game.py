from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)
jackpot = random.randint(1, 100)
counter = 0
@app.route('/', methods=['GET', 'POST'])
def guess_game():
    global counter, jackpot

    if request.method == 'POST':
        try:
            number = int(request.form['number'])
        except ValueError:
            return render_template('index.html', message="Please enter a valid number", attempts=counter)
        
        counter += 1

        if number < jackpot:
            return render_template('index.html', message="Wrong Guess! Please Guess Higher", attempts=counter)
        elif number > jackpot:
            return render_template('index.html', message="Wrong Guess! Please Guess Lower", attempts=counter)
        else:
            result_message = f"Correct Guess! Your attempts: {counter}"
            jackpot = random.randint(1, 100)
            counter = 0
            return render_template('index.html', message=result_message, attempts=0)

    return render_template('index.html', message="", attempts=counter)

if __name__ == '__main__':
    app.run(debug=True)
