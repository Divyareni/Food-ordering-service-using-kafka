# StreamStore — Kafka-based Food Ordering Service Demo 🍽️

## Project Overview

This project simulates a simple food-ordering / e-commerce backend, built using Apache Kafka and Docker — where different parts of the system communicate asynchronously via Kafka topics.  
The goal is to demonstrate how an order placed by a user can trigger events (e.g. order-placed, notification sent, inventory updated) in a decoupled, scalable way.

## What You’ll Learn / What It Demonstrates

- Kafka fundamentals: brokers, topics, producers, consumers, asynchronous messaging. :contentReference[oaicite:1]{index=1}  
- How to containerize Kafka using Docker / Docker Compose, to easily spin up a local broker for testing. :contentReference[oaicite:2]{index=2}  
- Building a simple producer and consumer client (in Python) to publish and consume messages — simulating order handling, message flow, etc.  
- How “event-driven” microservice-style communication works: decoupling services so that producers don’t wait on consumers. :contentReference[oaicite:3]{index=3}  
- Basic project structure for a backend / messaging-based service, which can be extended later (e.g. more topics, richer message payloads, real database, REST API, etc.)

## Project Structure
StreamStore/
├── docker-compose.yaml # to launch Kafka broker (and Zookeeper if needed)
├── producer.py # example script that produces messages (e.g. new orders) to Kafka
├── tracker.py # example script / consumer that listens to orders and processes them
├── .gitignore
└── README.md # this file


> Note: `docker-compose.yaml` may start Kafka (and optionally Zookeeper) containers so that your Python scripts can connect to the broker at `localhost:9092`.

## Prerequisites

- Docker and Docker Compose installed on your system.  
- Python 3.x installed (if using the provided Python producer/consumer scripts).  
- (Optional) `kafka-python`, `confluent-kafka`, or whichever Python Kafka client library you are using — install via `pip install ...`  

## Setup & Usage

1. **Start Kafka broker via Docker**  
   ```bash
   docker-compose up -d
   This will spin up Kafka (and Zookeeper if configured) and expose the broker on localhost:9092.

2. **Produce messages (simulate orders)**
   python producer.py
   This script will send example “order” events to a Kafka topic (e.g. orders).

3. **Consume messages (process orders / do something)**
   python tracker.py
   This script listens to the Kafka topic(s) and prints / processes incoming events — simulating order processing, inventory update, etc.

Example Workflow

* User (or producer script) generates a new “order placed” event → published to Kafka topic.

* Consumer (tracker) picks up the order event asynchronously — e.g. logs the order, updates internal state, or triggers other services.

* Because of Kafka’s decoupled design, producer and consumer don’t block each other — enabling scalable, resilient event-driven architecture.

# Install dependencies
poetry install

# Run producer
poetry run python producer.py

# Run consumer
poetry run python tracker.py
