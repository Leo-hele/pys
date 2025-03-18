from _improtpy import *


def make(file, save_path="", show=True):
    if not file:
        return
    file, filename = Image.open(file), file
    if not save_path:
        save_path = os.path.splitext(filename)[0] + ".ico"
    file.save(save_path)
    print(save_path)
    if show:
        showinfo("创建图标", "已创建图标（地点：%s）。" % os.path.split(save_path)[0])
