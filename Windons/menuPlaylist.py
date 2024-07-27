import os
import PySimpleGUI as sg
from Windons.playMusic import WindowPlayer

def iniLayoutPlaylist(Playlist):

    namesPlaylists = [[]]
    col = 0
    row = 0

    for valor in Playlist:
        if row >= 3:
            namesPlaylists.append([valor])
            col += 1
            row = 0
        else:
            namesPlaylists[col].append(valor)

        row += 1  
    
    layout =  [[sg.Column([
                [sg.Column(
                    [[sg.Image('D:\Projetos python\Player Music\Icones\Playlist.png')], [sg.Button(button_text= namesPlaylists[j][i])]],element_justification='c') for i in range(len(namesPlaylists[j]))
                ]for j in range(len(namesPlaylists))
                ], scrollable=True, size=(740,400))]
              ]
    
    return layout

class Window():

    def __init__(self, layout, DIRETORIO, ListPlaylists):
        self.window = sg.Window('Playlist', layout)
        self.playlist = ''
        self.ListPlaylists = ListPlaylists
        self.DIRETORIO = DIRETORIO
        self.isClosed = False

    def changeWindow(self):
        windowPlayer = WindowPlayer(self.playlist,self.DIRETORIO)
        windowPlayer.initWindow()

    def eventsWindow(self):

        while True:

            evento,values = self.window.read()

            if evento == sg.WIN_CLOSED:
                self.isClosed = True
                break
            if evento in self.ListPlaylists:
                self.playlist = evento
                break

        self.window.close()

        if not self.isClosed:
            self.changeWindow()

if __name__ == '__main__':
    iniLayoutPlaylist(os.listdir('C:/Users/igorb/OneDrive/Desktop/Playlist'))