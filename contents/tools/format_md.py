import os
import subprocess
from time import sleep
# prettier --write  file_path
# pip install pyautogui
import pyautogui 

def format(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            subprocess.run(["code",   file_path], check=True)
            sleep(1)
            pyautogui.hotkey('alt', 'shift', 'f')
            sleep(1)


            

list_code=[
    r"C:\Users\vvn20206205\Desktop\github\20232\DH_Slide"
]
for code in list_code:
    format(code)