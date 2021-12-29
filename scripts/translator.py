#!/usr/bin/env python3
import rospy
from gtts import gTTS
import googletrans
from translate.srv import Str, StrResponse
import os
import playsound

class Translator():
    def __init__(self):
        self.translator = googletrans.Translator()
        self.path = f'/home/{os.getlogin()}/catkin_ws/src/translate/pronounce/'

    #翻訳
    def translate(self, data):
        resp = StrResponse()
        sentence = data.strIn.split(', ')
        self.origin, self.lang = sentence[0], sentence[1]
        result = self.translator.translate(text=self.origin, src='ja', dest=self.lang)
        resp.strOut = result.text
        self.create_pronounce(text=result.text)
        return resp

    #音声ファイルの作成
    def create_pronounce(self, text):
        pronaunce = gTTS(text=text, lang=self.lang, slow=False)
        pronaunce.save(f'{self.path}{self.lang}.mp3')
    
    #音声の再生
    def play_sound(self, data):
        resp = StrResponse()
        playsound.playsound(f'{self.path}{data.strIn}.mp3')
        resp.strOut = 'completed'
        return resp

#メイン処理
def main():
    rospy.init_node('translator')
    translator = Translator()
    trans_srv = rospy.Service('translate', Str, translator.translate)
    sound_srv = rospy.Service('play_sound', Str, translator.play_sound)
    rospy.loginfo('translator server start')
    rospy.spin()

if __name__ == "__main__":
    if not rospy.is_shutdown():
        main()
