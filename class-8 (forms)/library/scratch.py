from server import app
from flask import render_template, request
import sqlite3


# @app.route('/books')
# def all_books():
#     books = []
#     db = sqlite3.connect('example.db')
#     get_rows = """SELECT id,title,isbn FROM book;"""
#     rows = db.execute(get_rows)
#     for row in rows.fetchall():
#         book_id = row[0]
#         book_title = row[1]
#         book_isbn = row[3]
#         books.append(book_id, book_title, book_isbn)
#     return render_template('books.html', books=books)
    
# @app.route('/books/<book_id>')
# def by_book():
#     db = sqlite3.connect('example.db')
#     pass

# @app.route('/authors')
# def all_author():
#     authors = []
#     db = sqlite3.connect('example.db')
#     get_rows = """SELECT author.name, country.country
#                 FROM author
#                 JOIN country
#                 ON author.country_id=country.id"""
#     rows = db.execute(get_rows)
#     for row in rows.fetchall():
#         name = row[0]
#         country = row[1]
#         authors.append([name,country])
#     return render_template('authors.html', authors=authors)

# @app.route('/authors/<author_id>')
# def by_author():
#     db = sqlite3.connect('example.db')    
#     pass

# Search Bar, work in progress
# Need to create indexes for db(?)
# @app.route('/search', methods=['GET', 'POST'])
# def search_db():
#     if request.methods=='POST':
#         db = sqlite3.connect('example.db')
#         author = request.form['author']
#         keyword = request.form['keyword']
#         if author and keyword:
#             results = []
#             get_rows = """SELECT author.name, book.title
#                         FROM author
#                         JOIN country
#                         ON author.id=book.author_id
#                         WHERE author.name=? AND book.title=?""",(author, keyword)
#             rows = db.execute(get_rows)
#             for row in rows.fetchall:
#                 name = row[0]
#                 book = row[1]
#                 results.append([name,book])
#         elif author:
#             get_rows = "SELECT name FROM author WHERE name LIKE %?%",(author)
#             rows = db.execute(get_rows)
#             results = [name for name in rows.fetchall()]
#         elif keyword:
#             get_rows = "SELECT title FROM book WHERE title LIKE %?%",(keyword)
#             rows = db.execute(get_rows)
#             results = [title for title in rows.fetchall()]
#         else:
#             results.append("None Found")
#         return render_template('search.html', results=results)#     
# elif request.methosd=='GET':
# PASS  

        