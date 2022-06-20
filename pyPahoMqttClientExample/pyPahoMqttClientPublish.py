import time
import random
from paho.mqtt import client as PahoMqttClient


# 服务器地址
BROKER = "66.42.63.94"
# 服务器端口
PORT = 1883
# 订阅主题
TOPIC = "demo/1"
# 客户端编号
CLIENT_ID = f"LINE2-{random.randint(100000, 999999)}"


# 客户端
def MqttClient():
    # 连接回调
    def on_connect(client, userdata, flags, rc):
        print(f"On Connected: {str(rc)}")
        # 订阅主题
        client.subscribe(TOPIC)

    # 断开连接回调
    def on_disconnect(client, userdata, rc):
        print(f"On Disconnected: {str(rc)}")

    # 消息回调
    def on_message(client, userdata, message):
        print(f"On Messaged: {message.topic} {str(message.qos)} {str(message.payload)}")

    # 订阅回调
    def on_subscribe(client, userdata, mid, granted_qos):
        print(f"On Subscribed: {str(mid)} {str(granted_qos)}")

    # 取消订阅回调
    def on_unsubscribe(client, userdata, mid):
        print(f"On unSubscribed: {str(mid)}")

    # 发布消息回调
    def on_publish(client, userdata, mid):
        print(f"On Published: {str(mid)}")

    # 日志回调
    def on_log(client, userdata, level, buf):
        print(f"Log: {buf}")

    # 客户端
    client = PahoMqttClient.Client(CLIENT_ID)

    # 将回调函数指派给客户端实例
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscribe
    client.on_publish = on_publish
    client.on_log = on_log

    # 连接服务器
    client.connect(BROKER, PORT)

    # 返回客户端实例
    return client


# 发布消息
def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"message: {msg_count}"
        result = client.publish(TOPIC, msg)
        if result[0] == 0:
            print(f"Send {msg} to topic: {TOPIC}")
        else:
            print(f"Failed to Send to topic: {TOPIC}")
        msg_count += 1


# 运行程序
def run():
    # 客户端
    client = MqttClient()
    # 开始循环
    client.loop_start()
    # 发布消息
    publish(client)


# 程序入口
if __name__ == "__main__":
    run()
