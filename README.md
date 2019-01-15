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
* 別のターミナルを立ち上げ, ルンバに回転動作指令を送信
```
$ubuntu rostopic pub /cmd_vel geometry_msgs/Twist -r 60 -- '[0, 0, 0]' '[0, 0, 1.0]'
```

### 参考資料
https://karaage.hatenadiary.jp/entry/2017/05/12/073000


