class Consumer:
    def __init__(self, broker, name="Consumer"):
        self.broker = broker
        self.offsets = {}
        self.name = name

    def consume(self, topic):
        offset = self.offsets.get(topic, 0)
        messages, new_offset = self.broker.get_messages(topic, offset)
        if messages:
            print(f"[{self.name}] Consumed messages from '{topic}': {messages}")
            self.offsets[topic] = new_offset
        else:
            print(f"[{self.name}] No new messages in '{topic}'.")
