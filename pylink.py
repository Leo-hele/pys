from _improtpy import *


def make(file, show=True):
    if not file:
        return
    source = file.replace("/", "\\")
    save_path = os.path.join(r"C:\Users\%s\Desktop" % getpass.getuser(
        ), os.path.split(file)[1]).replace('/', '\\')

    shell = Dispatch("WScript.Shell")

    link_name = os.path.splitext(save_path)[0] + ".lnk"

    shortcut = shell.CreateShortCut(link_name)
    shortcut.TargetPath = source
    shortcut.WorkingDirectory = os.path.split(save_path)[0]
    for img_file in map(
            lambda f: os.path.splitext(source)[0] + f, (".ico", ".png", ".jpg", ".jpeg", ".webp", ".emf")
    ):
        if os.path.exists(img_file):
            shortcut.IconLocation = img_file + ",0"
    shortcut.save()
    if show:
        showinfo("创建快捷方式", "已成功创建快捷方式（地点：桌面，目标：%s）。" % file)
