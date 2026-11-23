from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import TextArea

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route("/")
def home():
    return render_template('index.html')


# Login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # print(login_form.email.data, login_form.password.data)
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)



class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    phone = StringField(label='Phone', validators=[DataRequired()])
    message = TextAreaField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print(f"Name: {contact_form.name.data}, Email: {contact_form.email.data}, Phone: {contact_form.phone.data}, Message: {contact_form.message.data}")
        return render_template("success.html")
    else:
        return render_template("denied.html")

    return render_template("contact.html", form=contact_form)



if __name__ == '__main__':
    app.run(debug=True)
