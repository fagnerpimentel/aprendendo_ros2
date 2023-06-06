import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
from std_srvs.srv import Trigger
import json

class Checkpoints(Node):

    def __init__(self):
        super().__init__('checkpoints')
        self.goal_handle = None
        self._action_client = ActionClient(self, FollowWaypoints, '/follow_waypoints')
        self.srv_start = self.create_service(Trigger, '/start', self.start_callback)
        self.srv_cancel = self.create_service(Trigger, '/cancel', self.cancel_callback)
        self.declare_parameter('checkpoints_file', '')

    def start_callback(self, request, response):

        try:
            checkpoints_file = self.get_parameter('checkpoints_file').get_parameter_value().string_value

            f = open(checkpoints_file)
            data = json.load(f)

            poses = []
            for i in data['poses']:
                p = PoseStamped()
                p.header.frame_id = data['frame_id']
                p.pose.position.x = i['position']['x']
                p.pose.position.y = i['position']['y']
                p.pose.position.z = i['position']['z']
                p.pose.orientation.x = i['orientation']['x']
                p.pose.orientation.y = i['orientation']['y']
                p.pose.orientation.z = i['orientation']['z']
                p.pose.orientation.w = i['orientation']['w']
                poses.append(p)

            goal_msg = FollowWaypoints.Goal()
            goal_msg.poses = poses
            self._action_client.wait_for_server()
            self.goal_handle = self._action_client.send_goal_async(goal_msg)

            response.success = True
            response.message = "Success"
            return response
        except FileNotFoundError as e:
            self.get_logger().error (f"{e}")
            response.success = False
            response.message = f"{e}"
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