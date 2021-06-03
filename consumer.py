# Created by Sezer BOZKIR<admin@sezerbozkir.com> at 1.06.2021
from kafka import KafkaConsumer
from pprint import pprint

if __name__ == '__main__':
    consumer = KafkaConsumer('sample_topic', bootstrap_servers="localhost:9092",
                             enable_auto_commit=False)
    pprint(consumer.metrics())
    for msg in consumer:
        pprint(msg)
