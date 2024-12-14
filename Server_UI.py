import tkintertools as tkt
import subprocess
import os

current_path = os.path.realpath(__file__)
directory_path = os.path.dirname(current_path)

subprocess.Popen(f'start cmd /K python {os.path.join(directory_path,'main_Server_Client.py')}', shell=True)

root = tkt.Tk()
root.center()
root.mainloop()