from flask import Flask, abort

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    parts = numbers.split('/')
    max_num = None

    for part in parts:
        try:
            num = int(part)
            if max_num is None or num > max_num:
                max_num = num
        except ValueError:
            abort(400, description="All parts must be numbers")

    if max_num is None:
        abort(400, description="No numbers provided")

    return f"Максимальное число: <i>{max_num}</i>"


if __name__ == '__main__':
    app.run(debug=True)