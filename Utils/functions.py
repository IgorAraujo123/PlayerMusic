from pygame import mixer
from Utils.ManipulateDate import Urls
import os

class Player():
    
    def __init__(self,playlist,DIRETORIO):
        self.url = Urls(playlist,DIRETORIO)
        self.musicInfo = self.url.loadMusicsInfo()
        self.playMusic = False
        self.index = 0

        mixer.init()

    def initMusic(self):
        mixer.music.load(self.musicInfo[0][0])
        mixer.music.play()
       
    def play(self):
        if self.playMusic:
            mixer.music.unpause()
            self.playMusic = False
        elif not self.playMusic:
            mixer.music.pause()
            self.playMusic = True

    def chageMusic(self):
        self.index += 1
        mixer.music.unload()
        mixer.music.load(self.musicInfo[self.index][0])
        mixer.music.play()
    
    def backMusic(self):
        self.index -= 1
        mixer.music.unload()
        mixer.music.load(self.musicInfo[self.index][0])
        mixer.music.play()
    
    def becomenMusic(self):
        self.index = 0
        mixer.music.unload()
        mixer.music.load(self.musicInfo[0][0])
        mixer.music.play()

    def closeMixer(self):
        mixer.quit()

    def getNameMusic(self):
        return self.musicInfo[self.index][1]
