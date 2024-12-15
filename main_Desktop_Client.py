import tkintertools.animation as animation
import Share.definition as t
import tkintertools as tkt
from Share.const import *
import configparser
import sys
import os
config = configparser.ConfigParser()
current_path = os.path.realpath(__file__)
directory_path = os.path.dirname(current_path)  #当前文件路径
config_file_path = os.path.join(directory_path, 'config.ini')
root = tkt.Tk((w,h), title=titlesize)  #登录窗口
root.minsize(w, h)  #最小窗口大小
root.maxsize(w, h)  #最大窗口大小
root.center()
cv = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
cv.place(width=1280, height=720, x=640, y=360, anchor="center")
tkt.Image(cv, (w/2, h/2),(w,h), image=tkt.PhotoImage(file=os.path.join(directory_path,"Resource","background.png")), anchor="center")
LoginText = tkt.Text(cv, (450, 110), text="登 录", fontsize=25, anchor="center")
RegisterText = tkt.Text(cv, (450, -290), text="注  册", fontsize=25, anchor="center")
username_input = tkt.InputBox(cv, (310, 180), (280, 40),placeholder="账号",  fontsize=20)
password_input = tkt.InputBox(cv, (310, 240), (280, 40),placeholder="密码", show="*",  fontsize=20)
# 存储InputBox实例
BackButton = tkt.Button(cv, (20, -200), text="<-Back", command=lambda:BackMainMenu())
LoginButton = tkt.Button(cv, (310, 320), (170, 50), text="登录", fontsize=20,command=lambda:login_test(username_input, password_input))
RegisterMenuButton = tkt.Button(cv, (490, 320), (100, 50), text="注册", fontsize=20,command=lambda:register_Menu())
RegisterButton = tkt.Button(cv, (340, 820), (220, 50), text="注册", fontsize=20,command=lambda:print(1))
tkt.Text(cv, (215, h-20), text="Different systems may have different visual presentations", fontsize=15, anchor="center")
t.timetips("登录窗口组件加载完成")

Overlay = tkt.Image(cv, (w/2, (h/2)*3),(w,h), image=tkt.PhotoImage(file=os.path.join(directory_path,"Resource","OverlayPhoto.png")), anchor="center")
Overlay.disabled(True)

def OverlayAnimation():
    t.timetips('加载遮罩动画')
    Overlay.moveto(w/2, (h/2)*3)
    animation.MoveComponent(Overlay, 1000, (0, 0-h), controller=animation.smooth, fps=60).start(delay=100)
    animation.MoveComponent(Overlay, 800, (w, 0), controller=animation.smooth, fps=60).start(delay=1500)
    
