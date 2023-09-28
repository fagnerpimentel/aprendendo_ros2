import time
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

from rclpy.qos import QoSProfile, QoSReliabilityPolicy

class R2D2(Node):

    def __init__(self):
        super().__init__('R2D2')
        qos_profile = QoSProfile(depth=10, reliability = QoSReliabilityPolicy.BEST_EFFORT)

        self.laser = None
        self.create_subscription(LaserScan, '/scan', self.listener_callback_laser, qos_profile)

        self.pose = None
        self.create_subscription(Odometry, '/odom', self.listener_callback_odom, qos_profile)

        self.pub_cmd_vel = self.create_publisher(Twist, '/cmd_vel', 10)

    def wait(self, max_seconds):
        start = time.time()
        count = 0
        while count < max_seconds:
            count = time.time() - start            
            rclpy.spin_once(self)

    def listener_callback_laser(self, msg):
        self.laser = msg.ranges
        # self.get_logger().info(str(self.ranges))
        
    def listener_callback_odom(self, msg):
        self.pose = msg.pose.pose
        # self.get_logger().info(str(self.pose))

    def navigation(self):
        try:
            rclpy.spin_once(self)
            self.navigation_start()
            while(rclpy.ok):
                rclpy.spin_once(self)
                self.navigation_update()
        except (KeyboardInterrupt):
            pass

    def navigation_start(self):
        raise NotImplementedError()

    def navigation_update(self):
        raise NotImplementedError()
