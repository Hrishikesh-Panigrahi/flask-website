from datetime import datetime
from email.policy import default
from turtle import title
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class rishi(db.Model):
    No = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(255), nullable = False)
    desc = db.Column(db.String(2555), nullable = False)
    date = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.No} {self.title}"


@app.route("/")
def hello_world():
    new_user = rishi(title= "first", desc = "start")
    db.session.add(new_user)
    db.session.commit()
    all_list = rishi.query.all()
    return render_template('index.html', all_list= all_list)


@app.route("/list")
def new():
    #all_list = rishi.query.all()
    #print(all_list)
    return "Hello, new!"
    
if __name__ == "__main__":
    app.run(debug=True)