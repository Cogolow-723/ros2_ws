import rclpy                       #ROS2のクライアントのためのライブラリ
from rclpy.node import Node        #ノードを実装するためのNodeクラス
from std_msgs.msg import Int16     #通信の型(16bitの符号付き関数)


def cb(msg):                     
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)              #実行(無限ループ)
