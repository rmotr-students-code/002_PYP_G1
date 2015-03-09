from flask import Flask, render_template_string

app = Flask("This is my first app")

@app.route("/")
def say_me_hello():
    """Rendering with context variables"""
    my_name = "Martin"
    html = """
        <html>
            <h1>Hello {{my_name}}!</h1>
        </html>
    """
    return render_template_string(html, my_name=my_name)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
