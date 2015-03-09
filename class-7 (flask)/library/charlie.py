from server import app, render_template_string

@app.route('/charlie')
def charlie_main():
    return "A change has been made?"
    
@app.route('/charlie/my_profile')
def my_profile():
    name = "Charlie"
    age = 22
    location = "California"
    html = """
        <html>
            <head>
                <title>Charlie's Page</title>
            </head>
            
            <h1>My Information</h1>
            
            <div class='profile'>
                <ol>
                    <li>Name: {{ name }} </li>
                    <li>Age: {{ age }} </li>
                    <li>Location: {{ location }} </li>
                <ol>
            </div>
            <div class='picture-wall'>
                <h1>MY WATER IS ON FIRE!</h1>
                <img src='http://fc03.deviantart.net/fs44/f/2009/083/b/b/water_damp_fire_by_Slabik.jpg'>
            </div>
            
            <footer>
                <ul>
                    <li><a href='https://www.twitter.com'>Twitter</a></li>
                    <li><a href='https://www.github.com'>Github</a></li>
                    <li><a href='https://002-pyp-g1-martinzugnoni.c9.io/charlie'>Home</a></li>
                </ul>
            </footer>
            
            
            
        </html>
    """
    
    return render_template_string(html, name=name, age=age, location=location)