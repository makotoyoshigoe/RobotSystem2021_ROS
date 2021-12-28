# RobotSystem2021_ROS
テキストボックスに日本語を入力して翻訳ボタンを押すと、いくつかの言語で翻訳された文章が表示されます. また, 再生ボタンを押すことで、その言語で文章を読んだ音声が再生されます. 

---

## 動作環境
- Ubuntu 20.04.3 LTS Desktop
- ROS Noetic
- Python 3.8.10
- tkinter 8.6
- gtts 2.2.3
- googletrans 4.0.0-rc.1
- pysound 1.3.0

---

## 実行方法
### セットアップ
#### ROSのインストール~ワークスペースの作成
ROSのインストールからワークスペースの作成は, ryuichiueda様が作成された[こちら](https://cit.manaba.jp/ct/link_iframe_balloon?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DPL85Pw_zQH0)の動画を参考に行いました. 
```sh
cd ~/catkin_ws/src/
git clone git@github.com:makotoyoshigoe/RobotSystem2021_ROS.git
```
