"""
Example IMU Control
Robo HAT MM1
https://github.com/wallarug/circuitpython_mpu9250
"""
import board
import busio
# from robohat_mpu9250.mpu9250 import MPU9250
from robohat_mpu9250.mpu6500 import MPU6500
# from robohat_mpu9250.ak8963 import AK8963

from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)

mpu = MPU6500(i2c, address=0x69)

# print("Reading in data from IMU.")

while True:
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*mpu.read_acceleration()))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*mpu.read_gyro()))
    print('Temperature: {0:0.3f}C'.format(mpu.read_temperature()))
    sleep(2)
