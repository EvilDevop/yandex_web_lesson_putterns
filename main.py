from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def main_page():
    with open("static/personal_data.json", "rt", encoding="utf8") as f:
        data_list = json.loads(f.read())
    return render_template('data_pattern.html', title='Анкета', list=data_list)


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')