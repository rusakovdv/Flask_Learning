from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekdays_tuple = (
    "понедельника", "вторника", "среды",
    "четверга", "пятницы", "субботы", "воскресенья"
)


@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    day_name = weekdays_tuple[weekday]
    return f"Привет, {name}. Хорошего {day_name}!"


if __name__ == '__main__':
    app.run(debug=True)