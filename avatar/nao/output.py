import requests
import json

class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def out(data):
        self.tts.say(data)

    def onLoad(self):
        self.tts = ALProxy('ALTextToSpeech')
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        url = "http://jsonplaceholder.typicode.com/posts/1"
        res = requests.get(url)

        if(res.ok):
            jsonData = json.loads(res.content)
            self.tts.say(str(jsonData['id']))
        else:
            self.tts.say("error")
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box
