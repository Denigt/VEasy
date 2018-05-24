import os.path
import winshell
from win32com.client import Dispatch
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from os import system
from os import chdir
from os import getcwd
from os import listdir
from os import replace
from os import mkdir
from shutil import copy2
from shutil import copytree
from shutil import rmtree
from os.path import exists

InitDir=getcwd()
#--Funciones--------------------------------------------------------------------
#Elegir el directorio de instalación
def chooseDIR():
    aux = askdirectory().replace('/', '\\')
    if aux!='':
        DIR.set(aux)

#Instalación del programa       
def install():
    #Variables locales
    error=0
    estados=['Pulsa el botón "%s" para comenzar' %instalar, 'Instalando', 'Borrando archivos de instalación']
    if exists(DIR.get()) and not exists(DIR.get()+'\\'+'VEasyBeta'):
        EST.set(estados[1])
        win.update()
        #Instalar programa
        try: copytree(InitDir+'\\'+'VEasyBeta\\', DIR.get()+'\\'+'VEasyBeta\\')
        except:
            error=1
            showerror('Error', 'No se ha podido llevar a cabo la instalación')
        #Modificar variables de entorno
        else:
            chdir(DIR.get()+'\\VEasyBeta\\'+'Third\\')
            system('VEconfig.bat')
        #Crear acceso directo
        if ACC.get():
            desktop = winshell.desktop()
            path = os.path.join(desktop, "VEasy.lnk")
            target = r"%s" %DIR.get()+'\\'+'VEasyBeta\\'+'VEasyBeta.exe'
            wDir = r"%s" %DIR.get()+'\\'+'VEasyBeta'
            icon = r"%s" %DIR.get()+'\\'+'VEasyBeta\\'+'VEasyBeta.exe'
             
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()

        #Borrar archivos de instalación
        if DEL.get() and not error:
            EST.set(estados[2])
            win.update()
            try: rmtree(InitDir+'\\'+'VEasyBeta')
            except: showwarning('Error', 'No se han podido eliminar los archivos de instalación')
        if not error: showinfo('Instalación terminada', 'La instalación se ha llevado a cabo correctamente')
                    
    elif exists(DIR.get()+'\\'+'VEasyBeta'):
        error=1
        showerror('Error', 'Ya existe la carpeta %s en la ruta indicada' %'VEasyBeta')
    elif not exists(DIR.get()):
        error=1
        showerror('Error', 'No existe la ruta indicada para instalar el programa')
    if not error: win.destroy()
#-------------------------------------------------------------------------------
#--Variables--------------------------------------------------------------------
nombreINS='Instalador VEasy.pyw'
titulo='Instalador VEasy'
guardar='Instalar en: '
carpeta='Carpeta: '
instalar='Instalar'
estados=['Pulsa el botón "%s" para comenzar' %instalar, 'Instalando', 'Borrando archivos de instalación']
eliminar='Crear acceso directo en el escritorio'
guardarDIR='C:\\Program Files'
carpetaNOM='Programa'
#-------------------------------------------------------------------------------
#Crear Ventana
win=Tk()
win.title(titulo)
#--Variables Tkinter------------------------------------------------------------
DIR = StringVar()
DIR.set(guardarDIR)

ACC=IntVar()
ACC.set(1)

DEL=IntVar()
DEL.set(1)

EST = StringVar()
EST.set(estados[0])
#-------------------------------------------------------------------------------
#Dirección para guardar
frameDIR = Frame(win, bd=5, relief='groove')
botonDIR = Button(frameDIR, text=guardar, command=chooseDIR, width=20)
textoDIR = Entry(frameDIR, textvariable=DIR, width=50)

frameDIR.grid(padx=5, pady=5, row=3, column=2, columnspan=2, sticky=S+N+E+W)
botonDIR.grid(padx=10, pady=10, row=3, column=2, sticky=S+N+E+W)
textoDIR.grid(padx=10, pady=10, row=3, column=3, sticky=S+N+E+W)

#Botón borrar archivos de instalación
botonACC = Checkbutton(win, text=eliminar, variable=ACC)
botonACC.grid(row=4, column=2, columnspan=2, sticky=S+N+E+W)

#Botón de inicio
botonINI = Button(win, text=instalar, command=install, width=20)
botonINI.grid(padx=10, pady=10, row=5, column=2, columnspan=2, sticky=S+N+E+W)

#Barra de estado
labelEST = Label(win, textvariable=EST, bd=1, relief='sunken')
labelEST.grid(row=10, column=2, columnspan=2, sticky=S+E+W)

#Habilitar expansión de filas y columnas
win.columnconfigure(2, weight=1)
win.rowconfigure(10, weight=1)
frameDIR.columnconfigure(3, weight=1)

#Bucle ventana
win.mainloop()
