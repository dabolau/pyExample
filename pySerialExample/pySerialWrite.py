import serial

# 串口名称
PORT = "/dev/ttys009"
# 波特率
BAUDRATE = 9600
# 超时时间
TIMEOUT = 1

# 程序入口
if __name__ == "__main__":
    # 实例化串口
    ser = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
    # 写入数据
    while True:
        data = bytes(input("请输入要发送的数据："), encoding="utf-8")
        ser.write(data)
        print(data)
