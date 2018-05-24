#VEASY VERSIÓN .PY BETA                                                                                                #| LEYENDA
                                                                                                                        #|   Variables importtantes -> Capitalizadas
#--Importación de módulos-------------------------------------------------------------------                            #|   Variables Tkinter ------> Mayúsculas
from subprocess import *                                                                                                #|   Variables normales -----> Minúsculas
import sys                                                                                                              #|
import threading                                                                                                        #|
from os import mkdir                                                                                                    #|    Nombres de variables tkinter
from os import remove                                                                                                   #|      LA -> Label
from os import getcwd                                                                                                   #|      TX -> Entry
from os import listdir                                                                                                  #|      F --> Frame
from shutil import rmtree                                                                                               #|      B --> Button
from os.path import exists                                                                                              #|      CB -> Checkbutton
from os.path import isfile                                                                                              #|      OM -> OptionMenu
from os.path import isdir                                                                                               #|      M --> Menu
from tkinter import *                                                                                                   #|      SC -> ScrollBar
from tkinter.ttk import *                                                                                               #|      CA -> Canvas
from tkinter.messagebox import *                                                                                        #|    Programas de terceros:
from tkinter.filedialog import *                                                                                        #|      Youtube-dl
import Funciones as f                                                                                                   #|      Ffmpeg
#-------------------------------------------------------------------------------------------                            #|      
                                                                                                                        #|
#--Preparación de la CMD--------------------------------------------------------------------                            #|
call('@ECHO OFF', shell=True)                                                                                           #|
call('COLOR F0', shell=True)                                                                                            #|
#-------------------------------------------------------------------------------------------                            #|
                                                                                                                        #|   
#--Variables de inicio y nombres------------------------------------------------------------                            #|
#  Directorios                                                                                                          #|
InitDir=getcwd()                                                                                                        #|      
Prog={'ffmpeg':'Third\\Converter', 'pyfile':'VEasy.py', 'youtubedl': 'Third\\Downloader.exe'}
Carp={'files':'\\Temp', 'images':'\\Images'}
#  Excepciones
Except=['"', '*', ':', '<', '>', '?', '|', '\\', '/']
#  Menús
Funcion=['Descargar vídeos', 'Convertir vídeos']
Tema=['Claro', 'Oscuro', 'VEasy']
Info=['Acerca de VEasy', 'Acerca de Ffmpeg', 'Acerca de Youtube-dl']
#  Configuración de Widgets
c={'blanco':'#FFFFFF', 'grisc':'#F0F0F0', 'negro':'#000000','negroc': '#020245', 'griso':'#222275', 'naranja':'#FF7A21', 'caranja':'#FF9853', 'rojo':'#960A0A', 'error':'#FFC0C0', 'select':'#9CD6FF'}
Color=[{'fg':c['negro'], 'fg2':c['negro'], 'bg':c['blanco'], 'bg2':c['blanco'], 'bg3':c['blanco'], 'afg':c['negro'], 'abg':c['grisc'], 'sfg':c['negro'], 'sbg':c['select']},
       {'fg':c['blanco'], 'fg2':c['negro'], 'bg':c['negroc'], 'bg2':c['blanco'], 'bg3':c['griso'], 'afg':c['blanco'], 'abg':c['griso'], 'sfg':c['negro'], 'sbg':c['select']},
       {'fg':c['negro'], 'fg2':c['blanco'], 'bg':c['blanco'], 'bg2':c['naranja'], 'bg3':c['blanco'], 'afg':c['blanco'], 'abg':c['caranja'], 'sfg':c['negro'], 'sbg':c['caranja']}]
Bd=[[0,1,5],[0,1,5],[0,1,2]]
Borde=[['flat','groove','sunken'],['flat','groove','sunken'],['raised','raised','sunken']]
#  Programa
formato=[['Original','MP4','AVI','OGG','FLV','MKV','WEBM', 'AMV'],['Original','MP3','WAV','BEST','M4A','AAC','FLAC', 'WMA']]
estado=[['Listo para procesar', 'Analizando','Descargando vídeo', 'Convirtiendo vídeo', 'Guardando'],
        ['Listo para convertir', 'Analizando', 'Convirtiendo vídeo', 'Guardando']]
