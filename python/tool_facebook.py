from os import pipe
from tkinter import *
from tkinter import messagebox
from tkinter import font
from colorama.ansi import BEL
from colorama import Fore
from colorama import init, AnsiToWin32
from selenium import webdriver
import os , sys
import pyttsx3
import tkinter as tk 
from time import strftime
from threading import *
import pygame
import undetected_chromedriver.v2 as uc 
import base64
import json,requests,time,os,sys
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys 
import undetected_chromedriver.v2 as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from tkinter import filedialog,Tk
from PIL import ImageTk,Image
import pyautogui, pyperclip, random
from time import sleep

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream # text color
pygame.init()
bot = pyttsx3.init()
voices = bot.getProperty("voices") 
bot.setProperty("voice", voices[1].id) 
tool = Tk()
tool.geometry("840x400")
tool.iconbitmap("tuongclearlove7.ico")
tool.title("My Software")# set title
tool.configure(background="#099D9D")


class Class_multithreading(): 
    def Multiple(args):
        args.multithreading2=Thread(target=Multi_tool)
        args.multithreading2.start()
Object = Class_multithreading()

def new_time():
    time_string = strftime("Time : %H:%M:%S %p") 
    label_time.config(text = time_string)
    label_time.after(1000, new_time) 

My_str = tk.StringVar()
My_Label_string = Label(tool,fg="white",textvariable=My_str,
                        bg="#099D9D").place(x=5,y=250)
My_str.set("Path here")

def openfile():
    global My_img,My_Label
    global My_Label_Image,Filepath 
    Filepath = filedialog.askopenfilename(
    initialdir="C:\\Users\\clearlove7\Documents\\GitHub\\clearlove7.github.io\\python",
    title="you are open file",
    filetypes=[
        ("MKV file", ".mkv"),
        ("MP4 file", ".mp4"),
    ])
    My_Label = Label(tool,fg="white",bg="#099D9D",text=Filepath)
    My_Label.place(x=0,y=500)
    My_img = ImageTk.PhotoImage(Image.open(Filepath))
    My_Label_Image = Label(image=My_img).place(x=20,y=230)
    My_str.set(Filepath)

class Software():
    def handle():
        global Delay
        global loop,tuong
        try:
            loop = int(input("input number integer login google : "))
            Delay  = int(input("input integer time each time off : "))
            for tuong in range(loop):
                print("number of loop : {0}".format(loop))
                print( "time delay : {0}".format(Delay))
                #bot.say("login google")
                #bot.runAndWait()
                Software.Login()
        except ValueError:
            bot_said = "you were inputing wrong format "
            print(bot_said)
            bot.say(bot_said)
            bot.runAndWait()

    def Login():
    #num = int(input("input integer create account : "))
    #time  = int(input("input integer time each time off : "))
        while True:
            if __name__ == "__main__":
                driver = uc.Chrome()
                link = f'https://www.facebook.com/'
                driver.get(link)
                sleep(2)
                base64_message = 'dHJhbnRoaW1haTEzMzE5OThAZ21haWwuY29t'
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                data = message_bytes.decode('ascii')
                driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(data)
                sleep(3)
                base64_message = 'dHVvbmd5ZXV0aGFv'
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                data = message_bytes.decode('ascii')
                driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys(data)
                sleep(2)
                driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
                sleep(5)
                driver.get("https://www.facebook.com/Theanh28/photos/a.1509442759101639/6004433352935868/")
                sleep(3)
                driver.find_element_by_xpath('//*[@id="mount_0_0_5d"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/div[5]/div/div/div[2]/div[1]/form/div/div/div[1]/p').send_keys("hay")
                sleep(3)
                pyautogui.press("enter")
                sleep(2)
                
                sleep(Delay)
                print("Đã hết {0}".format(Delay) + "s trình duyệt của bạn đã bị tắt !")
            sys.exit()

def Multi_tool():
    try:
       Software.handle()
    except ValueError:
        print("error!, Your browser has been turned off ")

my_font=("fantasy",10,"bold")
label_time=tk.Label(tool,font=my_font, bg="#099D9D",fg="black")
label_time.grid(row=0,column=0,padx=5,pady=25)
name_dev = "By Clearlove7 Developer"
color_dev = ("black")
font_dev = ("fantasy",10,"bold")
l1 = Label(tool, text = name_dev, font = font_dev, fg = color_dev, bg="#099D9D")
l1.grid(row = 1, column = 0, sticky = W, pady = 1)

tick = Checkbutton(tool, text = "Accept", bg="#099D9D",width=5) 
tick.grid(row = 2, column = 0, sticky = W, columnspan = 2)
img = PhotoImage(file = "swift rose.png") 
my_image = Label(tool, image=img)
my_image.place(x=440, y=0,width=400 ,height=400)
b2 = Button(tool, text= "Login Google",bg="white",activebackground="#3399FF", width = 15, command=Object.Multiple)
b2.place(x=70,y=200)


Button_file = Button(text="Open file", command=openfile)
Button_file.place(x=10,y=200)

new_time()
tool.mainloop()
sys.exit("end tool") 










