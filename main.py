from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import Email, InputRequired
from flask_bootstrap import Bootstrap5
import smtplib
import os
from dotenv import load_dotenv

load_dotenv('password.env')

# Define the form class with email validation
class MyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email',
                       validators=[InputRequired(), Email(message="Invalid email address.")])  # Email validation
    number = StringField('Number', validators=[InputRequired()])
    message = StringField('Message', validators=[InputRequired()])


app = Flask(__name__)

my_gmail = os.getenv('my_gmail')

password = os.getenv('password')

Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


@app.route('/', methods=['GET', 'POST'])
def home():
    contact_form = MyForm()

    if request.method == 'POST' and contact_form.validate_on_submit():
        # If the form is valid, send the email
        try:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()  # Secure the connection
                connection.login(user=my_gmail, password=password)

                # Accessing form data to send the email
                msg = f'Subject: Job Opportunity\n\nDear William,\n\n' \
                      f'My name is {contact_form.name.data}.\n' \
                      f'My email address is {contact_form.email.data}.\n' \
                      f'I would like to discuss a job opportunity with you regarding: {contact_form.message.data}\n' \
                      f'Contact number: {contact_form.number.data}'

                # Send the email
                connection.sendmail(from_addr=my_gmail,
                                    to_addrs='william_ajiboye@yahoo.com',
                                    msg=msg)

            # Redirect after successfully sending email
            return redirect(url_for('home'))  # You can change the URL to a thank you page if needed.

        except Exception as e:
            # Handle email sending error (optional)
            return f"An error occurred while sending the email: {str(e)}"

    # If the form is not valid, it will re-render the form
    return render_template('home.html', form=contact_form)


if __name__ == '__main__':
    app.run(debug=True)