#-------------------------------------------------------------------------------------------

#--Crear Ventana----------------------------------------------------------------------------
WIN = Tk()
WIN.title('VEasy')
WIN.resizable(width=False, height=False)
WIN.iconbitmap('%s\\VEasy.ico' %(InitDir+Carp['images']))
WIN.option_add('*tearOff', False)
#-------------------------------------------------------------------------------------------

#--Crear Canvas-----------------------------------------------------------------------------
#FCANV, FLIST, SCLIST, CALIST
FCANV  = Frame(WIN)
FCANV.grid(padx=10, pady=10, row=5, column=7, rowspan=5, columnspan=3, sticky=S+N+E+W)

SCLIST = Scrollbar(FCANV, width=20)    
CALIST = Canvas(FCANV, width=450, height=100, yscrollcommand=SCLIST.set)
CALIST.grid(row=3, column=3, rowspan=5, columnspan=2, sticky=S+N+E+W)
SCLIST.config(command=CALIST.yview)
SCLIST.grid(row=3, column=5, rowspan=5, sticky=S+N) 
FLIST  = Frame(CALIST)
CALIST.create_window(0, 0, window=FLIST, width=450, anchor='nw')
#-------------------------------------------------------------------------------------------

#--Variables Tkinter------------------------------------------------------------------------
#  Variables del Menú
FUNCION = IntVar(value=0)
INIT    = IntVar(value=0)
TEMA    = IntVar(value=0)
#Variables de intercambio
APROCES = IntVar(value=0)
NPROCES = IntVar(value=0)
#  Downloader
URL    = StringVar(value='')
NAME   = StringVar(value='')
SAVE   = StringVar(value=InitDir)
ESTADO = StringVar(value=estado[FUNCION.get()][0])
FORMAT = StringVar(value=formato[0][0])
SOUND  = IntVar(value=0)
#  Converter
SEARCH  = StringVar(value='')
#NAME
CSOUND  = IntVar(value=0)
DELET   = IntVar(value=0)
#FORMAT
#-------------------------------------------------------------------------------------------

