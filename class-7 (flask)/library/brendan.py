from server import app
from flask import render_template
import sqlite3

@app.route('/brendan')
def brendan_main():
    return 'This is Brendan\'s main page'

@app.route('/brendan/list')
def brendan_list_authors():
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author;')
    authors = []
    
    for row in cursor.fetchall():
        id = row[0]
        name = row[1]
        authors.append({'id': id, 'name': name})
    return render_template('Brendan/author_list2.html', authors=authors)