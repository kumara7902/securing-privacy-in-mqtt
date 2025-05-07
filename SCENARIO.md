# Scenario: Privacy-Preserving Disaster Messaging System

## Context
In a disaster zone, victims send emergency messages using nearby drones acting as MQTT brokers. These messages are forwarded to a remote Command & Control center for response coordination.

## Goal
Ensure privacy of transmitted messages using privacy engineering techniques. Prevent adversaries from identifying, linking, or reading the content of the messages.

## System Architecture
- Victim device (publisher)
- MQTT broker (drone)
- Transient message queue
- C2 system (subscriber)
- Identity token store

## Privacy Threats (LINDDUN)
- Linkability: Same victim can be tracked by topic or ID
- Identifiability: Names or GPS data reveal identity
- Disclosure: Medical/emergency info is exposed
- Non-compliance: No encryption, consent, or access control

## PETs Implemented
1. **SHA-256 Pseudonymization** - replaces name with hashed ID
2. **AES Encryption (Fernet)** - encrypts entire message payload

## Metrics (Before vs After)

| Feature         | Without PETs | With PETs   |
|-----------------|--------------|-------------|
| ID Field        | Name         | Hashed ID   |
| Payload         | Plain JSON   | Encrypted   |
| Disclosure Risk | High         | Low         |
| Payload Size    | ~110 bytes   | ~245 bytes  |
| Latency         | ~10 ms       | ~15 ms      |

## How to Run
See README.md for full instructions on installing dependencies, launching the broker, and running the publisher and subscriber.

## Results
The PETs greatly improved privacy protection with minor performance trade-offs. All message content is protected in transit, and user identity is obfuscated consistently.
