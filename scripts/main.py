#!/usr/bin/env python3
from typing import Text
import rospy
import tkinter as tk
from translate.srv import Str

class Translate():
    def __init__(self, window, langs):
        self.window = window
        self.langs = langs
        self.lang_label = [tk.Label(text='', anchor=tk.W) for i in langs]
        self.result = [tk.Label(text='', anchor=tk.W) for i in langs]
        self.pronounce = [tk.Button(self.window, text='再生', command=self.pron_btn_cb) for i in langs]
        self.translator = rospy.ServiceProxy('translate', Str)
        self.create_quit_btn()
        self.create_textbox()

    def create_quit_btn(self):
        x, y = 600, 400
        quit_btn = tk.Button(self.window, text='Quit')
        quit_btn['command'] = self.window.destroy
        quit_btn.place(x=x, y=y+40)
    
    def create_textbox(self):
        x, y = 150, 40
        label = tk.Label(text='Origin')
        label.place(x=x-60, y=y)
        self.txt = tk.Entry(width=50)
        self.txt.place(x=x, y=y)
        trans_btn = tk.Button(self.window, text='Translate', command=self.trans_btn_cb)
        trans_btn.place(x=x+410, y=y-4)
    
    def trans_btn_cb(self):
        i = 0
        adjuster = tk.Label(text='')
        adjuster.grid(row=0, column=0, padx = 30, pady = 30)
        rospy.loginfo(self.txt.get())
        for key, value in self.langs.items():
            txt = self.translator(f'{self.txt.get()}, {value}')
            self.lang_label[i]['text'] = key
            self.lang_label[i].grid(row = i+100, column = 3, padx = 2, pady = 2)
            self.result[i]['text'] = txt.strOut
            self.result[i].grid(row = i+100, column = 4, padx = 2, pady = 2)
            self.pronounce[i].grid(row = i+100, column = 5,padx = 2, pady = 2)
            i += 1
        print(self.txt.get())

        if self.txt.get().find('nvidia') != -1:
            nv = tk.Label(text='???')
            nv.grid(row=i+100, column=3, padx = 2, pady = 2)
            fy = tk.Button(text='再生')
            fy.grid(row=i+100, column=5, padx = 2, pady = 2)
    
    def pron_btn_cb(self):
        print(self.pronounce.index())
        

def main():
    rospy.init_node('main')
    wait_srv = ['translate']
    for srv in wait_srv:
        rospy.wait_for_service(srv)
    rospy.loginfo('finished waiting server')
    langs = {
        '日本語': 'ja', '英語': 'en', 'フランス語': 'fr', '中国語(簡体字)': 'zh-cn', 
        '中国語(繁体字)': 'zh-tw', 'イタリア語': 'it','韓国語': 'ko', 'ドイツ語': 'da',
        'ロシア語': 'ru', 'スペイン語': 'es', 
        }
    window = tk.Tk()
    window.geometry("750x500")
    translate = Translate(window=window, langs=langs)
    window.mainloop()

if __name__ == "__main__":
    if not rospy.is_shutdown():
        main()