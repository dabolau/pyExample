import serial

# 串口名称
PORT = "/dev/ttys008"
# 波特率
BAUDRATE = 9600
# 超时时间
TIMEOUT = 1

# 程序入口
if __name__ == "__main__":
    # 实例化串口
    ser = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
    # 读取数据
    while True:
        data = ser.read_all()
        if data != bytes(b''):
            print(data)
