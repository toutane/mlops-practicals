from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='nowledgeable.com:9092')
future = producer.send('leger', json.JSONEncoder().encode({"data": [[1, 2], [3, 4]]}).encode('utf-8'))
future.get(timeout=60)
