import pyexe
import pyico
import pylink
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
    _makeButton(
        root,
        "创建qrcPyQt图片文件",
        lambda file: pyqrc.make(
            file,
            "/",
            *askopenfilenames(
                filetypes=(
                    (
                        "图片文件", (
                            ".png",
                            ".jpg",
                            ".jpeg",
                            ".emf",
                        ),
                    ),
                    ("所有文件", ".*"),
                ),
            ),
        ) if file else None,
        (
            ("PyQt5图片文件", ".qrc"),
            ("所有文件", ".*"),
        ),
        ask=asksaveasfilename,
    )
    root.mainloop()


if __name__ == '__main__':
    test()
