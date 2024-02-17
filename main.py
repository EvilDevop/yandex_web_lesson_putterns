from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    crew_list = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution_pattern.html', crew_list=crew_list)


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1')