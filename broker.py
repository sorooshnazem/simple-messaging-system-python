class Broker:
    def __init__(self):
        self.topics = {}

    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = []
            print(f"Topic '{topic_name}' created.")

    def publish(self, topic_name, message):
        if topic_name not in self.topics:
            raise Exception(f"Topic '{topic_name}' does not exist.")
        self.topics[topic_name].append(message)
        print(f"Published message to '{topic_name}': {message}")

    def get_messages(self, topic_name, offset):
        if topic_name not in self.topics:
            raise Exception(f"Topic '{topic_name}' does not exist.")
        return self.topics[topic_name][offset:], len(self.topics[topic_name])
