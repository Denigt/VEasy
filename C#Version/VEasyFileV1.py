from subprocess import *
import sys                                                                                                              #|
from os import mkdir                                                                                                    #|    Nombres de variables tkinter
from os import remove                                                                                                   #|      LA -> Label
from os import getcwd                                                                                                   #|      TX -> Entry
from os import listdir                                                                                                  #|      F --> Frame
from shutil import rmtree                                                                                               #|      B --> Button
from os.path import exists                                                                                              #|      CB -> Checkbutton
from os.path import isfile                                                                                              #|      OM -> OptionMenu
from os.path import isdir

#-- VARIABLES Y NOMBRES BASICOS -----------------------------------------------------------------------------------
#   Nombres de programas
nameYtdl = 'Downloader.exe'
#   Directorios
dirIni = getcwd()
dirFfmpeg = 'Third\\Converter\\bin\\ffmpeg.exe'
dirYtdl = 'Third\\Downloader.exe'
dirIn = 'in.fpy'
dirOut = 'out.fpy'
#   Formatos aceptados
forVideo = ['ORIGINAL','MP4','AVI','OGG','FLV','MKV','WEBM', 'AMV']
forAudio = ['ORIGINAL','MP3','WAV','BEST','M4A','AAC','FLAC', 'WMA']

#-- METODOS -------------------------------------------------------------------------------------------------------
# Actualizar Youtube-dl
def UpdateYtdl():
    error = call('%s -U' %(Prog['youtubedl']))
    time.sleep(5)
    if exists(Prog['youtubedl']+'.new'):
        call('ERASE %s' %(Prog['youtubedl']),shell=True)
        call('CD /D .\\Third && RENAME %s.new %s && CD ..' %(nameYtdl, nameYtdl), shell=True)

# Descargar video