def BackMainMenu():
    RegisterMenuButton.disabled(False)
    OverlayAnimation()
    animation.MoveComponent(BackButton, 1000, (0, -220), controller=animation.smooth, fps=60).start(delay=0)
    animation.MoveComponent(LoginText, 0, (0, 400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(RegisterText, 0, (0, -400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(LoginButton, 0, (0, 400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(RegisterMenuButton, 0, (0, 400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(RegisterButton, 0, (0, 500), controller=animation.smooth, fps=60).start(delay=1300)

def register_Menu():
    RegisterMenuButton.disabled(True)
    OverlayAnimation()
    animation.MoveComponent(BackButton, 1000, (0, 220), controller=animation.smooth, fps=60).start(delay=1500)
    animation.MoveComponent(LoginText, 0, (0, -400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(RegisterText, 0, (0, 400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(LoginButton, 0, (0, -400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(RegisterMenuButton, 0, (0, -400), controller=animation.smooth, fps=60).start(delay=1300)
    animation.MoveComponent(RegisterButton, 0, (0, -500), controller=animation.smooth, fps=60).start(delay=1300)

def login_test(username_input, password_input):
    global Login_status
    t.timetips("尝试登录")
    try:
        username = username_input.get()
        password = password_input.get()
        hwid = t.get_hwid()
        if 'Login' in config.sections() :
            if t.HEX(username) == usernameHEX and t.HEX(password) == passwordHEX :
                if not hwid == "" :
                    if hwid == t.b64(config.get('Login', 'hwid')) :
                        t.timetips("登录成功")
                        t.send_notification("github.com/Rain-dewdrop/Login-System", "登录成功,欢迎回来！")
                        username_b64 = t.b64code(username)
                        password_b64 = t.b64code(password)
                        hwid_b64 = t.b64code(hwid)
                        config['Login'] = {}
                        config['Login']['username'] = username_b64
                        config['Login']['password'] = password_b64
                        config['Login']['hwid'] = hwid_b64
                        with open(config_file_path, 'w') as configfile:
                            config.write(configfile)
                        Login_status = True
                        t.timetips("已更改登录状态")
                        root.destroy()
                    else:
                        t.timetips("配置文件hwid验证失败")
                        t.message("Hwid验证失败,请不要复制他人的配置文件,请在删除配置文件后重试!")
                else :
                    t.timetips("登录成功！")
                    t.send_notification("github.com/Rain-dewdrop/Login-System", "登录成功,欢迎回来！")
                    username_b64 = t.b64code(username)
                    password_b64 = t.b64code(password)
                    hwid_b64 = t.b64code(hwid)
                    config['Login'] = {}
                    config['Login']['username'] = username_b64
                    config['Login']['password'] = password_b64
                    config['Login']['hwid'] = hwid_b64
                    with open(config_file_path, 'w') as configfile:
                        config.write(configfile)
                    Login_status = True
                    t.timetips("已更改登录状态")
                    root.destroy()
            else:
                if username == "" or password == "":
                    t.timetips("登录失败")
                    t.message("请输入账号密码")
                else:
                    t.timetips("登录失败")
                    t.message("用户名或密码错误")
        else:
            if t.HEX(username) == usernameHEX and t.HEX(password) == passwordHEX :
                if not hwid == "" :
                        t.timetips("登录成功！")
                        t.send_notification("github.com/Rain-dewdrop/Login-System", "登录成功,欢迎回来")
                        username_b64 = t.b64code(username)
                        password_b64 = t.b64code(password)
                        hwid_b64 = t.b64code(hwid)
                        config['Login'] = {}
                        config['Login']['username'] = username_b64
                        config['Login']['password'] = password_b64
                        config['Login']['hwid'] = hwid_b64
                        with open(config_file_path, 'w') as configfile:
                            config.write(configfile)
                        Login_status = True
                        t.timetips("已更改登录状态")
                        root.destroy()
            else:
                if username == "" or password == "":
                    t.timetips("登录失败")
                    t.message("请输入账号密码")
                else:
                    t.timetips("登录失败")
                    t.message("用户名或密码错误")
    except Exception as e:
        t.timetips(str(e))

if config.read(config_file_path):
    t.timetips("成功找到登录配置文件")
    if 'Login' in config.sections() and config.get('Login', 'username') != "" and config.get('Login', 'password') != "" and config.get('Login', 'hwid') != "":
        password_b64 = config.get('Login', 'password')
        username_b64 = config.get('Login', 'username')
        t.timetips("成功解密配置文件")
        password = t.b64(password_b64)
        username = t.b64(username_b64)
        username_input.clear()
        t.timetips("成功读取配置文件")
        password_input.clear()
        t.timetips("已清空输入框内容")
        username_input.set(username)
        password_input.set(password)
        t.timetips("已将输入框内容设置为配置文件内容")
    else:
        t.timetips("配置文件错误")
else:
    t.timetips("配置文件不存在")
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)
    t.timetips("配置文件初始化成功！")

root.mainloop()

#↑登陆界面  ↓功能界面

if  Login_status == True:
    t.timetips("登录状态验证成功")
else:
    t.timetips("登录状态验证失败")
    sys.exit()

w = 650
h = 380

root = tkt.Tk((w,h), title=titlesize)  #功能窗口
root.center()
root.minsize(w, h)  #最小窗口大小
root.maxsize(w, h)  #最大窗口大小
cv = tkt.Canvas(root, zoom_item=True)
cv.place(width=1280, height=720)
tkt.Image(cv, (w/2, h/2),(w,h), image=tkt.PhotoImage(file=os.path.join(directory_path,"Resource","background.png")), anchor="center")



root.mainloop()