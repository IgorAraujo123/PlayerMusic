import PySimpleGUI as sg
from tkinter.messagebox import showerror
import os
from Utils.functions import Player

def iniLayoutMusic():
    layout = [
        [sg.Image('Tela_Inicial.png')],
        [sg.Text(text='Musica',key='-NameMusic-', font=25, justification='left',text_color='black', background_color='white',pad=((5,0),(20,10)))],
        [sg.Button(image_filename='D:/Projetos python/Player Music/Icones/back-arrow.png',key='Back',button_color='gray',visible=False),
        sg.Button(image_filename='D:/Projetos python/Player Music/Icones/botao-play.png', key='Play',button_color='gray',visible=False,pad=(15,10)),
        sg.Button(image_filename='D:/Projetos python/Player Music/Icones/avanco-rapido.png', key='Next',button_color='gray',visible=False),
        sg.Button('Start Song', key='-InitMusic-')]
    ]

    return layout

class WindowPlayer():
    def __init__(self,playlist,DIRETORIO):
        self.player = Player(playlist,DIRETORIO)
        self.playlist = playlist
        self.DIRETORIO = DIRETORIO
        self.window = sg.Window(title= self.playlist, layout=iniLayoutMusic(),background_color='white')

    def eventNextMusic(self):
        self.player.chageMusic()
        self.window['-NameMusic-'].update(self.player.getNameMusic())


    def eventBackMusic(self):
        try:
            self.player.backMusic()
            self.window['-NameMusic-'].update(self.player.getNameMusic())
        except:
            self.player.becomenMusic()

    def eventPlayMusic(self):
        self.player.play()

    def eventInitMusic(self):
        if len(os.listdir(self.DIRETORIO + '/' + self.playlist + '/Musics')) > 0:
            self.player.initMusic()
            self.window['-NameMusic-'].update(self.player.getNameMusic())
            self.window['-InitMusic-'].update(visible=False)
            self.window['Back'].update(visible=True)
            self.window['Play'].update(visible=True)
            self.window['Next'].update(visible=True)
        else:
            showerror('Error', 'Nenhum musica encontrada na playlist')


    def initWindow(self):
        while True:
            events,values = self.window.read()

            if events == sg.WIN_CLOSED:
                break
            elif events == '-InitMusic-':
                self.eventInitMusic()
            elif events == 'Play':
                self.eventPlayMusic()
            elif events == 'Back':
                self.eventBackMusic()
            else:
                self.eventNextMusic()

        self.window.close()
        self.player.closeMixer()
            

