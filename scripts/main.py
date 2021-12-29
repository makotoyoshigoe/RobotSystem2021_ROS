#!/usr/bin/env python3
import rospy
import tkinter as tk
from translate.srv import Str

class Translate():
    def __init__(self, window, langs):
        self.window = window
        self.langs = langs
        self.lang_label = [tk.Label(text='', anchor=tk.W) for i in langs]
        self.result = [tk.Label(text='', anchor=tk.W) for i in langs]
        self.nv1 = tk.Label()
        self.nv2 = tk.Label()
        self.pronounce = [tk.Button(self.window, text=f'{key}再生') for key, value in langs.items()]
        self.play_sound = rospy.ServiceProxy('play_sound', Str)
        self.translator = rospy.ServiceProxy('translate', Str)
        self.create_quit_btn()
        self.create_textbox()

    #終了ボタン作成
    def create_quit_btn(self):
        x, y = 600, 400
        quit_btn = tk.Button(self.window, text='Quit')
        quit_btn['command'] = self.window.destroy
        quit_btn.place(x=x, y=y+40)
    
    #テキストボックス作成
    def create_textbox(self):
        x, y = 150, 40
        label = tk.Label(text='Origin')
        label.place(x=x-60, y=y)
        self.txt = tk.Entry(width=50)
        self.txt.place(x=x, y=y)
        trans_btn = tk.Button(self.window, text='Translate', command=self.trans_btn_cb)
        trans_btn.place(x=x+410, y=y-4)
    
    #翻訳ボタンが押されたときの動作
    def trans_btn_cb(self):
        i = 0
        adjuster = tk.Label(text='')
        adjuster.grid(row=0, column=0, padx = 41, pady = 30)
        rospy.loginfo('translating...')
        for key, value in self.langs.items():
            txt = self.translator(f'{self.txt.get()}, {value}') #翻訳された文を受け取る
            #言語を表示
            self.lang_label[i]['text'] = key
            self.lang_label[i].grid(row = i+100, column = 3, padx = 2, pady = 2, sticky=tk.W)
            #翻訳した文を表示
            self.result[i]['text'] = txt.strOut
            self.result[i].grid(row = i+100, column = 4, padx = 2, pady = 2, sticky=tk.W)
            #再生ボタン作成
            self.pronounce[i].grid(row = i+100, column = 5,padx = 2, pady = 2, sticky=tk.W)
            self.pronounce[i].bind("<ButtonPress>", self.pron_btn_cb)
            i += 1
        
        self.nv1['text'] = ''
        self.nv2['text'] = ''
        if self.txt.get().find('nvidia') != -1:
            self.nv1['text'] = '???'
            self.nv2['text'] = 'Nvidia F○ck You.'
        self.nv1.grid(row = i+100, column = 3, padx = 2, pady = 2, sticky=tk.W)
        self.nv2.grid(row = i+100, column = 4, padx = 2, pady = 2, sticky=tk.W)
        rospy.loginfo('finished')
    
    #再生ボタンが押されたときの動作
    def pron_btn_cb(self, event):
        lang = event.widget.cget("text").replace('再生', '') #音声を再生するサーバーに指示を出す
        result = self.play_sound(self.langs[lang])

#メイン処理
def main():
    rospy.init_node('main')
    wait_srv = ['translate', 'play_sound']
    for srv in wait_srv:
        rospy.wait_for_service(srv)
    rospy.loginfo('finished waiting for server')
    langs = {
        '日本語': 'ja', '英語': 'en', '中国語(簡体字)': 'zh-cn', '中国語(繁体字)': 'zh-tw', '韓国語': 'ko', 
        'ロシア語': 'ru', 'ドイツ語': 'da', 'フランス語': 'fr', 'イタリア語': 'it', 'スペイン語': 'es', 
        }
    window = tk.Tk()
    window.geometry("750x500")
    translate = Translate(window=window, langs=langs)
    window.mainloop()

if __name__ == "__main__":
    if not rospy.is_shutdown():
        main()