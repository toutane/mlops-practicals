import json

from kafka import KafkaProducer

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda m: json.dumps(m).encode(),
    )
    producer.send("my-topic", {"X": [1, 2, 3]})
    producer.flush()
