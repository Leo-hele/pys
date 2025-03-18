import pyexe
import pyico
import pylink
import pystart_computer
from _improtpy import *


def _makeButton(
        master,
        text="",
        command=lambda _: None,
        filetypes=None,
        side=tk.TOP,
        anchor=tk.CENTER,
        pady=20,
        ask=askopenfilename,
        **kw,
):
    button = tk.Button(
        master,
        text=text,
        command=lambda: command(
            "\\".join(
                ask(
                    filetypes=filetypes if filetypes else (),
                    parent=master,
                ).split("/"),
            ),
        ),
        **kw,
    )
    button.pack(side=side, anchor=anchor, pady=pady)
    return button


def test():
    root = tk.Tk()
    root.title("pys")
    _makeButton(root, "创建快捷方式", pylink.make, (("所有文件", ".*"),))
    _makeButton(root, "创建图标文件", pyico.make, (
        ("图片文件", (".png", ".jpg", ".jpeg", ".ico", ".emf")),
        ("所有文件", ".*"),
    ))
    _makeButton(root, "创建exe可执行文件", pyexe.make, (("python文件", ".py"), ("所有文件", ".*")))
    _makeButton(root, "创建启动", pystart_computer.make, (
        ("可执行文件", (".exe", ".bat", ".vbs", ".dll")),
        ("所有文件", ".*")
    ))
    root.mainloop()


if __name__ == '__main__':
    test()
