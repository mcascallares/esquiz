import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from elasticsearch import Elasticsearch
from datetime import datetime
from quiz import quiz

app = Flask(__name__)
app.secret_key = 'dfuy48yerhfjdbsklueio'

es = Elasticsearch(
    ['http://localhost:9200/'],
    http_auth=('elastic', 'changeme'),
)

#es = Elasticsearch(
#    ['localhost', 'otherhost'],
#    http_auth=('user', 'secret'),
#    port=443,
#    use_ssl=True
#)

@app.route('/')
def index():
    return render_template('index.html', quiz=quiz)


@app.route('/submit', methods=['POST'])
def submit():
    form = request.form.to_dict()
    doc = {
        'timestamp': datetime.utcnow(),
        'email' : form['email'],
        #'remote_addr' : request.remote_addr, # TODO remove this!
        'remote_addr' : '8.8.8.8',
        'user_agent' : request.headers.get('User-Agent'),
        'correct': True
    }

    for q in quiz:
        doc[q['name']] = {
            'question' : q['question'],
            'answer' : form[q['name']]
        }
        if form[q['name']] != [i for i in q['options'] if i['correct']][0]['answer']:
            doc['correct'] = False

    es.index(index='esquiz', doc_type='answer', pipeline='esquiz', body=doc)
    flash('Thanks for your response')
    return redirect(url_for('index'))


@app.errorhandler(500)
def server_error(e):
    # For Google App Engine
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


if __name__ == '__main__':
    app.run()
