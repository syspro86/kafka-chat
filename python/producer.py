from kafka import KafkaProducer
# https://kafka-python.readthedocs.io/en/master/

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    producer.send('chat', b'hello')
producer.flush()
