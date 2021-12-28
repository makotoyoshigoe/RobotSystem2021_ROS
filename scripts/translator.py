#!/usr/bin/env python3
from typing import Text
import rospy
from gtts import gTTS
import googletrans
from translate.srv import Str, StrResponse
import os

class Translator():
    def __init__(self):
        self.translator = googletrans.Translator()
        self.path = '/home/'+os.getlogin()+'/catkin_ws/src/translate/pronounce/'

    #翻訳
    def translate(self, data):
        resp = StrResponse()
        sentence = data.strIn.split(', ')
        self.origin, self.lang = sentence[0], sentence[1]
        result = self.translator.translate(text=self.origin, src='ja', dest=self.lang)
        rospy.loginfo(result.text)
        resp.strOut = result.text
        self.create_pronounce(text=result.text)
        return resp

    #音声ファイルの作成
    def create_pronounce(self, text):
        pronaunce = gTTS(text=text, lang=self.lang, slow=False)
        pronaunce.save(f'{self.path}{self.lang}.mp3')

def main():
    rospy.init_node('translator')
    translator = Translator()
    trans_srv = rospy.Service('translate', Str, translator.translate)
    rospy.loginfo('translator server start')
    rospy.spin()

if __name__ == "__main__":
    if not rospy.is_shutdown():
        main()
