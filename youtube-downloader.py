from __future__ import unicode_literals
from tkinter import *
from tkinter_custom_button import TkinterCustomButton
import youtube_dl, time
preset=""

def webm():
    global ydl_opts, preset
    preset="WEBM Video (max quality)"
    ydl_opts={
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': 'true',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm',
        }],
    }
    download()

def mkv():
    global ydl_opts, preset
    preset="MKV Video (max quality)"
    ydl_opts={
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
    }
    download()

def mp4():
    global ydl_opts, preset
    preset="MP4 Video (max quality)"
    ydl_opts={
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': 'true',
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    download()

def wav():
    global ydl_opts, preset
    preset="WAV (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }
    download()

def aac():
    global ydl_opts, preset
    preset="AAC (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
        }],
    }
    download()

def flac():
    global ydl_opts, preset
    preset="FLAC (max quality)"
    ydl_opts={
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
        }],
    }
    download()

def mp3low():
    global ydl_opts, preset
    preset="MP3 Low (96kbps)"
    ydl_opts={
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '96',
        }],
    }
    download()

def mp3medium():
    global ydl_opts, preset
    preset="MP3 Medium (192kbps)"
    ydl_opts={
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    download()

def mp3high():
    global ydl_opts, preset
    preset="MP3 High (328kbps)"
    ydl_opts={
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '328',
        }],
    }
    download()


def download():
    url=urlbutton.get()
    print(url)
    if url:
        try:
            label=Label(roots, text = " "*100, bg="black", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
            label=Label(roots, text = "Downloading using "+preset+" preset.", bg="black",foreground="#60a3bc", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([str(url)])
                    
            label=Label(roots, text = " "*100, bg="black", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
            label=Label(roots, text = "Done!", bg="black",foreground="#009432", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
        except:
            label=Label(roots, text = " "*100, bg="black", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
            label=Label(roots, text = "Error: wrong URL.", bg="black", foreground="#e55039", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
    else:
        label=Label(roots, text = " "*100, bg="black", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
        roots.update_idletasks()
        label=Label(roots, text = "Error: the URL box is empty.", foreground="#e55039", bg="black", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=2)
        roots.update_idletasks()
    urlbutton.delete(0, END)
    roots.update_idletasks()


def paste():
    urlbutton.delete(0, END)
    global ClipBoard
    AnnoyingWindow = Tk()
    try:
        ClipBoard = AnnoyingWindow.clipboard_get()
    except:
        pass
    AnnoyingWindow.destroy()
    try:
        urlbutton.insert(0, ClipBoard)
    except:
        pass
    
def roots():
        global urlbutton, roots, paste, mp3low, mp3medium, mp3high, flac, aac, wav, mp4, mkv, webm

        roots=Tk()
        roots.title('YouTube Downloader')
        roots.configure(background='black')
        logo=PhotoImage(file="ytlogo.png")

        labellogo=Label(roots, image=logo, background="black").grid(row=0, columnspan=3, column=0, padx=2, pady=2)
        label=Label(roots, text="Enter URL:", bg="black", fg="white", font='Calibri').grid(row=1, columnspan=3, column=0, padx=2, pady=5)
        urlbutton = Entry(roots, background="#FAFAFA", foreground="#000000", width=100)
        urlbutton.grid(row=2, columnspan=3, column=0, padx=2, pady=2)
        #grab=Button(roots, text='Paste', command=paste, font='Calibri', height=1).grid(row=2, column=3, padx=2, pady=2)
        grab=TkinterCustomButton(text="Paste", corner_radius=10, command=paste, text_font='Calibri', height=27, fg_color='#4d004d', hover_color='#670067').grid(row=3, column=1, padx=2, pady=15)
        #grab=Button(roots, text='Paste from clipboard', command=paste, bg="black", font='Calibri', fg="white", width=15, corner_radius=10).grid(row=3, column=1, padx=2, pady=2).place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        #grab=TkinterCustomButton(text="Paste", corner_radius=10, command=paste, text_font='Calibri').grid(row=3, column=1, padx=2, pady=2)

        mp3low=TkinterCustomButton(text="MP3 96kbps", corner_radius=10, command=mp3low, text_font='Calibri').grid(row=4, column=0, padx=2, pady=7)
        mp3medium=TkinterCustomButton(text="MP3 192kbps", corner_radius=10, command=mp3medium, text_font='Calibri').grid(row=4, column=1, padx=2, pady=7)
        mp3high=TkinterCustomButton(text="MP3 328kbps", corner_radius=10, command=mp3high, text_font='Calibri').grid(row=4, column=2, padx=2, pady=7)

        flac=TkinterCustomButton(text="FLAC", corner_radius=10, command=flac, text_font='Calibri').grid(row=5, column=0, padx=2, pady=7)
        aac=TkinterCustomButton(text="AAC", corner_radius=10, command=aac, text_font='Calibri').grid(row=5, column=1, padx=2, pady=7)
        wav=TkinterCustomButton(text="WAV", corner_radius=10, command=wav, text_font='Calibri').grid(row=5, column=2, padx=2, pady=7)

        mp4=TkinterCustomButton(text="MP4", corner_radius=10, command=mp4, text_font='Calibri').grid(row=6, column=0, padx=2, pady=7)
        mkv=TkinterCustomButton(text="MKV", corner_radius=10, command=mkv, text_font='Calibri').grid(row=6, column=1, padx=2, pady=7)
        webm=TkinterCustomButton(text="WEBM", corner_radius=10, command=webm, text_font='Calibri').grid(row=6, column=2, padx=2, pady=7)
        
        label=Label(roots, text = " "*100, bg="black", font=("Calibri", 12)).grid(row=7, columnspan=3, column=0, padx=2, pady=7)
        roots.mainloop()

roots()
 
