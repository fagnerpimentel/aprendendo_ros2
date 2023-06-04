import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
from std_srvs.srv import Trigger

class Checkpoints(Node):

    def __init__(self):
        super().__init__('checkpoints')
        self.goal_handle = None
        self._action_client = ActionClient(self, FollowWaypoints, '/follow_waypoints')
        self.srv_start = self.create_service(Trigger, '/start', self.start_callback)
        self.srv_cancel = self.create_service(Trigger, '/cancel', self.cancel_callback)
    
    def start_callback(self, request, response):
        poses = []

        p1 = PoseStamped()
        # p1.header.seq = 0
        # p1.header.stamp = 0
        p1.header.frame_id = 'map'
        p1.pose.position.x = 1.5
        p1.pose.position.y = 0.5
        p1.pose.position.z = 0.0
        p1.pose.orientation.x = 0.0 
        p1.pose.orientation.y = 0.0
        p1.pose.orientation.z = 0.0
        p1.pose.orientation.w = 1.0
        poses.append(p1)

        p2 = PoseStamped()
        # p2.header.seq = 0
        # p2.header.stamp = 0
        p2.header.frame_id = 'map'
        p2.pose.position.x = 4.0
        p2.pose.position.y = -4.0
        p2.pose.position.z  = 0.0
        p2.pose.orientation.x = 0.0 
        p2.pose.orientation.y = 0.0
        p2.pose.orientation.z = 0.0
        p2.pose.orientation.w = 1.0
        poses.append(p2)

        p3 = PoseStamped()
        # p3.header.seq = 0
        # p3.header.stamp = 0
        p3.header.frame_id = 'map'
        p3.pose.position.x = -3.0
        p3.pose.position.y = -4.0
        p3.pose.position.z = 0.0 
        p3.pose.orientation.x = 0.0 
        p3.pose.orientation.y = 0.0
        p3.pose.orientation.z = 0.0
        p3.pose.orientation.w = 1.0
        poses.append(p3)

        p4 = PoseStamped()
        # p4.header.seq = 0
        # p4.header.stamp = 0
        p4.header.frame_id = 'map'
        p4.pose.position.x = -4.0
        p4.pose.position.y = 4.0
        p4.pose.position.z = 0.0
        p4.pose.orientation.x = 0.0 
        p4.pose.orientation.y = 0.0
        p4.pose.orientation.z = 0.0
        p4.pose.orientation.w = 1.0
        poses.append(p4)

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = poses
        self._action_client.wait_for_server()
        self.goal_handle = self._action_client.send_goal_async(goal_msg)

        response.success = True
        response.message = "Success"
        return response

    def cancel_callback(self, request, response):
        self.goal_handle.result().cancel_goal_async()

        response.success = True
        response.message = "Success"
        return response

def main(args=None):
    rclpy.init(args=args)

    action_client = Checkpoints()
    rclpy.spin(action_client)



if __name__ == '__main__':
    main()