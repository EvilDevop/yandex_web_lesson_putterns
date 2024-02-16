from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/list_prof/<list>')
def main_page(list):
    with open("static/profs.json", "rt", encoding="utf8") as f:
        prof_list = json.loads(f.read())
    return render_template('professions_pattern.html', list=list, prof_list=prof_list)


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')