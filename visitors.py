from flask import Flask, request
from datetime import datetime
from html_style import HtmlStyle

class Visitors(object):
    html_main = '''
<div>
<h1 class="my-form">Visitors book:</h1>
</br>
<form class="my-form" action="/new_visitor" method="post">
    <label class="my-fomr" for="fname">First name:</label>
    <input class="my-fomr" type="text" id="fname" name="fname"><br><br>
    <label class="my-fomr" for="lname">Last name:</label>
    <input class="my-fomr" type="text" id="lname" name="lname"><br><br>
    <input class="my-fomr" type="submit" value="Submit">
</form>
<br>
<a href="/show_visitors">Show recent visitors..</a>
<br>
<a href="/delete_visitors">Delete visitors book content..</a>
'''

    html_table = '''
<br>
Recent visitors:
<table class="visitors_table">
    <tr>
        <th>Name</th>
        <th>Last name</th>
        <th>Last visit</th>
    </tr>
'''

    html_return = '<a href="/">Return to main page..</a>'
    html_delete = '''
<div>
<br><h2>list of visitors deleted!!</h2><br>
<a href="/">Return to main page..</a>
</div>
'''
    def __init__(self):
        self.visitors_list = []
        self.add('Jan', 'Novak')
        self.add('Jan', 'Starak')
        self.add('Pepa', 'Zdepa')
        self.add('Karel', 'Zeman')


    def add(self, name: str, surname: str) -> str or None:
        entry = (name, surname, datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        for i, v in enumerate(self.visitors_list):
            if v[0] == name and v[1] == surname:
                last_visit = self.visitors_list[i][2]
                self.visitors_list[i] = entry
                return last_visit

        self.visitors_list.append(entry)
        return None


    def clear_visitors(self):
        self.visitors_list.clear()


    def print_visitors_table(self):
        html = ''
        for v in self.visitors_list:
            html += f'    <tr><td>{v[0]}</td><td>{v[1]}</td><td>{v[2]}</td></tr>\n'

        html += '</table>'
        return self.html_table + html


    def on_main_show(self):
        return f'<html><head>{HtmlStyle.html_main_style} {self.html_main}</html></head>'


    def on_visitors_show(self):
        html = f'''
{HtmlStyle.html_main_style}
<div>
<h1>Hello!</h1>
{self.print_visitors_table()}
<br>
{self.html_return}
</div>
'''
        return html


    def on_new_visitor(self, name, surname):
        if len(name) or len(surname):
            last_visit = self.add(name, surname)
        else:
            return f'{HtmlStyle.html_main_style}<div><h1>Error: you must enter at least one entry!</h1>{self.html_return}</div>'

        if last_visit:
            html_last_visit = f'Your last visit was at {last_visit}<br>'
        else:
            html_last_visit = '<br>'

        html = f'''
{HtmlStyle.html_main_style}
<div>
<h1>Hello!</h1><br>Welcome <b>{name} {surname}</b>!<br>
{html_last_visit}
{self.print_visitors_table()}
<br>
{self.html_return}
</div>
'''
        return html


    def on_delete_visitors(self):
        self.visitors_list = []
        return f'{HtmlStyle.html_main_style} {self.html_delete}'
