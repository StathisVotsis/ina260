#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
#import time
#import board
#import adafruit_ina260


#i2c = board.I2C()
#ina260 = adafruit_ina260.INA260(i2c)
#while True:
    #print("Current: %.2f Voltage: %.2f Power:%.2f"
        #%(ina260.current, ina260.voltage, ina260.power))
    #time.sleep(1)

class Ina260Publisher(Node):

    def __init__(self):
        super().__init__('ina260_publisher')
        self.publisher_ = self.create_publisher(String, 'voltage', 10)
        timer_period = 10  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    ina260_publisher = Ina260Publisher()

    rclpy.spin(ina260_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ina260_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

