import os

class Urls():

    def __init__(self,playlist,DIRETORIO):

        self.DIRETORIO_MUSICAS = DIRETORIO + '/' + playlist + '/Musics'
        self.musicInfo = []

    def loadMusicsInfo(self): 

        for valor in os.listdir(self.DIRETORIO_MUSICAS):
            self.musicInfo.append([self.DIRETORIO_MUSICAS + '/' + valor, valor.replace('.mp3','')])
        
        return self.musicInfo
    

