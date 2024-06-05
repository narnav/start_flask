from flask import Flask, render_template
api = Flask(__name__)

@api.route('/')
def hello():
    msg ="meir"
    return render_template("index.html",html_msg =msg)

@api.route('/about')
def about():
    msg ="eva"
    return render_template("about.html",html_msg =msg)

@api.route('/contact')
def contact():
    msg ="eva"
    return render_template("contact.html",html_msg =msg)

if __name__ == '__main__':
    api.run(debug=True)