class Producer:
    def __init__(self, broker, name="Producer"):
        self.broker = broker
        self.name = name

    def send(self, topic, message):
        print(f"[{self.name}] Sending message to '{topic}': {message}")
        self.broker.publish(topic, message)
