# MQTT Privacy Simulation Project

This repository contains the source code and supporting files for the final project titled:
**"Securing Privacy in MQTT-Based Systems Using PETs and LINDDUN"**

---

## 📌 Overview
This project simulates a real-world emergency communication system using MQTT. Victims send distress messages through drones (acting as MQTT brokers) to a Command & Control system. We identify privacy risks using the LINDDUN framework and apply privacy-enhancing technologies (PETs) to mitigate them.

---

## 🧩 System Components
- `publisher.py`: Simulates the victim publishing encrypted messages
- `subscriber.py`: Simulates the C2 system decrypting and reading messages
- `mosquitto.conf`: Custom MQTT broker configuration file (optional)
- `aes.key`: Symmetric encryption key used by both publisher and subscriber
- `Stage4_Evaluation_and_Documentation.pptx`: Final slide deck used in the YouTube video

---

## ⚙️ Tools & Libraries
- **Language**: Python 3.8+
- **Broker**: [Mosquitto MQTT](https://mosquitto.org/)
- **Libraries**:
  - `paho-mqtt`: MQTT client for Python
  - `cryptography`: AES encryption/decryption (Fernet)
  - `hashlib`: Used for SHA-256 pseudonymization

### 🔧 Installation
```bash
pip install paho-mqtt cryptography
```
Install Mosquitto:
```bash
sudo apt install mosquitto mosquitto-clients
```
Run the broker:
```bash
mosquitto
```

---

## 🛰️ MQTT Broker Configuration and Setup

### Default Usage
To start the broker with default settings:
```bash
mosquitto
```
This launches the broker on `localhost:1883` and only accepts local connections.

### Optional: Custom Configuration
Use this `mosquitto.conf` file to customize:
```conf
listener 1883
allow_anonymous true
persistence false
```
Run it with:
```bash
mosquitto -c mosquitto.conf
```

---

### 🧪 Testing the Simulation
1. Open one terminal:
```bash
python subscriber.py
```
2. Open another terminal:
```bash
python publisher.py
```

### 🧠 Interpreting Results
- Subscriber prints the decrypted message
- AES-encrypted messages are unreadable in transit
- Pseudonymized ID replaces real identity

---

## 📊 Results Summary
| Feature            | Without PETs | With PETs     |
|--------------------|---------------|----------------|
| ID Field          | "Alice"       | SHA-256 hash   |
| Message Visibility| Plain JSON    | Encrypted      |
| Risk Level        | High          | Low            |
| Message Size      | ~110 bytes    | ~245 bytes     |
| Latency           | ~10 ms        | ~15 ms         |

---

## 📂 LICENSE
This project is open-source under the **MIT License**.

---

## 🎥 YouTube Presentation
Watch the full 45-minute walkthrough explaining the system, threat model, PET implementation, and performance analysis:
📺 [Youtube Link](https://www.youtube.com/watch?v=Gru2X0hAaNY)

---

For questions or suggestions, feel free to open an issue or contact me through GitHub.
