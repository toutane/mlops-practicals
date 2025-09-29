import json
import signal
import types

import psycopg
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
    with psycopg.connect(
        "host=localhost port=5432 dbname=postgres user=postgres password=mysecretpassword"
    ) as conn:
        for msg in consumer:
            prediction = msg.value
            print(f"received: {prediction}")
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO predictions (X, y_pred) VALUES (%s, %s)",
                    (
                        prediction["X"],
                        prediction["y_pred"],
                    ),
                )
                conn.commit()
    exit(0)
