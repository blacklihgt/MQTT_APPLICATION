import json
import random
import time
import paho.mqtt.publish as publish

# Define the topic to publish to
topic = "firstevertopic"

# Define the broker address and port
broker_address = '127.0.0.1'
broker_port = 9001

# Define the number of messages to publish
num_messages = 10

# Generate and publish the messages
for i in range(num_messages):
    # Generate a random integer value
    value = random.randint(0, 100)

    # Generate the timestamp
    timestamp = int(time.time())

    # Create the JSON payload
    payload = {
        "timestamp": timestamp,
        "value": value
    }

    # Convert the payload to a JSON string
    payload_str = json.dumps(payload)

    # Publish the message
    publish.single(topic, payload_str, hostname='127.0.0.1', port=9001)

    # Sleep for a random amount of time (between 1 and 5 seconds) before publishing the next message
    time.sleep(random.uniform(1, 5))

print(f"Published {num_messages} messages to topic {topic}")
