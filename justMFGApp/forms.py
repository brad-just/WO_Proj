from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class DepartmentForm(FlaskForm):
   department = SelectField('Select Department', choices = [('custom', 'Custom'), ('bowl', 'Bowl')])
   submit = SubmitField("Go")
