import paho.mqtt.client as mqtt
import time
import json

broker = "localhost"
port = 1883
topic = "calamity/help"

client = mqtt.Client()
client.connect(broker, port)

victim_data = {
    "name": "Alice",
    "location": "Zone 3",
    "message": "Need water and medical aid"
}

while True:
    payload = json.dumps(victim_data)
    client.publish(topic, payload)
    print(f"Published: {payload}")
    time.sleep(5)
