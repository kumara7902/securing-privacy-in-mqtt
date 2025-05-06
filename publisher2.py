import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet
import hashlib
import json
import time

# MQTT Setup
broker = "localhost"
port = 1883
topic = "calamity/help"
client = mqtt.Client()
client.connect(broker, port)

# Generate or load encryption key
# Generate once and reuse for consistent testing
key = Fernet.generate_key()
cipher = Fernet(key)

# Save key so subscriber can use it
with open("aes.key", "wb") as f:
    f.write(key)

# Pseudonymization using SHA-256
real_name = "Alice"
salt = "CalamityDroneProject2025"
hashed_id = hashlib.sha256((salt + real_name).encode()).hexdigest()

# Payload to send
victim_data = {
    "id": hashed_id,
    "location": "Zone 3",
    "message": "Need water and medical aid"
}

# Main loop to publish repeatedly
while True:
    json_payload = json.dumps(victim_data)
    encrypted_payload = cipher.encrypt(json_payload.encode())
    client.publish(topic, encrypted_payload)
    print("Published encrypted message.")
    time.sleep(5)
