#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import board
import adafruit_ina260
import busio

#print("Current:", ina260.current)
#print("Voltage:", ina260.voltage)
#print("Power:", ina260.power)

class Ina260Publisher(Node):

    def __init__(self):
        super().__init__('ina260_publisher')
        self.publisher_ = self.create_publisher(String, 'voltage', 10)
        timer_period = 10  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ina260 = adafruit_ina260.INA260(i2c)

    def timer_callback(self):
        msg = String()
        msg2 = round(self.ina260.voltage, 2)
        msg.data = str(msg2)
        self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    ina260_publisher = Ina260Publisher()
    rclpy.spin(ina260_publisher)
    ina260_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

