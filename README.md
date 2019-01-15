# ロボットシステム学
## robosys2019　課題2 16C1015 井村 彩聖
### 課題2 内容
ルンバ500seriesをROS化する.

* 動画: https://youtu.be/vqtoQXvw28A

###ROSパッケージを追加
* ルンバのROSパッケージのリポジトリをクローン
```
$ubuntu $ cd ~/catkin_ws/src
$ubuntu $ git clone https://github.com/AutonomyLab/create_autonomy.git
```

###　動作方法
* ルンバのバッテリの確認
```
$ubuntu roslaunch ca_driver create_2.launch
```
* 別のターミナルを立ち上げ, ルンバにturn.pyを実行
```

  # left turn
    print "Turning the robot left."
    twist = Twist();
    twist.angular.z = 1.0
    pub.publish(twist)
```

### 参考資料
https://karaage.hatenadiary.jp/entry/2017/05/12/073000


