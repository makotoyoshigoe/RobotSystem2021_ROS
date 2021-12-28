#!/usr/bin/env python3
import rospy
import tkinter as tk
from translate.srv import Str

class Translate():
    def __init__(self, window, langs):
        self.window = window
        self.langs = langs
        self.create_quit_btn()
        self.create_textbox()

    def create_quit_btn(self):
        x, y = 600, 400
        quit_btn = tk.Button(self.window, text='Quit')
        quit_btn['command'] = self.window.destroy
        quit_btn.place(x=x, y=y+40)
    
    def create_textbox(self):
        x, y = 150, 100
        label = tk.Label(text='Origin')
        label.place(x=x-60, y=y)
        self.txt = tk.Entry(width=50)
        self.txt.place(x=x, y=y)

        trans_btn = tk.Button(self.window, text='Translate', command=self.trans_btn_cb)
        trans_btn.place(x=x+410, y=y-4)
    
    def trans_btn_cb(self):
        x, y = 350, 200
        i = 0
        for key, value in self.langs.items():
            label = tk.Label(text=key)
            label.place(x=x-50, y=y+30*i)
            result = tk.Label(text=f'{self.txt.get()}')
            result.place(x=x, y=y+30*i)
            i += 1

def main():
    rospy.init_node('translate')
    wait_srv = []
    for srv in wait_srv:
        rospy.wait_for_service(srv)
    rospy.loginfo('finished waiting server')
    langs = {'日本語': 'ja', '英語': 'en', '中国語': 'ch', 'フランス語': 'fr', }
    window = tk.Tk()
    window.geometry("750x500")
    translate = Translate(window=window, langs=langs)
    window.mainloop()

if __name__ == "__main__":
    if not rospy.is_shutdown():
        main()