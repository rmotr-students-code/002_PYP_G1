from flask import (
    Flask, request, session, g, redirect, url_for,
    abort, render_template, render_template_string, flash
)

app = Flask('This is my first app')


@app.route('/rmotr', methods=['GET','POST'])
def testing():
    if request.method == 'GET':
        return """
            <html>
                <form method="POST">
                    First Name:
                    <input type="text" name="first-name">
                    <input type="text" name="last-name">
                    <input type="submit">
                </form>
            </html>
        """
    elif request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        return "Hello {} {}".format(first_name, last_name)
    

if __name__ == "__main__":
    
    # import all views
    from alan_martinV2 import *
    from charlie_mike_paulo import *
    from scratch import *
    from brencharmik import *
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
    
    # If you get a port being used error and no one else is on (they might be running one), try this:
    # move to the current directory: "cd DIRECTORY_PATH"
    # terminal: ps -fA | grep python
    
    # then look to see if a server.py process is running
    # if one is running, end it using "kill PROCESS_NUMBER and try running server.py"
    
    # if you're confused, don't kill a random process and hope it works. 
    
    # once it's running, make sure to stop the server when you're done using it so it 
    # doesn't bug out for others when they want to use it. control-c or STOP in 
    # terminal. 