"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""

from flask import Flask
from flask_wtf import FlaskForm
import wtforms
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, NumberRange
from hw2_validators import number_length, NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email: StringField = StringField(validators=[wtforms.validators.Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(10, 10), NumberLength(10, 10)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired(), NumberRange(100000, 999999)])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form: RegistrationForm = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
