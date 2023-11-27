import rclpy                       #ROS2のクライアントのためのライブラリ
from rclpy.node import Node        #ノードを実装するためのNodeクラス
from person_msgs.msg import Person     #通信の型(16bitの符号付き関数)


def cb(msg):                     
    global node
    node.get_logger().info("Listen: %s" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "person", cb, 10)

rclpy.spin(node)              #実行(無限ループ)
