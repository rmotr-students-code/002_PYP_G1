from server import app
from flask import render_template, request, redirect
import sqlite3
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
        return render_template('newbook.html')
    elif request.method == 'POST':
        title = request.form['book_title']
        isbn = request.form['isbn_value']
        auth_id = request.form['author_id']
        db = sqlite3.connect('example.db')
        isbn_check = db.execute("SELECT isbn FROM book WHERE isbn=?", [isbn])
        isbn_found = len([str(i) for i in isbn_check.fetchall()])
        # After playing around with it, the result set returns a set of unicode tuples. 
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
            db.execute("INSERT INTO book (author_id, title, isbn) VALUES(?,?,?)", (auth_id, title, isbn))
            book_info = {'title':title, 'isbn':isbn, 'auth_id': auth_id}
            db.commit()
            db.close()
            return redirect('/g2/library')