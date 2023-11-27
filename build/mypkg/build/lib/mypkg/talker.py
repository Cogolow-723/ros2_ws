import rclpy                       #ROS2のクライアントのためのライブラリ
from rclpy.node import Node        #ノードを実装するためのNodeクラス
from person_msgs.msg import Person #使う型を変更

rclpy.init()                                        
node = Node("talker")                               #ノード作成
pub = node.create_publisher(Person, "person", 10)   #パブリッシャのオブジェクト作成
n = 0                                               #カウント用変数

def cb():                     #17行目で定期実行されるコールバック関数
    global n                  #関数を抜けてもnがリセットされないようにする
    msg = Person()            #メッセージのオブジェクト
    msg.name = "毛利夏海"       #msgファイルに書いたname
    msg.age = 20              #msgファイルに書いたage
    pub.publish(msg)          #pubの持つpublishでメッセージを送信
    n += 1

node.create_timer(0.5, cb)    #タイマー設定
rclpy.spin(node)              #実行(無限ループ)
