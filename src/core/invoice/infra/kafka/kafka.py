from dataclasses import dataclass
from typing import Optional
from confluent_kafka import Producer, Consumer, KafkaError
from core.invoice.application.usecase.dto import MessageOutput


@dataclass(slots=True)
class KafkaConfig:
    bootstrap_servers: str
    producer: Optional[dict] = None
    consumer: Optional[dict] = None

    def __post_init__(self):
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        self.consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': 'invoice',
            'auto.offset.reset': 'earliest'
        })

    def send(self, message: str) -> None:
        self.producer.produce(message.topic, value=str(message.content))
        print(f"Sent message: {message.topic} - {message.content}")
        self.producer.flush()

    def consume(self, topics, callback) -> None:
        self.consumer.subscribe(topics)
        while True:
            message = self.consumer.poll(1.0)
            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    continue
                print(f"Error occurred: {message.error().str()}")
                break
            callback(message.value().decode("utf-8"))
            print(f"Received message: {message.value().decode('utf-8')}")

        self.consumer.close()

    @dataclass(slots=True, frozen=True)
    class Message(MessageOutput):
        pass
