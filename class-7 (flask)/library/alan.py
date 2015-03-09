from server import app, render_template
import sqlite3

@app.route('/alan')
def alan_main():
    return "Hello alan!"



@app.route('/alan/bookinfo')
def present_authors():
    title = 'books'
    authors = [] #[(id#, author_name)]
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author;')
    for item in cursor.fetchall():
        id = item[0]
        name= item[1]
        authors.append((id, name))
    return render_template('alan/alanbooks.html',title=title, authors=authors)
    
    
    


@app.route('/alan/test')
def sample_page():
    rmotr = "Advanced Python Class"
    student = "Alan"
    favorite_site = "reddit.com"
    favorite_car = "BMW M3"
    html = """
    <html>
        <h1>Welcome to the {{rmotr}} sample page</h1>
        <p1>Among the many talented students in the class is {{student}},
        an unusually handsome individual.</p1>
        
        <p2>He frequently visits {{favorite_site}}, and one day wishes to drive
        a {{favorite_car}}</p2>
        
        <p3>Here's a link to reddit:</p3>
        <a href="http://www.{{favorite_site}}"><img src="https://www.redditstatic.com/about/assets/reddit-alien.png"></a>
    </html>
    """
    return render_template_string(html, rmotr=rmotr, student=student,
    favorite_site=favorite_site, favorite_car=favorite_car)
    
