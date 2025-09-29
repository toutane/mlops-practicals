import json
import signal
import types

from kafka import KafkaConsumer


def signal_handler(sig: int, frame: types.FrameType | None, consumer: KafkaConsumer):
    consumer.close()
    exit(1)


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "prediction_charles-antoine",
        bootstrap_servers=["localhost:9092"],
        value_deserializer=lambda m: json.loads(m.decode()),
    )
    if not consumer:
        exit(1)
    signal.signal(signal.SIGINT, lambda sig, _: signal_handler(sig, None, consumer))
    for msg in consumer:
        print(f"received: {msg.value}")
    exit(0)
