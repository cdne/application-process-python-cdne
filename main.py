import data_manager
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('László')
    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/all-mentors')
def all_names():
    first_and_last_name = data_manager.get_mentors_names()
    return render_template('first_second_name.html', first_and_last_name=first_and_last_name)


if __name__ == '__main__':
    app.run(debug=True)
