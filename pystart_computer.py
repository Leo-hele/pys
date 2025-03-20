from _improtpy import *
import pylink
from shutil import move


start_file = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"


def make(file, show=True):
    pylink.make(file)
    move(desktop + rf"\{os.path.splitext(os.path.split(file)[-1])[0]}.lnk", start_file)
    if show:
        showinfo("创建启动", "已创建启动，即将弹出通知。")
    