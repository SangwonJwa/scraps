import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080/api/v1/dags?paused=false"
dags = requests.get(url, auth=HTTPBasicAuth('airflow', 'airflow'))
dags = dags.json()['dags']

for dag in dags:
    print(dag['dag_id'])
