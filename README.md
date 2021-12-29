# RobotSystem2021_ROS
テキストボックスに日本語を入力して翻訳ボタンを押すと、いくつかの言語で翻訳された文章が表示されます. また, 再生ボタンを押すことで、その言語で文章を読んだ音声が再生されます. 

---

## 動作環境
- Ubuntu 20.04.3 LTS Desktop
- ROS Noetic
- Python 3.8.10
- tkinter 8.6
- gTTs 2.2.3
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
- 上記のコマンドを実行すると, 下の画像のようなウィンドウが表示されます. 
![Screenshot 2021-12-29 02:56:48](https://user-images.githubusercontent.com/91446273/147593977-87850b5a-146f-4d64-9398-6d33f0b124d3.png)

- テキストボックスに適当な日本語の文章を入力します. 
![Screenshot 2021-12-29 03:06:34](https://user-images.githubusercontent.com/91446273/147594484-92255adb-83c4-4251-9660-f546bc3f9ae6.png)

- Translateボタンを押すと, 入力した日本語の文章がいくつかの言語に翻訳されて表示されます. 
![Screenshot 2021-12-29 03:46:15](https://user-images.githubusercontent.com/91446273/147597337-ee40cf59-1b06-4859-912e-fa25df9737d5.png)

- 文章の隣りにある〇〇語再生というボタンをクリックすると, 〇〇語で文章を読んでくれます. 

---

### 終了
- 画面右下にあるQuitボタンを押すと, ウィンドウが閉じ, 終了します.

---

## 実際に動かしている様子
- YouTube: 

---

## ライセンス
- This repository is licensed under the BSD license.
- gTTs: [MIT License](https://github.com/pndurette/gTTS/blob/master/LICENSE)
- googletrans: [MIT License](https://github.com/ssut/py-googletrans/blob/master/LICENSE)
- playsound: [MIT License](https://github.com/TaylorSMarks/playsound/blob/master/LICENSE)
