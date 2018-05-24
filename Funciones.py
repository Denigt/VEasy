#FUNCIONES DE PROCESADO                                                                                                #| LEYENDA
                                                                                                                        #|   Variables importtantes -> Capitalizadas
#--Importación de módulos-------------------------------------------------------------------                            #|   Variables Tkinter ------> Mayúsculas
from subprocess import *                                                                                                #|   Variables normales -----> Minúsculas
import sys                                                                                                              #|
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
#-------------------------------------------------------------------------------------------                            #|      Ffmpeg
import time
#--Variables de inicio y nombres------------------------------------------------------------                            #|
#  Directorios                                                                                                          #|
InitDir=getcwd()                                                                                                        #|      
Prog={'ffmpeg':'Third\\Converter', 'pyfile':'VEasy.py', 'youtubedl': 'Third\\Downloader.exe'}
Carp={'files':'\\Temp', 'images':'\\Images'}
#  Excepciones
Except=['"', '*', ':', '.','<', '>', '?', '|', '\\', '/']
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
Estado=[['En espera', 'Analizando', 'Descargando', 'Convirtiendo', 'Guardando', 'Terminado'],
        ['En espera', 'Analizando', 'Convirtiendo', 'Terminado']]
#-------------------------------------------------------------------------------------------

#--Funciones--------------------------------------------------------------------------------
# InitDir -> Directorio de inicio
# Carp ----> Carpetas del programa
# Prog ----> Rutas de Ffmpeg y Youtube-dl
# Except --> Excepciones para el nombre del archivo
# El resto de variables son variables de Tkinter
def Process(WIN=None, CALIST=None, FLIST=None, NAME=None, URL=None, SEARCH=None, SAVE=None, FORMAT=None, DELET=None, NPROCES=None, APROCES=None, FUNCION=None, TEMA=None):
    # Guardar las variables Tkinter en copias locales para no modificar las orginales
    name    = StringVar(value=NAME.get())
    url     = URL.get()
    search  = SEARCH.get()
    save    = SAVE.get()
    formato = FORMAT.get()
    delet   = DELET.get()
    nproces = NPROCES.get()
    funcion = FUNCION.get()
    # Restauración de las variables originales
    NAME.set('')
    URL.set('')
    SEARCH.set('')
    #Variables para la comprobación de errores
    nocopy   = 0    #Sobreescritura
    error    = 0    #Errores comprobados
    namerror = 1    #Excepciones en nombres
    # Variables Tkinter
    ESTADO = StringVar(value=Estado[funcion][0])
    
    #Creación de etiqueta de proceso
    FRLIST = Frame(FLIST)
    FRLIST.grid(row=nproces, column=0, padx=1, sticky=S+N+E+W)
    LALIST = Label(FRLIST, textvariable= name)
    LALIST.grid(row=0, column=0, sticky=S+N+E+W)
    LAESTADO = Label(FRLIST, textvariable=ESTADO)
    LAESTADO.grid(row=1, column=0, sticky=S+N+E+W)

    FRLIST.config(bd=2, relief='raised', bg=c['blanco'])
    LALIST.config(bd=0, relief='raised', bg=c['blanco'], fg=c['negro'], height=2, width=63)
    LAESTADO.config(bd=1, relief='sunken', bg=c['blanco'], fg=c['negro'], width=63)
    
    WIN.update()
    CALIST.config(scrollregion=CALIST.bbox("all"))
    
    #Actualizar estado
    ESTADO.set(Estado[funcion][1])
    WIN.update()
    
    if funcion==0:    #Descargar vídeos de youtube
        # Comprobación de errores
        if url=='':
            error=1
            showerror('Error', 'Introduce una URL')
        elif not isdir(save):
            error=1
            showerror('Error', 'El directorio "%s" no existe' %save)
        if not error:
            try: auxname=Popen(Prog['youtubedl']+' -e "%s"' %url, stdout=PIPE).communicate()[0].decode('latin9', errors="replace")[:-1]
            except:
                showerror('Error', 'Downloader.exe no existe, vuelve a instalar el programa')
                WIN.destroy()
                sys.exit(-1)
        if not error and auxname=='':
            error=1
            showerror('Error', 'La URL introducida no es válida')
        # Inicio del procesado
        if not error:
            if name.get()=='': name.set(auxname)
            auxname=list(name.get())
            while namerror:
                namerror=0
                for quitar in Except:
                    if quitar in auxname:
                        auxname[auxname.index(quitar)]=''
                        namerror=1
            name.set(''.join(auxname))
            
            # Evitar que se inicie mientras hay un proceso activo
            if APROCES.get()==1:
                ESTADO.set(Estado[funcion][0])
                WIN.update()
                while APROCES.get()==1:
                    pass
            #Informar del inicio del proceso
            APROCES.set(1)

            # Descarga
            ESTADO.set(Estado[funcion][2])
            WIN.update()
            error=call('%s --no-playlist -o "%s\\%s.%%(ext)s" %s' %(Prog['youtubedl'], InitDir+Carp['files']+str(nproces), name.get(), url))
            if not error:
                # Conversión
                auxname=listdir(InitDir+Carp['files']+str(nproces))[0]
                ESTADO.set(Estado[funcion][3])
                WIN.update()
                if formato=='Original':
                    formato=auxname.split('.')[1]
                elif auxname!=name.get()+'.'+formato.lower():
                    error=call('ffmpeg -y -i "%s" "%s"' %(InitDir+Carp['files']+str(nproces)+'\\'+auxname, InitDir+Carp['files']+str(nproces)+'\\'+name.get()+'.'+formato.lower()))
                # Guardado
                if not error:
                    ESTADO.set(Estado[funcion][4])
                    WIN.update()
                    call('MOVE "%s" "%s"' %(InitDir+Carp['files']+str(nproces)+'\\'+name.get()+'.'+formato.lower(), save), shell=True)
                else: showerror('Error', 'Error durante la conversión')
            else: showerror('Error', 'Error durante la descarga')
            try: rmtree(InitDir+Carp['files']+str(nproces))
            except: showwarning('Aviso', 'No se han podido eliminar los archivos temporales')
            ESTADO.set(Estado[funcion][5])
   
    elif funcion==1:  #Convertir vídeos del ordenador
        # Comprobación de errores
        if search=='':
            error=1
            showerror('Error', 'Introduce el archivo a convertir')
        elif not isfile(search):
            error=1
            showerror('Error', 'El archivo "%s" no existe' %search)
        elif not isdir(save):
            error=1
            showerror('Error', 'El directorio "%s" no existe' %save)
        elif not error:
            if name.get()=='':
                auxname=re.findall('.+\\\(.+)\.', search)[0]
                name.set(auxname)
            auxname=list(name.get())
            while namerror==0:
                for quitar in Except:
                    if quitar in auxname:
                        auxname[auxname.index(quitar)]=''
                        namerror=1
            name.set(''.join(auxname))
            
            # Evitar que se inicie mientras hay un proceso activo
            if APROCES.get()==1:
                ESTADO.set(Estado[funcion][0])
                WIN.update()
                while APROCES.get()==1:
                    pass
            #Informar del inicio del proceso
            APROCES.set(1)

            # Descarga
            auxname=re.findall('\.(.+)', search)[0]
            ESTADO.set(Estado[funcion][2])
            WIN.update()
            if formato=='Original':
                if isfile(save+'\\'+name.get()+'.'+auxname):
                    if askyesno('Sobrescribir', '"%s" ya existe\n ¿Quiere sobrescribir el archivo?' %save+'\\'+name.get()+'.'+formato.lower()):
                        error=call('ffmpeg -y -i "%s" "%s"' %(search, save+'\\'+name.get()+'.'+formato.lower()))
                    else: nocopy=1
                else:
                    call('ffmpeg -y- i "%s" "%s"' %(search, save+'\\'+name.get()+'.'+formato.lower()))
            elif search!=save+'\\'+name.get()+'.'+formato.lower():
                if isfile(save+'\\'+name.get()+'.'+formato.lower()):
                    if askyesno('Sobrescribir', '"%s" ya existe\n¿Quiere sobrescribir el archivo?' %save+'\\'+name.get()+'.'+formato.lower()):
                        error=call('ffmpeg -y -i "%s" "%s"' %(search, save+'\\'+name.get()+'.'+formato.lower()))
                    else: nocopy=1
                else:
                    error=call('ffmpeg -y -i "%s" "%s"' %(search, save+'\\'+name.get()+'.'+formato.lower()))
                if error: showerror('Error', 'Error durante la conversión')
            else:
                error=1
                showerror('Error', 'Error durante la conversión')
            if not error and not nocopy and delet:
                remove(search)
            ESTADO.set(Estado[funcion][3])            
    
    # Borrar etiquetas en caso de error
    if error:
        FRLIST.grid_remove()
        LALIST.grid_remove()
        LAESTADO.grid_remove()
        NPROCES.set(nproces-1)
    # Limpiado al finalizar
    #call('CLS', shell=True)
    WIN.update()
    # Informar del fin del proceso
    APROCES.set(0)

#-------------------------------------------------------------------------------------------
