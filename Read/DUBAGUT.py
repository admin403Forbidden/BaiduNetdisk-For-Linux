import tkinter as tk
import tkinter.font as font
import tkinter.scrolledtext as sc
import pyttsx3
import datetime,time,os
import requests
import threading
import news_rmrb

def download():
    down["text"]="正在下载中，界面会卡死请稍等。"
    win.update()
    #news_rmrb.main()
    dir_ = os.listdir(".\\Data\\%s"%time.strftime('%Y%m%d' , time.localtime()))
    for i in dir_:
        filebox.insert(1,i)
    down["text"]="下载今日新闻（需要连接网络）"
    win.update()

def db(self):
    
    Name = filebox.get(filebox.curselection())
    
    dir__  = ".\\Data\\%s"%time.strftime('%Y%m%d' , time.localtime())+"\\"+filebox.get(filebox.curselection())

    file = open(dir__,'r',encoding = 'utf-8')

    content = file.read()

    file.close()

    article_box.delete('1.0','end')

    article_box.insert("end",content)


    

win = tk.Tk()
win.geometry('1000x600')
win["background"] = "black"

F = font.Font(family='微软雅黑',size=17)

article_box = sc.ScrolledText(win,height=18,font = F,width = 53 ,relief=tk.FLAT,bg="black",fg='white')
article_box.place(x=0,y=0)

filebox = tk.Listbox(win,width = 38,height = 15,relief=tk.FLAT,bg="black",fg='white')
filebox.place(x=715,y=0)

filebox.bind("<Double-Button-1>",db)

local = tk.Button(win,text = "加载本地新闻",background = 'black',relief=tk.FLAT,activebackground='black',fg='white',activeforeground='white')
local.place(x = 715,y = 280)

down = tk.Button(win,text = "下载今日新闻（需要连接网络）",background = 'black',relief=tk.FLAT,activebackground='black',fg='white',activeforeground='white',command = download)
down.place(x = 800,y = 280)

play = tk.Button(win,text = "Play",background = 'black',relief=tk.FLAT,activebackground='black',fg='white',activeforeground='white')
play.place(x=0,y=550)

stop = tk.Button(win,text = "Stop",background = 'black',relief=tk.FLAT,activebackground='black',fg='white',activeforeground='white')
stop.place(x=50,y=550)
