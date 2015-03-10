from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
	"""docstring for LoginForm"""
	name = StringField('name', validators=[DataRequired()])
	email
	password
