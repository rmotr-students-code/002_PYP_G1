from flask import (
    Flask, request, session, g, redirect, url_for,
    abort, render_template, render_template_string, flash
)
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask('This is my first app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/rmotr.db'
db = SQLAlchemy(app)
 
 
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
 
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', backref=db.backref('authors', lazy='dynamic'))
 
    def __init__(self, name, country):
        self.name = name
        self.country = country
 
    def __repr__(self):
        return '<Author %r>' % self.name
 
 
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
 
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return '<Country %r>' % self.name
 
 
@app.route('/rmotr')
def testing():
    pass
    
 
if __name__ == "__main__":
    
    # import all views
    from alan_martinV2 import *
    from charlie_mike_paulo import *
    from scratch import *
    from brencharmik import *
    app.debug = True
    app.run(host='0.0.0.0', port=8080)