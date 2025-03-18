from _improtpy import *


def make(file, link=True, ico_file="", show=True):
    newDir = os.getcwd()
    join = os.path.join
    exists = os.path.exists
    split, splitext = os.path.split, os.path.splitext
    if not file:
        return
    if (not ico_file) and show:
        ico_file = (
            ("图片文件", (".png", ".jpg", ".jpeg", ".ico", ".emf")),
            ("所有文件", ".*"),
        )
        ico_file = askopenfilename(title="创建exe可执行文件", filetypes=ico_file)
    toPath = r"D:\python make exe"
    if not exists(toPath):
        os.makedirs(toPath)
    if ico_file:
        import pyico
        pyico.make(ico_file, splitext(file)[0] + ".ico")
        os.system("pyinstaller -F -w -i %s %s" % (splitext(ico_file)[0] + ".ico", file))
    else:
        os.system("pyinstaller -F -w " + file)
    path, new_file = split(splitext(file)[0])
    if not os.path.isabs(path):
        path = join(newDir, path)
    best_file = join(toPath, new_file + ".exe")
    start_file = join(newDir, "dist", new_file + ".exe")
    if exists(best_file):
        if askyesno("创建exe可执行文件", "目标地点（%s）已有一个重名文件，是否替换？" % newDir):
            os.remove(best_file)
        else:
            return 
    shutil.move(start_file, toPath)
    shutil.rmtree(join(newDir, "dist"))
    shutil.rmtree(join(newDir, "build"))
    specName = os.path.join(newDir, new_file + ".spec")
    if exists(specName):
        os.remove(specName)
    if link:
        import pylink
        pylink.make(best_file)
    if show:
        showinfo("创建exe可执行文件", "已创建exe可执行文件（地点：%s）。" % split(best_file)[0])
