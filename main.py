from flask import Flask, render_template, request, redirect, url_for, flash
#from elasticsearch import Elasticsearch

app = Flask(__name__)
app.secret_key = 'dfuy48yerhfjdbsklueio'

#app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200/'
#es = Elasticsearch([app.config['ELASTICSEARCH_URL']])

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    print request.form.keys
    flash('Thank you!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
