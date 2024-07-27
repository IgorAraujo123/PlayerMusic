import PySimpleGUI as sg
from Windons import menuPlaylist
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno, showinfo
from tkinter.simpledialog import askstring
import os

DIRETORIO_PLAYLISTS = askdirectory(title='Select Past Playlist')
Playlists = os.listdir(DIRETORIO_PLAYLISTS)

if len(Playlists) > 0:
    layout = menuPlaylist.iniLayoutPlaylist(Playlists)

    windowClass = menuPlaylist.Window(layout,DIRETORIO_PLAYLISTS,Playlists)
    windowClass.eventsWindow()

else:
    if askyesno('Warning', 'Não possui nenhuma playlist, Deseja criar uma nova?'):
        nome_playlist = askstring(title='Playlist', prompt= 'Coloque o nome da playlist')
        patch_playlist = DIRETORIO_PLAYLISTS + '/' + nome_playlist
        os.mkdir(patch_playlist)
        os.mkdir(patch_playlist + '\\Musics')

        Playlists.append(nome_playlist)

        layout = menuPlaylist.iniLayoutPlaylist(Playlists)

        windowClass = menuPlaylist.Window(layout,DIRETORIO_PLAYLISTS,Playlists)
        windowClass.eventsWindow()
    else:
        showinfo('Saindo', 'Saindo do programa')
