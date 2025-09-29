from kafka import KafkaConsumer
consumer = KafkaConsumer('exo1', bootstrap_servers='nowledgeable.com:9092')
for msg in consumer:
    print (msg)

