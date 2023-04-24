# run export LC_ALL=C to avoid locale errors
import tkinter as tk
import ttkbootstrap as ttk
from pygame import mixer
import os
mixer.init()



# funcs
def handleTable(selection):
    try:
        selection = table.item(selection)['values'][0] 
        mixer.music.load(selection)
        print(f"Playing {selection}")
        songName_var.set(selection)
        next = song_list[song_list.index(selection) - 1]
        print(song_list.index(selection))
        mixer.music.play()
        # mixer.music.set_endevent(lambda: play_next_song(next))
    except:
        pass

def pause():
    if mixer.music.get_busy():
        mixer.music.pause()

def play():
    if mixer.music.get_busy() == False:
        mixer.music.unpause()

def stop():
    mixer.music.stop()
    songName_var.set("")

def play_next_song(next):
    # not working yet
    mixer.music.load(next)
    mixer.music.play()

# Setup
window = ttk.Window(themename='vapor')
window.title('app')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry('500x200')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# widgets
Frame1 = ttk.Frame(window)
songNameFrame = ttk.LabelFrame(Frame1, text="Now Playing")
controlFrame = ttk.LabelFrame(Frame1, text="Control", height=50)
controlFrameBtnPause =ttk.Button(controlFrame, text='Pause', command=pause)
controlFrameBtnPlay = ttk.Button(controlFrame, text='Play', command=play)
controlFrameBtnStop = ttk.Button(controlFrame, text='Stop', command=stop)
songName_var = tk.StringVar(value='')
songNameLabel = ttk.Label(songNameFrame, text='song', anchor='center', textvariable=songName_var)

Frame1.grid(row=0, column=0, sticky='nsew'), songNameFrame.pack(fill='x', expand=True, padx=20)
controlFrame.pack(fill='x', expand=True, padx=10, ipady=2, ipadx=10), songNameLabel.pack(),
controlFrameBtnPause.pack(side='left', padx=2)
controlFrameBtnPlay.pack(side='left', padx=2)
controlFrameBtnStop.pack(side='left', padx=2)


Frame2 = ttk.Frame(window)
table = ttk.Treeview(Frame2, columns=('songs'), show='headings')
table.heading("songs", text='Songs')
Frame2.grid(row=0, column=1, sticky='e')
table.pack(fill='y', expand=True, side='right')

song_list = ['']
for i in os.listdir():
    if '.mp3' in i:
        table.insert(parent='', index=0, values=i)
        song_list.append(i)



# Security event
window.bind('<Escape>', lambda event: window.quit())
table.bind('<<TreeviewSelect>>', lambda e: handleTable(table.selection()))
# Run
window.mainloop()