import paho.mqtt.client as mqtt
####
# Bitte vor dem scripts zu bedarfen , Einstellen Sie ihre MQTT Brocker !  
# Brocker details
BROKER = "127.0.0.1"  # Brocker ip@
PORT = 1883           # Brocker default port
TOPIC = "hello/topic_without_Auth"  
client = mqtt.Client(protocol=mqtt.MQTTv5)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to broker")
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

# Callback for when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: '{msg.payload.decode()}' on topic '{msg.topic}'")

# Callback for when a message is published
def on_publish(client, userdata, mid):
    print(f"Message {mid} published successfully")

# Initialize the MQTT client with the latest protocol version
client = mqtt.Client(protocol=mqtt.MQTTv311)

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

# Connect to the broker
try:
    client.connect(BROKER, PORT, 60)
except Exception as e:
    print(f"Error connecting to broker: {e}")
    exit(1)

# Publish a test message
client.loop_start()  # Start a loop in a separate thread
client.publish(TOPIC, "Hello, MQTT Broker v5!")

# Keep the script running to listen for messages
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nDisconnecting from broker...")
    client.loop_stop()
    client.disconnect()
