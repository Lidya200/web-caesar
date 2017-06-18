from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>

  
"""
@app.route("/")
def index():
    return form

@app.route("/", methods= ["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    try:
        int(rot)
    except ValueError:
        return "<h1>" + rotate_string("Your entry was not valid try agin", 0) + "</h1>"
    if int(rot) != 0:
        return "<h1>" + rotate_string(text, int(rot)) + "</h1>"
    else:
        return "<h1>" + rotate_string("Your entry was not valid try agin", 0) + "</h1>"

app.run()
