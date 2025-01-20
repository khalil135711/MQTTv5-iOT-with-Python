string broker = "your_broker_address";
int port = 8883; // Default port for MQTT over TLS/SSL
string clientId = Guid.NewGuid().ToString();
string topic = "your_topic_Name";
string username = "your_username";
string password = "your_password";

// Create a MQTT client factory
var factory = new MqttFactory();
// Create a MQTT client instance
var mqttClient = factory.CreateMqttClient();

// Create MQTT client options with TLS/SSL
var options = new MqttClientOptionsBuilder()
    .WithClientId(clientId)
    .WithTcpServer(broker, port)
    .WithCredentials(username, password)
    .WithTls()
    .Build();

// Connect to the broker
await mqttClient.ConnectAsync(options, CancellationToken.None);
