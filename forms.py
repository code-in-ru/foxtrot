from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, SelectField
from wtforms.validators import DataRequired


class AddOrderForm(FlaskForm):
    author = StringField('Автор', validators=[DataRequired()])
    location = StringField('Локация', validators=[DataRequired()])
    title = StringField('Заголовок', validators=[DataRequired()])
    task_type = SelectField("Тип задачи", choices=['Требование', 'Заявка'], validators=[DataRequired()])
    due_date = StringField('Срок выполнения', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('>')
