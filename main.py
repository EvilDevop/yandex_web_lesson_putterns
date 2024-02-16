from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def main_page(prof):
    return render_template('expansion_pattern.html', prof=prof)


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')