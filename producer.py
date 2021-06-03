# Created by Sezer BOZKIR<admin@sezerbozkir.com> at 1.06.2021
from kafka import KafkaProducer
from time import sleep


def kafka_producer_sync(procuder: KafkaProducer, msg, size):
    print("Senkron mesaj gonderimi basladi.")
    for _ in range(size):
        future = procuder.send("sample_topic", msg)
        result = future.get(timeout=60)
        print(result)
        procuder.flush()
        sleep(1)


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


def kafka_producer_async(producer: KafkaProducer, msg, size):
    print("Asenkron mesaj gonderimi basladi.")
    for _ in range(size):
        producer.send("sample_topic", msg).add_callback(success).add_errback(error)
        producer.flush()
        sleep(1)


if __name__ == '__main__':
    main_producer = KafkaProducer(bootstrap_servers="localhost:9092")
    main_msg = ('Bu Ornek Bir Kafka Mesaj Gonderimidir' * 20).encode()[:100]
    kafka_producer_sync(main_producer, main_msg, 10)
    kafka_producer_async(main_producer, main_msg, 10)
