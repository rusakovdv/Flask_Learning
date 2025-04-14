import datetime
import os
import random
import re

from flask import Flask

app = Flask(__name__)

cars_list = ["Chevrolet", "Renault", "Ford", "Lada"]
cats_breeds = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

counter_visits = 0


def load_words():
    with open(BOOK_FILE, 'r', encoding='utf-8') as file:
        text = file.read()
    words = re.findall(r'\b[а-яА-ЯёЁ]+\b', text)
    return words


war_and_peace_words = load_words()


@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"


@app.route('/cars')
def cars():
    return "".join(cars_list)


@app.route('/cats')
def cats():
    return random.choice(cats_breeds)


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"Точное время: {current_time}"


@app.route('/get_time/future')
def get_time_future():
    time_in_hour = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%H:%M:%S")
    return f"Точное время через час будет {time_in_hour}"


@app.route('/get_random_word')
def get_random_word():
    return random.choice(war_and_peace_words)


@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return str(counter_visits)


if __name__ == '__main__':
    app.run(debug=True)
