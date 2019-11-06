import base64
import requests as r 
from flask import *
from mako.template import Template
import html

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/intro-gan', methods=['GET', 'POST'])
def base():
    person = ""
    if request.method == 'POST':
        if request.form['name']:
            bases = request.form['name']
            before_xor = base64.b64decode(bases).decode('utf-32')
            base = html.escape(before_xor)
            person = base

    template = 'Your Name %s Inimda' % person
    return Template(template).render(data="world")


@app.route('/example', methods=['GET', 'POST'])
def example():
    url = "http://127.0.0.1:6001/intro-gan"
    name = "Im Nayeon".encode('utf-32')
    grup = base64.b64encode(name)
    data = {'name': grup}
    return r.post(url, data=data).text

if __name__ == "__main__":
    app.run("0.0.0.0", port=6001, debug=False)
