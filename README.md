# esquiz

Minimal web application to general poll/quiz using Elasticsearch as a backend.


## Requirements

- Elasticsearch 5.2.2 or above
- Kibana 5.2.2 or above
- XPack
- Ingest geoip processor plugin
- Ingest user agent processor plugin
- Check Python libraries in requirements.txt


## Running in development mode

1. Install requirements

`pip install -r requirements.txt`

2. Run Flask web application

```
> export FLASK_APP=main.py
> export FLASK_DEBUG=1
> flask run
```

3. Setup Kibana
TODO

## Screenshots

TODO
