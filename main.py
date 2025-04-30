from broker import Broker
from producer import Producer
from consumer import Consumer

# Initialize broker and create topic
broker = Broker()
broker.create_topic("events")

# Initialize producer and send messages
producer = Producer(broker, name="P1")
producer.send("events", "User registered")
producer.send("events", "User updated profile")

# Initialize consumer and read messages
consumer = Consumer(broker, name="C1")
consumer.consume("events")
consumer.consume("events")

# More messages
producer.send("events", "User deleted account")
consumer.consume("events")