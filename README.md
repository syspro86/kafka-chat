## kafka-chat

kafka를 활용한 chat 제작 연습

## local test

kafka 배포

```
kubectl create namespace chat
kubectl apply -f kubernetes
```

테스트를 위한 포트 포워딩

```
kubectl port-forward deployment/kafka 9092 -n chat
```

consumer (새로운 터미널을 열고)

```
cd python
python consumer.py
```

producer (3번째 터미널을 열고)

```
cd python
python producer.py
```

consumer 터미널에서 로그가 출력된다

```
ConsumerRecord(topic='chat', partition=0, offset=0, timestamp=1653485416522, timestamp_type=0, key=None, value=b'hello', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=5, serialized_header_size=-1)
ConsumerRecord(topic='chat', partition=0, offset=1, timestamp=1653485416522, timestamp_type=0, key=None, value=b'hello', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=5, serialized_header_size=-1)
.............
ConsumerRecord(topic='chat', partition=0, offset=98, timestamp=1653485416523, timestamp_type=0, key=None, value=b'hello', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=5, serialized_header_size=-1)
ConsumerRecord(topic='chat', partition=0, offset=99, timestamp=1653485416523, timestamp_type=0, key=None, value=b'hello', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=5, serialized_header_size=-1)
```
