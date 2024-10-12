from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,TextAreaField,IntegerField
from wtforms.validators import Length ,Email,EqualTo,ValidationError,DataRequired
from App.models import User
from App import db


class LoginForm(FlaskForm):
    email =StringField(label='Email',validators=[Length(min=4),DataRequired()])
    password = PasswordField('Password',validators=[Length(min=8,max=40),DataRequired()])
    submit = SubmitField('Sign in')

class RegisterForm(FlaskForm):
    username=StringField(label='Username',validators=[Length(max=30,min=8),DataRequired()])
    email = StringField(label='Email',validators=[Email(),Length(max=100),DataRequired()])
    password = PasswordField('Password',validators=[Length(min=8,max=40),DataRequired()])
    submit = SubmitField('Create account')
    
    def validate_username(self,get_username):
        user = User.query.filter_by(username=get_username.data).first()
        if user: 
            raise ValidationError(message='username is already exist')
    
    def validate_email(self,get_email):
        user = User.query.filter_by(email=get_email.data).first()
        if user: 
            raise ValidationError(message='email is already exist')
    
    
class ProductForm(FlaskForm):
    category =SelectField(label="Category",validators=[DataRequired()])
    product_name = StringField(label="Product Label",validators=[DataRequired()])
    desc = TextAreaField(label='description of product',validators=[DataRequired()])
    quantity = IntegerField(label="Quantity",validators=[DataRequired(),Length(min=1)])
    price = IntegerField(label="Price",validators=[DataRequired(),Length(min=1)])
    submit = SubmitField('Add Product')
    
    
            

    

