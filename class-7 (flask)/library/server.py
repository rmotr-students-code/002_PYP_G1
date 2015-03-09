from flask import (
    Flask, request, session, g, redirect, url_for,
    abort, render_template, render_template_string, flash
)

app = Flask('This is my first app')

@app.route('/authors/<author_id>')
def list_of_authors_with_template(author_id):
    """Moving the HTML code out of python modules"""
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author WHERE id = {0};'.format(author_id))
    author = cursor.fetchall()[0]
    return render_template('author_detail.html', author=author)


if __name__ == "__main__":
    
    # import all views
    from alan import *
    from charlie import *
    from paulo import *
    from mike import *
    from brendan import *
    from martin import *

    app.debug = True
    app.run(host='0.0.0.0', port=8080)
    