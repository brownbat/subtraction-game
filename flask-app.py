from flask import Flask, render_template, request, redirect, url_for
import random
import time

app = Flask(__name__)

num_digits = 1
rounds = []
correct_streak = 0
current_question = None
start_time = None

def generate_question():
    global current_question, start_time
    num1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
    num2 = random.randint(10**(num_digits-1), 10**num_digits - 1)
    if num1 < num2:
        num1, num2 = num2, num1
    current_question = (num1, num2)
    start_time = time.time()

generate_question()

@app.route('/', methods=['GET', 'POST'])
def index():
    global num_digits, correct_streak, start_time
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        if user_answer.isdigit():
            user_answer = int(user_answer)
            correct_answer = current_question[0] - current_question[1]
            elapsed_time = round(time.time() - start_time, 2)
            if user_answer == correct_answer:
                rounds.append({"values": list(current_question), "time": elapsed_time})  # Ensure it's a list
                if elapsed_time < (num_digits + 1) ** 2:
                    correct_streak += 1
                else:
                    correct_streak = 0
                if correct_streak >= 3:
                    num_digits += 1
                    correct_streak = 0
                generate_question()
            else:
                return render_template('index.html', num1=current_question[0], num2=current_question[1], incorrect=True, rounds=rounds)
        return redirect(url_for('index'))
    return render_template('index.html', num1=current_question[0], num2=current_question[1], incorrect=False, rounds=rounds)

if __name__ == '__main__':
    app.run(debug=True)
