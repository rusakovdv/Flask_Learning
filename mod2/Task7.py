from datetime import datetime
from flask import Flask

app = Flask(__name__)

storage = {}


@app.route('/add/<date>/<int:number>', methods=['POST', 'GET'])
def save_date(date, number):
    date = datetime.fromisoformat(date)
    storage.setdefault(date.year, {}).setdefault(date.month, {}).setdefault(date.day, {})
    storage[date.year][date.month][date.day] = number
    return ''


@app.route('/calculate/<int:year>')
def calculate_year(year):
    if year not in storage:
        storage[year] = {}
    sum = 0
    for k1, v1 in storage[year].items():
        for k2, v2 in v1.items():
            sum += v2

    return f'Сумма за {year} год: {sum} руб.'


months = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь',

}


@app.route('/calculate/<int:year>/<int:month>')
def calculate_year_month(year, month):
    if year not in storage:
        storage[year] = {}
    if month not in storage[year]:
        storage[year][month] = {}
    sum = 0
    for k, v in storage[year][month].items():
        sum += v

    return f'Сумма за {months[month]} месяц {year} года: {sum} руб.'


if __name__ == '__main__':
    app.run(debug=True)
