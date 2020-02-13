import paho.mqtt.publish as publish

publish.single("armtronix_mqtt", "payload", hostname="192.168.10.233")