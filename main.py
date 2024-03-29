from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def main_page(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')