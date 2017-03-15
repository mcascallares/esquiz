from flask import Flask, render_template, request, redirect, url_for, flash
from elasticsearch import Elasticsearch
from datetime import datetime
from quiz import quiz

app = Flask(__name__)
app.secret_key = 'dfuy48yerhfjdbsklueio'

app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200/'
es = Elasticsearch([app.config['ELASTICSEARCH_URL']])

@app.route('/')
def index():
    return render_template('index.html', quiz=quiz)


@app.route('/submit', methods=['POST'])
def submit():
    form = request.form.to_dict()
    doc = {
        'correct': True,
        'timestamp': datetime.now(),
        'email' : form['email']
    }

    for q in quiz:
        doc[q['name']] = form[q['name']]
        if form[q['name']] != [i for i in q['options'] if i['correct']][0]['answer']:
            doc['correct'] = False

    res = es.index(index='esquiz', doc_type='answer', body=doc)
    flash('Thank you!') #TODO show this
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
