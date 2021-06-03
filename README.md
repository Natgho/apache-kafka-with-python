# Kafka Producer and Consumer Sample with Docker-compose
This repo shows how you can create a topic, send a message and listen to a kafka environment with 1 zookeper and 1 broker, which you simulate with docker-compose, using the python programming language.
## Run docker dompose
```shell
docker-compose up -d
```
## Start project
```shell
pip install -r requirements.txt
python producer.py
python consumer.py
```
Also you can take a look detailed article: