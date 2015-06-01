from server import app
from flask import request, render_template, redirect, flash
import sqlite3

global_links = [{'name':'Books',
              'address':'https://002-pyp-g1-martinzugnoni.c9.io/g1/books'},
              {'name':'Books and Authors',
              'address':'https://002-pyp-g1-martinzugnoni.c9.io/g1/books_authors'},
              {'name':'Add a Book',
              'address':'https://002-pyp-g1-martinzugnoni.c9.io/g1/addbook'},
              {'name':'Add an Author',
              'address':'https://002-pyp-g1-martinzugnoni.c9.io/g1/newauthor'}]

#global author list for easy access across functions
gdb = sqlite3.connect('example.db')
gcursor = gdb.execute('SELECT name FROM author;')

global_authors = [author[0] for author in gcursor.fetchall()]


@app.route('/g1')
def g1_this_is_a_test():
    pagetitle = "The RMOTR Library"
    links = global_links
    authors= global_authors
    return render_template('g1_base.html',
                            pagetitle=pagetitle, 
                            links=links,
                            authors=authors)
    
@app.route('/g1/books')
def g1_booklist():
    db = sqlite3.connect('example.db')
    query="""SELECT author.name, book.title, 
            book.isbn FROM author LEFT OUTER JOIN book
            ON book.author_id = author.id;
            """
    cursor = db.execute(query)
    links = global_links
    authors=global_authors
    book_list = {}  #
    page_title = "Book List"
    for row in cursor.fetchall():
        author, title, isbn = row 
        if author not in book_list:
            book_list[author] = [(title, isbn)]
        else:
            book_list[author].append((title, isbn))
        
    return render_template('g1_booklist.html', page_title=page_title, 
                                              book_list=book_list, 
                                              links=links,
                                              authors=authors)
    
@app.route('/g1/books/<book_id>')
def g1_book_id(book_id):
    links = global_links
    authors=global_authors
    query="""'SELECT book.id, author.name, book.title, 
              book.isbn FROM book LEFT JOIN Author ON 
              book.author_id = author.id WHERE book.id = {};'.format(book_id)
              """
    db = sqlite3.connect('example.db')
    cursor = db.execute()
    id_num, name, title, isbn = cursor.fetchone(query)
    return render_template('g1_book_id.html', name=name,
                                              id_num=id_num,
                                              title=title,
                                              isbn=isbn,
                                              links=links,
                                              authors=authors)

@app.route('/g1/books_authors')
def g1_AuthorList():
    links = global_links
    authors=global_authors
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT book.id, book.title, author.name FROM book JOIN author ON book.author_id = author.id;')
    my_list = []
    for row in cursor.fetchall():
        book_id = row[0]
        book_title = row[1]
        author = row[2]
        my_list.append({'id':book_id,'book_name':book_title,'author':author})
    return render_template('g1_authors.html',
                                title = 'The Author-Book List',
                                book_list = my_list,
                                links=links,  #javascript:void(0) ???
                                authors=authors)
                                
@app.route('/g1/addbook', methods=['GET','POST'])
def addbook():
    db = sqlite3.connect('example.db')
    grab_authors = db.execute('SELECT name, id FROM author;')
    author_ref = [row for row in grab_authors.fetchall()] #(authorname, id#)
    links = global_links
    authors= sorted([row[0] for row in author_ref])
    title = 'Enter in a new book!'
    if request.method == "GET":
        return render_template('g1_get.html', title=title, 
                                              links=links, 
                                              authors=authors, 
                                              author_ref=author_ref)
    elif request.method == 'POST':
        
        author_name = request.form['author_name']
        book_title = request.form['book_title']
        isbn = request.form['isbn']
        author_id = [item[1] for item in author_ref if author_name in item[0]]#KeyError: u'Mark' ?????
        
        db = sqlite3.connect('example.db')
        db.execute('INSERT INTO book (author_id, title, isbn) VALUES(?,?,?)',(author_id[0], book_title, isbn))
        db.commit()
        #flash('New book added!') #should flash this message when a book is entered
        return redirect('/g1/books')

        
@app.route('/g1/newauthor', methods=['GET','POST'])
def new_author():
    links = global_links
    db = sqlite3.connect('example.db')
    grab_authors = db.execute('SELECT name FROM author;')
    author_ref = [row for row in grab_authors.fetchall()]
    if request.method == 'GET':
        return render_template('g1_newauthor.html', links=links)
    
    elif request.method == 'POST':
        author_name = request.form['author_name']
        country_id = request.form['country_id']
        
        if author_name in author_ref:
            return redirect('/g1/newauthor') # Change this to show "Author already in DB"
        else:
            db.execute('INSERT INTO author (name, country_id) VALUES(?,?)', (author_name, country_id))
            db.commit()
            return redirect('g1/addbook')
    
################################################################################################    
    

        


"""
INSERT INTO author (id, country_id, name) VALUES (4, 3, 'Jorge Luis Borges');

-- Books
INSERT INTO book (id, author_id, title ,isbn) VALUES (1, 1, 'The Raven', '978-3-16-148410-0');

drop table if exists book;
create table book (
  id integer primary key autoincrement,
  author_id integer,
  title text not null,
  isbn text
  """