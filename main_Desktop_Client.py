import tkintertools as tkt
import Share.definition as t
import os
import configparser
import sys
t.timetips("支持库导入成功！")

usernameHEX = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"  #用户名哈希值
passwordHEX = "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"  #密码哈希值
#(测试账户 username:1 password:1)

config = configparser.ConfigParser()
t.timetips("初始化ConfigParser对象成功!")

Login_status = False
t.timetips("登录状态重置成功！")

current_path = os.path.realpath(__file__)
directory_path = os.path.dirname(current_path)  #当前文件路径
t.timetips("成功获取当前路径！")

config_file_path = os.path.join(directory_path, 'config.ini')
t.timetips("配置文件目录设置成功！")

w = 900
h = 520
size = w,h
titlesize = f"github.com/Rain-dewdrop/Login-System"  #窗口基础设置
t.timetips("登录窗口设置初始化成功！")

root = tkt.Tk(size, title=titlesize)  #登录窗口
t.timetips("登录窗口创建成功！")

root.minsize(w, h)  #最小窗口大小
root.maxsize(w, h)  #最大窗口大小
t.timetips("登录窗口大小锁定成功！")

root.center()
t.timetips("登录窗口居中显示成功！")

cv = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
cv.place(width=1280, height=720, x=640, y=360, anchor="center")       #窗口组件   
# 存储InputBox实例
tkt.Image(cv, (w/2, h/2),(w,h), image=tkt.PhotoImage(file=os.path.join(directory_path,"Resource","background.png")), anchor="center")
tkt.Text(cv, (450, 110), text="登 录", fontsize=25, anchor="center")
username_input = tkt.InputBox(cv, (310, 180), (280, 40),placeholder="账号",  fontsize=20)
password_input = tkt.InputBox(cv, (310, 240), (280, 40),placeholder="密码", show="*",  fontsize=20)
tkt.Button(cv, (310, 320), (170, 50), text="登录", fontsize=20,command=lambda:login(username_input, password_input))
tkt.Button(cv, (490, 320), (100, 50), text="注册", fontsize=20,command=print)
tkt.Text(cv, (215, h-20), text="Different systems may have different visual presentations", fontsize=15, anchor="center")
t.timetips("登录窗口组件加载完成！")

if config.read(config_file_path):
    t.timetips("成功找到登录配置文件！")

    if 'Login' in config.sections() and config.get('Login', 'username') != "" and config.get('Login', 'password') != "" and config.get('Login', 'hwid') != "":
        t.timetips("成功找到登录配置文件!")
        password_b64 = config.get('Login', 'password')
        username_b64 = config.get('Login', 'username')
        t.timetips("成功解密配置文件!")
        password = t.b64(password_b64)
        username = t.b64(username_b64)
        username_input.clear()
        t.timetips("成功读取配置文件!")
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

def login(username_input, password_input):
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
                    t.message("请输入账号密码！")
                else:
                    t.timetips("登录失败")
                    t.message("用户名或密码错误")
        else:
            if t.HEX(username) == usernameHEX and t.HEX(password) == passwordHEX :
                if not hwid == "" :
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
                    t.message("请输入账号密码！")
                else:
                    t.timetips("登录失败")
                    t.message("用户名或密码错误")
    except Exception as e:
        t.timetips(str(e))

root.mainloop()

#↑登陆界面  ↓功能界面

if  Login_status == True:
    t.timetips("登录状态验证成功!")
else:
    t.timetips("登录状态验证失败")
    sys.exit()

w = 650
h = 380
size = w,h

root = tkt.Tk(size, title=titlesize)  #功能窗口
t.timetips("功能窗口创建成功！")

root.center()
t.timetips("功能窗口居中显示成功！")

root.minsize(w, h)  #最小窗口大小
root.maxsize(w, h)  #最大窗口大小
t.timetips("功能窗口大小锁定成功！")

cv = tkt.Canvas(root, zoom_item=True)
cv.place(width=1280, height=720)

root.mainloop()