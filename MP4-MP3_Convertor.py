from moviepy.editor import *
from tkinter import filedialog
from tkinter import *
import os


def createFields(root,name,folder_path_var,row,col1,col2):
    global folder_pathMP4,folder_pathMP3
    Label(master=root,textvariable=folder_path_var).grid(row=row,column=col1)
    button = Button(text=name, command=lambda:browse_button(folder_path_var))
    button.grid(row=row, column=col2)

def browse_button(folder_path): # Allow user to select a directory and store it in global var called folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

def convertMp4ToMP3(folder_MP4,folder_MP3):
    listFiles = os.listdir(folder_MP4.get())
    print(os.listdir(folder_MP4.get()))
    for file in listFiles:
        video = VideoFileClip(folder_MP4.get()+"\\"+file)
        video.audio.write_audiofile(folder_MP3.get()+"\\"+file[0:-4]+".mp3")
        #sys.stdout

root = Tk()
root.title("MP4 to MP3 Converter")
windowWidth, windowHeight = 960,540
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
centerX, centerY = int(screen_width/2-windowWidth/2), int(screen_height/2-windowHeight/2)
root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')
folder_pathMP4 = StringVar()
folder_pathMP3 = StringVar()
createFields(root,"Browse MP4 Folder",folder_pathMP4,0,1,3)
createFields(root,"Browse MP3 Folder",folder_pathMP3,3,1,3)
convertButton = Button(text="Convert", command=lambda:convertMp4ToMP3(folder_pathMP4,folder_pathMP3))
convertButton.grid(row=6, column=1)
mainloop()