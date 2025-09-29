from kafka import KafkaConsumer, KafkaProducer
import json
import numpy as np

consumer = KafkaConsumer('leger', bootstrap_servers='nowledgeable.com:9092')
producer = KafkaProducer(bootstrap_servers='nowledgeable.com:9092')
for msg in consumer:
    data = json.loads(msg.value)
    s = np.sum(np.array(data["data"]))
    producer.send('processed', str(s).encode('utf-8'))
    producer.flush()
