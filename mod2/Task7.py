from flask import Flask

app = Flask(__name__)

finance_storage = {}


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])

    finance_storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    finance_storage[year][month][day] += number

    return f"Expense {number} added for {day}.{month}.{year}"


@app.route('/calculate/<int:year>')
def calculate_year(year):
    total = 0
    if year in finance_storage:
        for month in finance_storage[year]:
            for day in finance_storage[year][month]:
                total += finance_storage[year][month][day]
    return f"Total expenses for {year}: {total}"


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    total = 0
    if year in finance_storage and month in finance_storage[year]:
        for day in finance_storage[year][month]:
            total += finance_storage[year][month][day]
    return f"Total expenses for {month}/{year}: {total}"


if __name__ == '__main__':
    app.run(debug=True)