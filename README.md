# esquiz

Minimal web application to generate poll/quiz using Elasticsearch as a backennd. It also provides a draw mechanism (/draw endpoint) to pick a winner among all the correct answers.

Access and response can be visualize using pre-built Kibana dashboards.


## Requirements

- Elasticsearch 5.2.2 or above
- Kibana 5.2.2 or above
- XPack for authentication/authorization
- Ingest geoip processor plugin
- Ingest user agent processor plugin

## Configuration

- [Elasticsearch configuration](https://github.com/mcascallares/esquiz/blob/master/main.py#L12)
- [Questions and answers](https://github.com/mcascallares/esquiz/blob/master/quiz.py)

## Running in development mode

1. Install requirements

```
pip install -r requirements.txt`
```

2. Run web application using Flask

```
> export FLASK_APP=main.py
> export FLASK_DEBUG=1
> flask run
```

## Running in GCP

1. Create a Python GCP app

2. Deploy web application

```
> pip install -t lib -r requirements.txt
> gcloud app deploy 
```


## Kibana

1. Create a Kibana index pattern using 'esquiz' with time based events

2. Import Kibana objects stored in [kibana.json](https://github.com/mcascallares/esquiz/blob/master/etc/kibana.json)


## Screenshots

![Screen01](https://github.com/mcascallares/esquiz/blob/master/screenshots/screen01.png)
![Screen02](https://github.com/mcascallares/esquiz/blob/master/screenshots/screen02.png)
![Screen03](https://github.com/mcascallares/esquiz/blob/master/screenshots/screen03.png)

