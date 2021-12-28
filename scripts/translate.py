import rospy
from gtts import gTTS
from googletrans import Translator
from translate.srv import Str, StrResponse

class Translator():
    def __init__(self):
        pass


    def translate(self, data):
        resp = StrResponse()
        self.origin = data.strIn

        pass

    def create_pronounce(self):
        pass

def main():
    rospy.init_node('translator')
    translator = Translator()
    trans_srv = rospy.Service('translate', Str, translator.translate())
