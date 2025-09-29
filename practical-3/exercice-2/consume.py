from kafka import KafkaConsumer
import json
import numpy as np
consumer = KafkaConsumer('leger', bootstrap_servers='nowledgeable.com:9092')
for msg in consumer:
    data = json.loads(msg.value)
    arr = np.array(data["data"])
    print(f'sum is: {np.sum(arr)}')

