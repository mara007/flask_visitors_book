from flask import Flask, request
from datetime import datetime

class Visitors(object):
    html_main_style = '''
<style>
:root {
  --white: #afafaf;
  --red: #e31b23;
  --bodyColor: #292a2b;
  --borderFormEls: hsl(0, 0%, 10%);
  --bgFormEls: hsl(0, 0%, 14%);
  --bgFormElsFocus: hsl(0, 7%, 20%);
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  outline: none;
}

a {
  color: inherit;
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 70%;
}

td, th {
  border: 1px solid #216296;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #355a78;
}
input,
select,
textarea,
button {
  font-family: inherit;
  font-size: 100%;
}

button,
label {
  cursor: pointer;
}

select {
  appearance: none;
}

/* Remove native arrow on IE */
select::-ms-expand {
  display: none;
}

/*Remove dotted outline from selected option on Firefox*/
/*https://stackoverflow.com/questions/3773430/remove-outline-from-select-box-in-ff/18853002#18853002*/
/*We use !important to override the color set for the select on line 99*/
select:-moz-focusring {
  color: transparent !important;
  text-shadow: 0 0 0 var(--white);
}

textarea {
  resize: none;
}

ul {
  list-style: none;
}

body {
  font: 18px/1.5 "Open Sans", sans-serif;
  background: var(--bodyColor);
  color: var(--white);
  margin: 1.5rem 0;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1.5rem;
}


/* FORM ELEMENTS
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.my-form h1 {
  margin-bottom: 1.5rem;
}

.my-form li,
.my-form .grid > *:not(:last-child) {
  margin-bottom: 1.5rem;
}

.my-form select,
.my-form input,
.my-form textarea,
.my-form button {
  width: 100%;
  line-height: 1.5;
  padding: 15px 10px;
  border: 1px solid var(--borderFormEls);
  color: var(--white);
  background: var(--bgFormEls);
  transition: background-color 0.3s cubic-bezier(0.57, 0.21, 0.69, 1.25),
    transform 0.3s cubic-bezier(0.57, 0.21, 0.69, 1.25);
}

.my-form textarea {
  height: 170px;
}

.my-form ::placeholder {
  color: inherit;
  /*Fix opacity issue on Firefox*/
  opacity: 1;
}

.my-form select:focus,
.my-form input:focus,
.my-form textarea:focus,
.my-form button:enabled:hover,
.my-form button:focus,
.my-form input[type="checkbox"]:focus + label {
  background: var(--bgFormElsFocus);
}

.my-form select:focus,
.my-form input:focus,
.my-form textarea:focus {
  transform: scale(1.02);
}

.my-form *:required,
.my-form select {
  background-repeat: no-repeat;
  background-position: center right 12px;
  background-size: 15px 15px;
}

.my-form *:required {
  background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/asterisk.svg);  
}

.my-form select {
  background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/down.svg);
}

.my-form *:disabled {
  cursor: default;
  filter: blur(2px);
}


/* FORM BTNS
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.my-form .required-msg {
  display: none;
  background: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/asterisk.svg)
    no-repeat center left / 15px 15px;
  padding-left: 20px;
}

.my-form .btn-grid {
  position: relative;
  overflow: hidden;
  transition: filter 0.2s;
}

.my-form button {
  font-weight: bold;
}

.my-form button > * {
  display: inline-block;
  width: 100%;
  transition: transform 0.4s ease-in-out;
}

.my-form button .back {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-110%, -50%);
}

.my-form button:enabled:hover .back,
.my-form button:focus .back {
  transform: translate(-50%, -50%);
}

.my-form button:enabled:hover .front,
.my-form button:focus .front {
  transform: translateX(110%);
}


/* CUSTOM CHECKBOX
–––––––––––––––––––––––––––––––––––––––––––––––––– */
.my-form input[type="checkbox"] {
  position: absolute;
  left: -9999px;
}

.my-form input[type="checkbox"] + label {
  position: relative;
  display: inline-block;
  padding-left: 2rem;
  transition: background 0.3s cubic-bezier(0.57, 0.21, 0.69, 1.25);
}

.my-form input[type="checkbox"] + label::before,
.my-form input[type="checkbox"] + label::after {
  content: '';
  position: absolute;
}

.my-form input[type="checkbox"] + label::before {
  left: 0;
  top: 6px;
  width: 18px;
  height: 18px;
  border: 2px solid var(--white);
}

.my-form input[type="checkbox"]:checked + label::before {
  background: var(--red);
}

.my-form input[type="checkbox"]:checked + label::after {
  left: 7px;
  top: 7px;
  width: 6px;
  height: 14px;
  border-bottom: 2px solid var(--white);
  border-right: 2px solid var(--white);
  transform: rotate(45deg);
}


/* FOOTER
–––––––––––––––––––––––––––––––––––––––––––––––––– */
footer {
  font-size: 1rem;
  text-align: right;
  backface-visibility: hidden;
}

footer a {
  text-decoration: none;
}

footer span {
  color: var(--red);
}


/* MQ
–––––––––––––––––––––––––––––––––––––––––––––––––– */
@media screen and (min-width: 600px) {
  .my-form .grid {
    display: grid;
    grid-gap: 1.5rem;
  }

  .my-form .grid-2 {
    grid-template-columns: 1fr 1fr;
  }

  .my-form .grid-3 {
    grid-template-columns: auto auto auto;
    align-items: center;
  }

  .my-form .grid > *:not(:last-child) {
    margin-bottom: 0;
  }

  .my-form .required-msg {
    display: block;
  }
}

@media screen and (min-width: 541px) {
  .my-form input[type="checkbox"] + label::before {
    top: 50%;
    transform: translateY(-50%);
  }

  .my-form input[type="checkbox"]:checked + label::after {
    top: 3px;
  }
}

.my-form div {
  width: 500px;
  margin: auto;
  border: 3px solid #355a78;
}
</style>
'''

    html_main = '''
<div class="my-form">
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
</div>
'''

    html_table = '''
<div>
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
        return f'{self.html_main_style} {self.html_main}'


    def on_visitors_show(self):
        html = f'''
{self.html_main_style}
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
            return f'{self.html_main_style}<div><h1>Error: you must enter at least one entry!</h1>{self.html_return}</div>'

        if last_visit:
            html_last_visit = f'Your last visit was at {last_visit}<br>'
        else:
            html_last_visit = '<br>'

        html = f'''
{self.html_main_style}
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
        return f'{self.html_main_style} {self.html_delete}'
