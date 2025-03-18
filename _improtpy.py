import os
from threading import Thread


def thread_install(name):
    try:
        exec("import %s" % name)
    except ModuleNotFoundError:
        os.system("pip install %s" % name)


def install(name):
    Thread(target=thread_install, args=(name,), daemon=True).start()


install("pyinstaller")
install("pywin32")
install("winshell")
install("Pillow")
import PIL, shutil
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, askyesno
import tkinter as tk
import getpass
from win32com.client import Dispatch
from pyms import file
desktop = file.userfile + r"\Desktop"

