from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<! DOCTYPE html>

<html>
    <head>
        <style>
        """

form = """
{
background-color: #eee;
padding: 20px;
margin: 0 auto;
width: 540px;
font: 16px sans-serif;
border-radius: 10px;
}
"""
textarea = """{
margin: 10px 0;
width: 540px;
height: 120px;
}
"""
rest_code = """
</style>
</head>
<body>
<form method="post">
        <label>
            Rotated by <input type="text" value= 0 name="rot"/>
        </label>
        <input type="submit" value="Submit"/>
        <input type="textarea" name = "text"/>
    </form>
</body>
</html>
"""


@app.route("/")
def index():
    content = page_header + form + textarea + rest_code

    return content

app.run()