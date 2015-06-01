from server import app
from flask import render_template, request, redirect
import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/g2.db'
db = SQLAlchemy(app)
# from flask_bootstrap import Bootstrap

@app.route('/g2')
def g2_this_is_a_test(): 
    return "test"


@app.route('/g2/books')
def book_list():
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT * FROM book;')
    book_list_data = []
    for row in cursor.fetchall():
        book_list_data.append(row)
    return render_template('g2_template.html', book_list_data = book_list_data)


@app.route('/g2/books/<book_id>')
def book_id(book_id):
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT author_id, title ,isbn FROM book WHERE id = {}'.format(book_id))
    auth_id, title, isbn = cursor.fetchone()
    return render_template('g2_bookid.html', auth_id=auth_id, title = title, isbn = isbn)

    
@app.route('/g2/library')
def library(): 
    all_entries = {}
    # note: Tried using ORDER BY to order by author name but dicts are unordered by design. 
    db = sqlite3.connect('example.db')
    get_rows = """SELECT b.title,a.name, b.isbn 
                FROM book as b
                LEFT OUTER JOIN author as a
                ON b.author_id=a.id"""
    rows = db.execute(get_rows)
    for row in rows.fetchall():
        book_title = row[0]
        author_name = row[1]
        isbn = row[2]
        if author_name in all_entries:
            all_entries[author_name].append([book_title,isbn])
        else:
            all_entries[author_name] = [[book_title,isbn]]
    return render_template("library.html", entries=all_entries)


@app.route('/g2/add_book', methods=['POST','GET']) # add a book
def add_book():

    if request.method == 'GET':
        db = sqlite3.connect('example.db')
        get_authors = db.execute("""SELECT name FROM author""")
        authors = [author for author in get_authors.fetchall()]
        return render_template('newbook.html', authors=authors)
        
    elif request.method == 'POST':
        title = request.form['book_title']
        isbn = request.form['isbn_value']
        auth_name = request.form['auth_name']
        db = sqlite3.connect('example.db')
        isbn_check = db.execute("SELECT isbn FROM book WHERE isbn=?", [isbn])
        isbn_found = len([str(i) for i in isbn_check.fetchall()])
        if isbn_found > 0:
            exists_page = """
                <html>
                    <p> That book already exists in the library <p>
                    <form action="https://002-pyp-g1-martinzugnoni.c9.io/g2/add_book" method="get">
                        <input type="submit" value="Add another book" name="Submit"/>
                    </form>
                </html>
            """
            return exists_page
        else:
            find_auth_id = db.execute("SELECT book.author_id, author.name FROM author join book ON book.author_id=author.id")
            add_id = find_auth_id.fetchall()
            auth_id = "There was an error contact Charlie"
            for author_info in add_id:
                if auth_name[3:] in str(author_info[1]):
                    auth_id = int(author_info[0])
            db.execute("INSERT INTO book (author_id, title, isbn) VALUES(?,?,?)", (auth_id, title, isbn))
            db.commit()
            db.close()
            return redirect('/g2/library')
            


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(80), unique=True)

    def __init__(self, country_name):
        self.country_name = country_name

    def __repr__(self):
        return '<Country {}>'.format(self.country_name)
        

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('Country.id'))
    country = db.relationship('Country', backref=db.backref('authors', lazy='dynamic'))
    
    def __init__(self, author_name):
        self.author_name = author_name
    
    def __repr__(self):
        return '<Author: {}>'.format(self.author_name) 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    isbn = db.Column(db.String(80), unique=True)
    author_ID = db.Column(db.Integer, db.ForeignKey('Author.id'))
    author = db.relationship('Author',backref=db.backref('books', lazy='dynamic'))

    def __init__(self, title, author_id, isbn):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn

    def __repr__(self):
        return '<Book: {}, Author: {}, ISBN: {}>'.format(self.title, self.author.name, self.isbn)