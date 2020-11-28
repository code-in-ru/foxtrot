from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddOrderForm(FlaskForm):
    order_name = StringField('Выполняемые работы', validators=[DataRequired()])
    order_type = SelectField("Ordertype", choices=['Требование', 'Заявка'], validators=[DataRequired()])
    submit = SubmitField('Добавить')