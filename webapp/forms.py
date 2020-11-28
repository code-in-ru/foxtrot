from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class AddOrderForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    task_type = SelectField("Тип задачи", choices=['Техническое', 'Технологическое', 'Организационное'], validators=[DataRequired()])
    due_date = StringField('Срок выполнения', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[DataRequired()])
    priority = SelectField('Приоритет', choices=['Зелёный', 'Жёлтый', 'Красный'])
    location = StringField('Место исполнения задания', validators=[DataRequired()])
    submit = SubmitField('Добавить')