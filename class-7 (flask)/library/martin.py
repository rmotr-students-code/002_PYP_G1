from server import app, render_template
import sqlite3

@app.route('/martin')
def martin_main():
    return "Hello Martin!"

@app.route('/martin/book/<indv_id>')
def martin_list_authors(indv_id):
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author WHERE id = {0};'.format(indv_id))
    authors = []
    title = "Author List"
    
    for row in cursor.fetchall():
        id = row[0]
        name = row[1]
        authors.append({'id': id, 'name': name})
    return render_template('/martin/martinbook.html',title=title, authors=authors)