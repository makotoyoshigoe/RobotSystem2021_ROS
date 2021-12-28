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
- playsound 1.3.0

---

## 実行方法
### セットアップ
#### ROSのインストール~ワークスペースの作成
ROSのインストールからワークスペースの作成は, ryuichiueda様が作成された[こちら](https://www.youtube.com/watch?v=PL85Pw_zQH0)の動画を参考に行いました. 
#### 使用するモジュールのインストール
インストールされていないモジュールがありましたら, 以下のコマンドで必要なものを実行してください. 
```sh
sudo apt install python3-pip
sudo apt install python3-tk
pip install gtts
pip install googletrans==4.0.0-rc1
pip install playsound
```
#### リポジトリのクローン
```sh
cd ~/catkin_ws/src/
git clone git@github.com:makotoyoshigoe/RobotSystem2021_ROS.git
```

---

### 実行
- 端末1
```sh
roscore
```

- 端末2
```sh
roslaunch translate translate.launch
```
上記のコマンドを実行すると, 下の画像のようなウィンドウが表示されます. 
