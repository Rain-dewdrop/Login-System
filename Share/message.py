import tkinter.messagebox as messagebox
from const import *
from timetips import *
def message(message):
    timetips(f"已弹窗提醒 内容:{message}")

    messagebox.askyesno(message=message,title=titlesize)

    return