# Simple Messaging System in Python

This project is a **minimal simulation of a messaging system**, inspired by how real-world systems like [Apache Kafka](https://kafka.apache.org/) work under the hood. It’s built using plain Python classes and functions to help you **understand the core concepts** behind modern message brokers.

---

## What This Project Demonstrates

- The **Producer-Consumer** pattern
- A central **Broker** that stores messages in topics
- Manual **offset tracking** for consumers
- How systems like Kafka abstract and scale these concepts

---

## Components

| File           | Description                                    |
|----------------|------------------------------------------------|
| `broker.py`    | Manages topics and message storage             |
| `producer.py`  | Sends messages to a topic via the broker       |
| `consumer.py`  | Consumes messages from the broker by offset    |
| `main.py`      | Runs the simulation with sample messages       |

---

## How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/simple-messaging-system-python.git
   cd simple-messaging-system-python
   ```

2. **Run the simulation**
   ```bash
   python3 main.py
   ```

---

## Why I Built This

Messaging systems like Kafka can feel like black boxes when you’re first learning about them. By re-creating the core behavior with simple Python, I wanted to:
- Make the architecture **more approachable**
- Understand how **producers, brokers, and consumers** work together
- Show how even simple code can model **powerful ideas**

---

## Related Article

Read the full breakdown of this simulation and how it connects to Kafka on my [LinkedIn article](#) *(link coming soon!)*.

---

## 🛠️ Future Improvements (Optional Ideas)

- Support multiple consumers (consumer groups)
- Add persistence (save topics to disk)
- Add message timestamps or keys
- Build a web-based visualizer