#--Funciones de Menús-----------------------------------------------------------------------
def InfoW(info):
    #Variables
    cont=0
    program=['VEasy', 'Ffmpeg', 'Youtube-dl']
    messages=(['-Programa gratuito y de código abierto',
              '-Usa software de terceros: Ffmpeg y Youtube-dl',
              '-Sirve para la descarga y conversión de vídeo y audio',
              '-Prohibido su uso y/o distribución con fines lucrativos',
              '-Solicitar código, quejas o sugerencias:\n guerrero.raulparra@gmail.com'],
              ['-Programa gratuito',
               '-Conversor de archivos (no solo de audio y vídeo)',
               '-Se ha instalado junto a VEasy\n Lo puede usar con el comando ffmpeg en la CMD',
               '-Página oficial:\n https://www.ffmpeg.org/'],
              ['-Programa gratuito',
               '-Descarga  vídeos y playlist de multitud de webs',
               '-Se encuentra en la carpeta:\n %s' %InitDir+'\\'+Prog['youtubedl'],
               '-Documentación:\n https://github.com/rg3/youtube-dl/blob/master/README.md#readme'])
    images=[InitDir+Carp['images']+'\\VEasy.png',
            InitDir+Carp['images']+'\\Ffmpeg.png',
            InitDir+Carp['images']+'\\Youtube-dl.png']
    img = PhotoImage(file=images[info])
    #Ventana
    INFO=Toplevel()
    INFO.title(program[info])
    INFO.resizable( width=False, height=False)
    INFO.configure(bg=Color[TEMA.get()]['bg'])
    INFO.iconbitmap('%s\\VEasy.ico' %(InitDir+Carp['images']))
    #Widgets
    FINFO = Frame(INFO)
    FINFO.grid(padx=10, pady=10, row=3, column=3, columnspan=3, sticky=S+N+E+W)
    for message in messages[info]:
        LA = Label(FINFO, text=message, width=60, anchor=W, justify=LEFT)
        LA.grid(padx=10, pady=10, row=cont, column=3, sticky=S+N+E+W)
        LA.config(bd=Bd[TEMA.get()][0], relief=Borde[TEMA.get()][0], bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'])
        cont+=1
    LA = Label(FINFO, image=img)
    LA.grid(padx=10, pady=10, row=0, rowspan=4, column=5, sticky=S+N+E+W)
    LA.config(bd=Bd[TEMA.get()][2], relief='sunken', bg=c['blanco'])
    FINFO.config(bd=Bd[TEMA.get()][2], relief=Borde[TEMA.get()][1], bg=Color[TEMA.get()]['bg2'])
    INFO.mainloop()
#-------------------------------------------------------------------------------------------

#--Añadir menú de opciones------------------------------------------------------------------
#  Barra del Menú
MBAR = Menu(WIN)
WIN['menu'] = MBAR
#  Menú para seleccionar programa
MPROG = Menu(MBAR)
MBAR.add_cascade(menu=MPROG, label='Programas')
MPROG.add_radiobutton(label=Funcion[0], variable=FUNCION, value=0)
MPROG.add_separator()
MPROG.add_radiobutton(label=Funcion[1], variable=FUNCION, value=1)
#  Menú para cambiar el tema
MTEMA = Menu(MBAR)
MBAR.add_cascade(menu=MTEMA, label='Tema')
MTEMA.add_radiobutton(label=Tema[0], variable=TEMA, value=0)
MTEMA.add_separator()
MTEMA.add_radiobutton(label=Tema[1], variable=TEMA, value=1)
MTEMA.add_separator()
MTEMA.add_radiobutton(label=Tema[2], variable=TEMA, value=2)
#  Menú de información
MINFO = Menu(MBAR)
MBAR.add_cascade(menu=MINFO, label='Información')
MINFO.add_command(label=Info[0], command= lambda:InfoW(0))
MINFO.add_separator()
MINFO.add_command(label=Info[1], command= lambda:InfoW(1))
MINFO.add_separator()
MINFO.add_command(label=Info[2], command= lambda:InfoW(2))
#-------------------------------------------------------------------------------------------

#--Funciones para los widgets---------------------------------------------------------------
def borrarW(*args):
    cont=0
    for widget in WIN.winfo_children():
        if cont>1:
            widget.destroy()
        cont+=1
                
def configWIN(*args):
    WIN.configure(bg=Color[TEMA.get()]['bg'])

def configCAN(*args):
    FCANV.config(bd=5, relief='groove', bg=c['blanco'])
    FLIST.config(bd=0, bg=c['blanco'])
    CALIST.config(bd=0, bg=c['blanco'])

#  Downloader
def formatDownloader(*args):
    #Actualizar Menú de Formato
    #OMFORMAT
    FORMAT.set('Original')
    OMFORMAT = OptionMenu(WIN, FORMAT, formato[SOUND.get()][0],formato[SOUND.get()][1],formato[SOUND.get()][2],formato[SOUND.get()][3],formato[SOUND.get()][4],formato[SOUND.get()][5],formato[SOUND.get()][6],formato[SOUND.get()][7])
    OMFORMAT.config(width=30)
    OMFORMAT.config(bd=Bd[TEMA.get()][1], bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'], activebackground=Color[TEMA.get()]['abg'], activeforeground=Color[TEMA.get()]['afg'])
    OMFORMAT.grid(padx=15, pady=10, row=7, column=5, sticky=S+N+E+W)
    WIN.update()
    
def WDownloader(*args):
    if INIT.get()!=0: borrarW()
    
    #Petición de URL y asignación de nombre al archivo
    #FURL, LAURL, TXURL, LANAME, TXNAME
    FURL  = Frame(WIN)
    FURL.grid(padx=10, pady=10, row=3, column=3, columnspan=3, sticky=S+N+E+W)
    LAURL = Label(FURL, text='URL', width=8)
    LAURL.grid(padx=10, pady=15, row=3, column=3, sticky=S+N+E+W)
    TXURL = Entry(FURL, textvariable=URL, width=50)
    TXURL.grid(padx=15, pady=15, row=3, column=5, sticky=S+N+E+W)

    LANAME = Label(FURL, text='Nombre', width=8)
    LANAME.grid(padx=10, pady=15, row=5, column=3, sticky=S+N+E+W)
    TXNAME = Entry(FURL, textvariable=NAME, width=50)
    TXNAME.grid(padx=15, pady=15, row=5, column=5, sticky=S+N+E+W)
    #Elección audio-vídeo o audio
    #CBSOUND
    CBSOUND = Checkbutton(WIN, text='Solo Audio', variable=SOUND)
    CBSOUND.grid(padx=20, row=5, column=3, sticky=S+N+E+W)
    #Elección de Formato
    #LAFORMAT
    LAFORMAT = Label(WIN, text='Formato', width=8)
    LAFORMAT.grid(padx=10, pady=10, row=7, column=3, sticky=S+N+E+W)
    formatDownloader()
    SOUND.trace('w', formatDownloader)
    #Elección de carpeta de guardado
    #FSAVE, BSAVE, TXSAVE
    FSAVE = Frame(WIN)
    FSAVE.grid(padx=10, pady=10, row=3, column=7, columnspan=3, sticky=S+N+E+W)
    BSAVE = Button(FSAVE, text=' Guardar en', command=searchdir, width=15)
    BSAVE.grid(padx=10, pady=15, row=3, column=3, sticky=S+N+E+W)
    TXSAVE = Entry(FSAVE, textvariable=SAVE, width=50)
    TXSAVE.grid(padx=15, pady=15, row=3, column=5, sticky=S+N+E+W)
    #Botón de procesar
    #BPROCES
    BPROCES = Button(WIN, text='Procesar', command=Procesar, width=20)
    BPROCES.grid(padx=15, pady=15, row=9, column=3, columnspan=3, sticky=N+S+E+W)
    #Barra de estado
    #LAESTADO
    LAESTADO = Label(WIN, textvariable=ESTADO)
    LAESTADO.grid(row=13, column=1, columnspan=9, sticky=S+N+E+W)
        
    FURL.config(bd=Bd[TEMA.get()][2], relief=Borde[TEMA.get()][1], bg=Color[TEMA.get()]['bg2'])
    LAURL.config(bd=Bd[TEMA.get()][0], relief=Borde[TEMA.get()][0], bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'])
    TXURL.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], selectbackground=Color[TEMA.get()]['sbg'], selectforeground=Color[TEMA.get()]['sfg'])
    LANAME.config(bd=Bd[TEMA.get()][0], relief=Borde[TEMA.get()][0], bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'])
    TXNAME.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], selectbackground=Color[TEMA.get()]['sbg'], selectforeground=Color[TEMA.get()]['sfg'])
    CBSOUND.config(bg=Color[TEMA.get()]['bg'], selectcolor=Color[TEMA.get()]['bg3'], fg=Color[TEMA.get()]['fg'], activebackground=Color[TEMA.get()]['bg'], activeforeground=Color[TEMA.get()]['fg'])
    LAFORMAT.config(bd=Bd[TEMA.get()][0], relief=Borde[TEMA.get()][0], bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'])
    FSAVE.config(bd=Bd[TEMA.get()][2], relief=Borde[TEMA.get()][1], bg=Color[TEMA.get()]['bg2'])
    BSAVE.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], activebackground=Color[TEMA.get()]['abg'], activeforeground=Color[TEMA.get()]['afg'])
    TXSAVE.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], selectbackground=Color[TEMA.get()]['sbg'], selectforeground=Color[TEMA.get()]['sfg'])
    BPROCES.config(bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'], activebackground=Color[TEMA.get()]['abg'], activeforeground=Color[TEMA.get()]['afg'])
    LAESTADO.config(bd=Bd[TEMA.get()][1], relief=Borde[TEMA.get()][2], bg=c['blanco'], fg=c['negro'])
    if INIT.get()==0: INIT.set(1)

#  Converter
def formatConverter(*args):
    #Actualizar Menú de Formato
    #OMFORMAT
    FORMAT.set('Original')
    OMFORMAT = OptionMenu(WIN, FORMAT, formato[CSOUND.get()][0],formato[CSOUND.get()][1],formato[CSOUND.get()][2],formato[CSOUND.get()][3],formato[CSOUND.get()][4],formato[CSOUND.get()][5],formato[CSOUND.get()][6],formato[CSOUND.get()][7])
    OMFORMAT.config(width=30)
    OMFORMAT.config(bd=Bd[TEMA.get()][1], bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'], activebackground=Color[TEMA.get()]['abg'], activeforeground=Color[TEMA.get()]['afg'])
    OMFORMAT.grid(padx=15, pady=10, row=7, column=5, sticky=S+N+E+W)
    WIN.update()

def WConverter(*args):
    if INIT.get()!=0: borrarW()
    
    #Elección de archivo
    #FSEARCH, BSEARCH, TXSEARCH, LANAME, TXNAME
    FSEARCH = Frame(WIN)
    FSEARCH.grid(padx=10, pady=10, row=3, column=3, columnspan=3, sticky=S+N+E+W)
    BSEARCH = Button(FSEARCH, text=' Convertir', command=searchfile, width=15)
    BSEARCH.grid(padx=10, pady=15, row=3, column=3, sticky=S+N+E+W)
    TXSEARCH = Entry(FSEARCH, textvariable=SEARCH, width=50)
    TXSEARCH.grid(padx=15, pady=15, row=3, column=5, sticky=S+N+E+W)

    LANAME = Label(FSEARCH, text='Nombre', width=8)
    LANAME.grid(padx=10, pady=15, row=5, column=3, sticky=S+N+E+W)
    TXNAME = Entry(FSEARCH, textvariable=NAME, width=50)
    TXNAME.grid(padx=15, pady=15, row=5, column=5, sticky=S+N+E+W)
    #Elección audio-vídeo o audio
    #CBSOUND
    CBSOUND = Checkbutton(WIN, text='Solo Audio', variable=CSOUND)
    CBSOUND.grid(padx=20, row=5, column=3, sticky=S+N+E+W)
    #Elegir si borrar archivo original
    #CBDEL
    CBDEL = Checkbutton(WIN, text='Borrar archivo original', variable=DELET)
    CBDEL.grid(padx=20, row=5, column=5, sticky=S+N+E+W)
    #Elección de Formato
    #LAFORMAT
    LAFORMAT = Label(WIN, text='Formato', width=8)
    LAFORMAT.grid(padx=10, pady=10, row=7, column=3, sticky=S+N+E+W)
    formatConverter()
    CSOUND.trace('w', formatConverter)
    #Elección de carpeta de guardado
    #FSAVE, BSAVE, TXSAVE
    FSAVE = Frame(WIN)
    FSAVE.grid(padx=10, pady=10, row=3, column=7, columnspan=3, sticky=S+N+E+W)
    BSAVE = Button(FSAVE, text=' Guardar en', command=searchdir, width=15)
    BSAVE.grid(padx=10, pady=15, row=3, column=3, sticky=S+N+E+W)
    TXSAVE = Entry(FSAVE, textvariable=SAVE, width=50)
    TXSAVE.grid(padx=15, pady=15, row=3, column=5, sticky=S+N+E+W)
    #Botón de procesar
    #BCONVER
    BCONVER = Button(WIN, text='Convertir', command=Procesar, width=20)
    BCONVER.grid(padx=15, pady=15, row=9, column=3, columnspan=3, sticky=N+S+E+W)
    #Barra de estado
    #LAESTADO
    LAESTADO = Label(WIN, textvariable=ESTADO)
    LAESTADO.grid(row=13, column=1, columnspan=9, sticky=S+N+E+W)

    FSEARCH.config(bd=Bd[TEMA.get()][2], relief=Borde[TEMA.get()][1], bg=Color[TEMA.get()]['bg2'])
    BSEARCH.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], activebackground=Color[TEMA.get()]['abg'], activeforeground=Color[TEMA.get()]['afg'])
    TXSEARCH.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], selectbackground=Color[TEMA.get()]['sbg'], selectforeground=Color[TEMA.get()]['sfg'])
    LANAME.config(bd=Bd[TEMA.get()][0], relief=Borde[TEMA.get()][0], bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'])
    TXNAME.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], selectbackground=Color[TEMA.get()]['sbg'], selectforeground=Color[TEMA.get()]['sfg'])
    CBSOUND.config(bg=Color[TEMA.get()]['bg'], selectcolor=Color[TEMA.get()]['bg3'], fg=Color[TEMA.get()]['fg'], activebackground=Color[TEMA.get()]['bg'], activeforeground=Color[TEMA.get()]['fg'])
    CBDEL.config(bg=Color[TEMA.get()]['bg'], selectcolor=Color[TEMA.get()]['bg3'], fg=Color[TEMA.get()]['fg'], activebackground=Color[TEMA.get()]['bg'], activeforeground=Color[TEMA.get()]['fg'])
    LAFORMAT.config(bd=Bd[TEMA.get()][0], relief=Borde[TEMA.get()][0], bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'])
    FSAVE.config(bd=Bd[TEMA.get()][2], relief=Borde[TEMA.get()][1], bg=Color[TEMA.get()]['bg2'])
    BSAVE.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], activebackground=Color[TEMA.get()]['abg'], activeforeground=Color[TEMA.get()]['afg'])
    TXSAVE.config(bg=Color[TEMA.get()]['bg'], fg=Color[TEMA.get()]['fg'], selectbackground=Color[TEMA.get()]['sbg'], selectforeground=Color[TEMA.get()]['sfg'])
    BCONVER.config(bg=Color[TEMA.get()]['bg2'], fg=Color[TEMA.get()]['fg2'], activebackground=Color[TEMA.get()]['abg'], activeforeground=Color[TEMA.get()]['afg'])
    LAESTADO.config(bd=Bd[TEMA.get()][1], relief=Borde[TEMA.get()][2], bg=c['blanco'], fg=c['negro'])
    if INIT.get()==0: INIT.set(1)
