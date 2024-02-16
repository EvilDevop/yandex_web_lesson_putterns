from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    astronaut_id = StringField('Id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def form_page():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('form_pattern.html', title='Авторизация', form=form)


@app.route('/success')
def success_page():
    return render_template('success_pattern.html', title='Успех')


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')