#!/usr/bin/env python3

from flask import Flask, request


app = Flask(__name__)

visitor_list = []

@app.route("/")
def main_page_get():
    return main_page_uri_get('')


@app.route("/<uri>", methods=['GET', 'POST'])
def main_page_uri_get(uri):
    if request.method == 'GET':
        html = """
<h1>Hello world</h1>
</br>
<form action="/post_data" method="post">
<label for="fname">First name:</label>
<input type="text" id="fname" name="fname"><br><br>
<label for="lname">Last name:</label>
<input type="text" id="lname" name="lname"><br><br>
<input type="submit" value="Submit">
</form>
"""
        return html

    if request.method == 'POST':
        name = request.form.get('fname')
        surname = request.form.get('lname')

        visitor_list.append((name, surname))

        visitors_table = """
<table>
    <tr>
        <th>Name</th>
        <th>Last name</th>
    </tr>
"""
        for v in visitor_list:
            visitors_table += (f'<tr><td>{v[0]}</td><td>{v[1]}</td><tr>')

        html = f"""
<h1>Hello!</h1>
<br><br> You entered {name} {surname}!<br>
Used URI : {uri}<br>
Previous visitors:<br>
"""
        return html + visitors_table + '</table>'

if __name__ == "__main__":
    app.run()

