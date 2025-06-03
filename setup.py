import pyautogui
import time
import requests
import os

fd = ['https://github.com/ORelio/Sound-Manager-Schemes/raw/refs/heads/master/Windows/Main/Windows-Vista-7.ths', ]
prmn = ['Windows 7 Sounds']
pyautogui.alert("Hello, welcome to the setup program for the manual installation of the windows 7 user interface for windows 11.")

def download_folder():
    username = os.getlogin()
    newpath = os.path.join(r'C:\Users', username, 'Downloads', 'Win7-11')
    
    if not os.path.exists(newpath):
        try:
            os.makedirs(newpath)
            pyautogui.alert("The folder has been created.")
        except PermissionError as e:
            pyautogui.alert("The folder could not be created. Please run this program as an administrator.")

download_folder()

def dmc(name, url, save_path):
    durl = pyautogui.prompt("Pleas enter the url for " + name + ". If you do not know the url, please press enter or OK.")
    if durl == None or "":
        pyautogui.alert("The download has started with the default url. If there are any errors, please search up the package name from the Packages.txt file.")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Check if the request was successful
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        
            print(f"File downloaded successfully and saved to {save_path}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    
    else:
        pyautogui.alert("The download has started with the given url. If there are any errors, please search up the package name from the Packages.txt file.")
        try:
            response = requests.get(durl, stream=True)
            response.raise_for_status()  # Check if the request was successful
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        
            print(f"File downloaded successfully and saved to {save_path}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

dmc(prmn[0], fd[0], r'C:\Users\{username}\Downloads\Win7-11\\')

#def daero7():
