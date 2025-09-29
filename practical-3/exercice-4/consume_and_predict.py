import json
import os
import signal
import types
from typing import Optional

import joblib
import numpy as np
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from sklearn.linear_model import LinearRegression

folder = "../../models"


def signal_handler(
    sig: int,
    frame: Optional[types.FrameType],
    consumer: KafkaConsumer,
    producer: KafkaProducer,
) -> None:
    consumer.close()
    producer.close()
    exit(0)


def load_model(filename: str) -> Optional[LinearRegression]:
    model = None
    if os.path.exists(filename):
        model = joblib.load(filename)
    return model


if __name__ == "__main__":
    model = load_model(os.path.join(folder, "regression.joblib"))
    if model is None:
        exit(1)
    consumer = KafkaConsumer(
        "my-topic",
        bootstrap_servers=["localhost:9092"],
        value_deserializer=lambda m: json.loads(m.decode()),
    )
    if consumer is None:
        exit(1)
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda m: json.dumps(m).encode(),
    )
    if producer is None:
        consumer.close()
        exit(1)
    signal.signal(
        signal.SIGINT, lambda sig, _: signal_handler(sig, None, consumer, producer)
    )
    for msg in consumer:
        X_arr = msg.value["X"]
        X_nparr = np.array(X_arr).reshape(1, -1)
        X_df = pd.DataFrame(X_nparr, columns=["size", "nb_rooms", "garden"])
        y_pred = model.predict(X_df)[0]
        print(f"Prediction of {X_arr} is: {y_pred:.2f}")
        prediction = {"X": X_arr, "y_pred": y_pred}
        producer.send("prediction_charles-antoine", prediction)
    exit(0)
