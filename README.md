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

### ルンバで音楽を演奏♪
* iRobot roomba 500 Open Interface Specificationを参考に製作
```
code:140 >> 16小節からなる曲を登録可能
code:141　>>　登録した曲を別途演奏
```
* ターミナルでmusic.pyを実行
```
$ubuntu chmod +x music.py
$ubuntu python music.py
```
### 参考資料
https://karaage.hatenadiary.jp/entry/2017/05/12/073000


