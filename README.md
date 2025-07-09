# MQTT Setup with SSL and Bridging

This repository provides a complete setup guide for configuring Eclipse Mosquitto with SSL/TLS encryption and MQTT bridging on a virtual machine.

## Features

MQTT broker setup using Eclipse Mosquitto.
Secure communication using SSL/TLS.
Bridging configuration to connect two MQTT brokers.
Scripts for automation and testing.

## Requirements

A Linux-based virtual machine (Ubuntu recommended).
Root or sudo access to configure services.
OpenSSL installed (sudo apt install openssl).
## Setup Instructions

### 1. Clone the Repository

$ git clone https://github.com/your-username/mqtt-setup.git
$ cd mqtt-setup
### 2. Install Mosquitto
Run the installation script to set up Mosquitto and its clients:
$ sudo bash scripts/install-mosquitto.sh

### 3. Generate SSL Certificates
Run the certificate generation script:
$ sudo bash certs/generate-certs.sh

This will generate:

 * ca.crt: Certificate Authority file.
 * server.crt: Server certificate.
 * server.key: Server private key.
These will be stored in /etc/mosquitto/certs/

### 4. Configure Mosquitto
SSL Configuration

Edit the config/mosquitto.conf file to enable SSL:

listener 8883
cafile /etc/mosquitto/certs/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
require_certificate false

Copy the configuration to /etc/mosquitto/mosquitto.conf:

$ sudo cp config/mosquitto.conf /etc/mosquitto/mosquitto.conf

### Restart Mosquitto:

$ sudo systemctl restart mosquitto
### Bridging Configuration

Edit the config/bridge.conf file to set up a bridge:

# Bridge to external MQTT broker
connection my_bridge
address <REMOTE_BROKER_IP>:1883

topic # out 0
topic # in  0

try_private false
cleansession true

#Authentication (optional)
#remote_username <REMOTE_BROKER_USERNAME>
#remote_password <REMOTE_BROKER_PASSWORD>

Copy the bridging configuration:
$ sudo cp config/bridge.conf /etc/mosquitto/conf.d/bridge.conf

Restart Mosquitto:
$ sudo systemctl restart mosquitto

### 5. Test the Configuration
#### Publish a Message: 
$ mosquitto_pub -h localhost -t test/topic -m "Hello, MQTT!" --cafile /etc/mosquitto/certs/ca.crt -p 8883
#### Subscribe to the Topic
$ mosquitto_sub -h localhost -t test/topic --cafile /etc/mosquitto/certs/ca.crt -p 8883

### Test the Bridge

Publish a message to the local broker:
$ mosquitto_pub -h localhost -t bridge/test -m "Bridge Test Message" -u your_username -P your_password

Check the message on the remote broker:
$ mosquitto_sub -h <REMOTE_BROKER_IP> -t bridge/test -u <REMOTE_BROKER_USERNAME> -P <REMOTE_BROKER_PASSWORD>

# Firewall Configuration

Open the necessary ports for MQTT:

$ sudo ufw allow 1883

$ sudo ufw allow 8883

# Logs and Debugging

Enable verbose logging in Mosquitto by adding the following to /etc/mosquitto/mosquitto.conf:

$ log_type all

$ connection_messages true

$ log_dest file /var/log/mosquitto/mosquitto.log

Check logs for troubleshooting:
$ sudo tail -f /var/log/mosquitto/mosquitto.log

# Credits

- Eclipse Mosquitto: https://mosquitto.org/
- OpenSSL for certificate generation.