#-------------------------------------------------------------------------------------------
    
#--Funciones--------------------------------------------------------------------------------
def initTVar(*args):
    #  Downloader
    URL.set('')
    NAME.set('')
    SAVE.set(InitDir)
    ESTADO.set(estado[FUNCION.get()][0])
    FORMAT.set(formato[0][0])
    #  Converter
    SEARCH.set('')
    DELET.set(0)

def pChange(*args):
    borrarW()
    WIN.update()
    initTVar()
    if FUNCION.get()==0: WDownloader()
    if FUNCION.get()==1: WConverter()
    
def searchdir():
    aux=askdirectory(initialdir=InitDir)
    if aux!='': SAVE.set(aux.replace('/','\\'))

def searchfile():
    aux=askopenfilename(initialdir=InitDir, title='Elige un archivo', filetypes=(("All files","*.*"),
                                                                                ('Video files', "*.mp4"),('Video files', "*.avi"),('Video files', "*.ogg"),('Video files', "*.flv"),('Video files', "*.mkv"),('Video files', "*.webm"),('Video files','.amv'),
                                                                                ('Audio files', "*.mp3"),('Audio files', "*.wav"),('Audio files', "*.best"),('Audio files', "*.m4a"),('Audio files', "*.aac"),('Audio files', "*.flac"),('Audio files','.wma')))
    if aux!='' and aux!=None: SEARCH.set(aux.replace('/','\\'))

def Procesar():
    threading.Thread(target=f.Process, args=[WIN, CALIST, FLIST, NAME, URL, SEARCH, SAVE, FORMAT, DELET, NPROCES, APROCES, FUNCION, TEMA]).start()
    NPROCES.set(NPROCES.get()+1)
#-------------------------------------------------------------------------------------------

#--Main-------------------------------------------------------------------------------------
configWIN()
configCAN()
WDownloader()
TEMA.trace('w', configWIN)
TEMA.trace('w', configCAN)
TEMA.trace('w', pChange)
FUNCION.trace('w', pChange)
#-------------------------------------------------------------------------------------------

WIN.mainloop()

