import rclpy                       #ROS2のクライアントのためのライブラリ
from rclpy.node import Node        #ノードを実装するためのNodeクラス
from std_msgs.msg import Int16     #通信の型(16bitの符号付き関数)

rclpy.init()                                        
node = Node("talker")                               #ノード作成
pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャのオブジェクト作成
n = 0                                               #カウント用変数

def cb():                     #17行目で定期実行されるコールバック関数
    global n                  #関数を抜けてもnがリセットされないようにする
    msg = Int16()             #メッセージのオブジェクト
    msg.data = n              #msgオブジェクトの持つdataにnを結び付ける
    pub.publish(msg)          #pubの持つpublishでメッセージを送信
    n += 1

node.create_timer(0.5, cb)    #タイマー設定
rclpy.spin(node)              #実行(無限ループ)
