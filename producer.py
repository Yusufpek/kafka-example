import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='172.19.0.3:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for _ in range(100):
    producer.send(
        topic='test',
        value='hello world',
    )
    time.sleep(2)
    print("send")
