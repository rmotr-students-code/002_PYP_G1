from server import app, render_template_string
import sqlite3
from server import app
from flask import render_template


@app.route('/paulo/author_list')
def author_list():
    db = sqlite3.connect('example.db')
    cursor = db.execute('SELECT id, name FROM author;')
    author_list_data = []
    for row in cursor.fetchall():
        id = row[0]
        bookname = row[1]
        itm = (id, bookname)
        author_list_data.append(itm)
    return render_template('paulo/paulotemplate.html', authors=author_list_data)
    # return str(author_list_data)

@app.route('/paulo')
def paulo_main():
    return "Hello paulo!"
    
@app.route('/paulo/html-sample')
def sample_2():
    return "<h1>lkjasdklja</h1>"
    

@app.route('/paulo/sheep')
def paulo_sheep():
    sheep_text = """<br>I'm really scared of bears. You would be too. <br><br>
                    <br>I'm serious<br>
                    <br><img src="https://c402277.ssl.cf1.rackcdn.com/photos/1014/images/carousel_small/brown-bear-why-they-matterHI_205432.jpg?1345535509"> <br>
                    
                    
                <a href="https://plus.google.com/photos/105384813851804807673/albums/6058940110498579985?authkey=COLuttHyucGuFA">Click here for pictures (you can see them better than on the slideshow below)</a>
                
                <br />
                <br />
                <br />
                <embed flashvars="host=picasaweb.google.com&amp;hl=en_US&amp;feat=flashalbum&amp;RGB=0x000000&amp;feed=https%3A%2F%2Fpicasaweb.google.com%2Fdata%2Ffeed%2Fapi%2Fuser%2F105384813851804807673%2Falbumid%2F6058940110498579985%3Falt%3Drss%26kind%3Dphoto%26authkey%3DGv1sRgCOLuttHyucGuFA%26hl%3Den_US" height="400" pluginspage="http://www.macromedia.com/go/getflashplayer" src="https://photos.gstatic.com/media/slideshow.swf" type="application/x-shockwave-flash" width="600"></embed>
                """
    return sheep_text
    
