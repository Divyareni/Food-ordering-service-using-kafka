import uuid
import json

from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)


def delivery_report(err, msg):
    if err:
        print(f"Delivery {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")
        print(dir(msg))
        print(f"Delivered to {msg.topic()}, partition: {msg.partition()}")


order = {
    "order_id": str(uuid.uuid4()),
    "user": "Divya",
    "item": "Mushroom pizza",
    "quantity": 2
}

value = json.dumps(order).encode("utf-8")
producer.produce(topic="orders", value=value, callback=delivery_report)
producer.flush()
