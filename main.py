from os import error
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class Windows(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=1)
        self.iFrames = []
        
        self.topFrame = Frame(self)
        self.topFrame.grid(row=0, column=0)

        self.botFrame = Frame(self)
        self.botFrame.grid(row=1, column=0)

        num2str = ['r', 'g', 'b', 'a']
        for i in range(0, 4):
            iFrame = ImageFrame(self.topFrame)
            iFrame.grid(row=i, column=0)
            iFrame.ChangeLabel(num2str[i] + ' channel')
            self.iFrames.append(iFrame)

class ImageFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.path = tk.StringVar()
        self.path.set('Black')
        self.image = Image.new('L', (100, 100), color=0)
        self.imageTk = ImageTk.PhotoImage(self.image)
        #self.image = Image.open("testImg.jpg")
        #self.image.resize((100, 100))

        self.textLabel = Label(self)
        self.textLabel.grid(row=0, column=0)

        self.imgLabel = Label(self)
        self.imgLabel.grid(row=0, column=1)
        self.imgLabel.configure(image=self.imageTk)

        self.imgEntry = Entry(self, textvariable=self.path)
        self.imgEntry.grid(row=0, column=2)

        self.fileBtn = Button(self, text='path', command=self.FindImg)
        self.fileBtn.grid(row=0, column=3)

        self.whiteBtn = Button(self, text='white', command=self.WhiteImg)
        self.whiteBtn.grid(row=0, column=4)

        self.blackBtn = Button(self, text='black', command=self.BlackImg)
        self.blackBtn.grid(row=0, column=5)


    def ChangeLabel(self, strVal):
        self.textLabel['text'] = strVal

    def WhiteImg(self):
        self.image = Image.new('L', (100, 100), color=255)
        self.imageTk = ImageTk.PhotoImage(self.image)
        self.path.set('White')
        self.ChangeImg()        

    def BlackImg(self):
        self.image = Image.new('L', (100, 100), color=0)
        self.imageTk = ImageTk.PhotoImage(self.image)
        self.path.set('Black')
        self.ChangeImg()

    def ChangeImg(self):
        self.imgLabel.configure(image=self.imageTk)
    
    def FindImg(self):
        imgPath = filedialog.askopenfilename()
        print(imgPath)
        try:
            self.path.set(imgPath)
            self.image = Image.open(imgPath).convert('L')
            self.imageTk = ImageTk.PhotoImage(self.image.resize((100, 100)))
            print(self.image.getbbox())
            self.ChangeImg()
        except BaseException as err:
            self.path.set("Can't load image")
            print(f"Unexpected {err=}, {type(err)=}")


if __name__ == "__main__":
    root = Tk()
    Windows(root)
    root.mainloop()