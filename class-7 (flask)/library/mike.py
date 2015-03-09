from server import app
from flask import render_template
import sqlite3


@app.route('/mike/AllBooks')
def mike_AllBooks():
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author;')
    lst_auth = []
    for row in cursor.fetchall():
        auth_id = row[0]
        auth_name = row[1]
        lst_auth.append({'id': auth_id, 'name': auth_name})
    cursor1 = db.execute('SELECT id, name FROM country;')
    lst_country = []
    for row in cursor1.fetchall():
        lst_country.append(row[0])
        lst_country.append(row[1])
    return render_template('/Mike/AllBooks.html', lst_auth=lst_auth, lst_country=lst_country)
    
@app.route('/mike/Book3')
def mike_Book3():
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author;')
    lst_auth = []
    for row in cursor.fetchall():
        auth_id = row[0]
        auth_name = row[1]
        if auth_id == 3:
            lst_auth.append({'id': auth_id, 'name': auth_name})
    return render_template('/Mike/Book3.html', lst_auth=lst_auth)


@app.route('/mike/<auth_id>')
def mike_auth():
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author if id = <auth_id>;')
    lst_auth = []
    for row in cursor.fetchall():
        auth_id = row[0]
        auth_name = row[1]
        lst_auth.append({'id': auth_id, 'name': auth_name})
    return render_template('/Mike/auth_id.html', lst_auth=lst_auth, auth_id = auth_id)

    
