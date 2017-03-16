import logging
import certifi
from elasticsearch import Elasticsearch
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from quiz import quiz

app = Flask(__name__)
app.secret_key = 'dfuy48yerhfjdbsklueio'

es = Elasticsearch(
    ['https://a8a9927db88266cd7ec03ad563239b5c.ap-northeast-1.aws.found.io:9243'],
    http_auth=('elastic', 'BEcACgDS5dIbsNHVaiSdAWTi'),
    send_get_body_as='POST',
    use_ssl=True,
    ca_certs=certifi.where()
)

@app.route('/')
def index():
    return render_template('index.html', quiz=quiz)


@app.route('/submit', methods=['POST'])
def submit():
    form = request.form.to_dict()
    doc = {
        'timestamp': datetime.utcnow(),
        'email' : form['email'],
        'remote_addr' : request.remote_addr,
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
