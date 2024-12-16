from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField
from wtforms.validators import Email,InputRequired
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    email = EmailField('email',validators=[Email()])
    number = StringField('number', validators=[InputRequired()])
    message = StringField('message', validators=[InputRequired()])

app = Flask(__name__)

Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# app.secret_key='hello there'
@app.route('/',methods=['GET','POST'])
def home():
    contact_form = MyForm()
    if request.method=='POST' and contact_form.validate_on_submit():
        return redirect(url_for('#'))
    return render_template('home.html',form=contact_form)

if __name__=='__main__':
    app.run(debug=True)


