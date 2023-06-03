import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from nav2_msgs.action import NavigateThroughtPoses


class NavigateThroughtPosesClient(Node):

    def __init__(self):
        super().__init__('pasando por poses')
        self._action_client = ActionClient(self, NavigateThroughtPoses, 'navigate_throught_poses')

    def send_goal(self, poses):
        goal_msg = NavigateThroughtPoses.Goal()
        goal_msg.poses = poses

        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = NavigateThroughtPosesClient()

    future = action_client.send_goal([])

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()