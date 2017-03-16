# esquiz

Minimal web application to generate poll/quiz using Elasticsearch as a backennd. It also provides a draw mechanism to pick a winner among all the correct answers.

Access and response can be visualize using pre-built Kibana dashboards.


## Requirements

- Elasticsearch 5.2.2 or above
- Kibana 5.2.2 or above
- XPack for authentication/authorization
- Ingest geoip processor plugin
- Ingest user agent processor plugin
- Check Python libraries in requirements.txt


## Running in development mode

1. Install requirements

`pip install -r requirements.txt`


2. Run web application in development

```
> export FLASK_APP=main.py
> export FLASK_DEBUG=1
> flask run
```

3. Run web application in GCP

```
> pip install -t lib -r requirements.txt
```


4. Setup Kibana

1. Create a Kibana index pattern using 'esquiz' with time based events
2. Import Kibana objects stored in [kibana.json](https://github.com/mcascallares/esquiz/blob/master/etc/kibana.json)
## Screenshots

![Screen01](https://github.com/mcascallares/esquiz/blob/master/screenshots/screen01.png)
![Screen02](https://github.com/mcascallares/esquiz/blob/master/screenshots/screen02.png)
![Screen03](https://github.com/mcascallares/esquiz/blob/master/screenshots/screen03.png)

