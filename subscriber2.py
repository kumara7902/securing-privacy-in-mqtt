import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet
import json

# MQTT Setup
broker = "localhost"
port = 1883
topic = "calamity/help"

# Load the same encryption key as used by publisher
with open("aes.key", "rb") as f:
    key = f.read()
cipher = Fernet(key)

# Define callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    try:
        decrypted_payload = cipher.decrypt(msg.payload).decode()
        data = json.loads(decrypted_payload)
        print(f"[RECEIVED] ID: {data['id']} | Location: {data['location']} | Message: {data['message']}")
    except Exception as e:
        print(f"[ERROR] Decryption failed: {e}")

# Create and run client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)
client.loop_forever()
