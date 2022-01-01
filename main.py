from os import error
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class Windows(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=1)
        self.iFrames = []
        self.outputPath = StringVar()
        self.outputPath.set('Black')
        self.outputWidth = StringVar()
        self.outputHeight = StringVar()
        self.outputWidth.set(100)
        self.outputHeight.set(100)
        self.outputImg = Image.new('L', (100, 100), color=0)
        self.outputTkImg = ImageTk.PhotoImage(self.outputImg)
        
        self.topFrame = Frame(self)
        self.topFrame.grid(row=0, column=0)

        self.botFrame = Frame(self)
        self.botFrame.grid(row=1, column=0)

        # add image frame to top frame
        num2str = ['r', 'g', 'b', 'a']
        for i in range(0, 4):
            iFrame = ImageFrame(self.topFrame)
            iFrame.grid(row=i, column=0)
            iFrame.ChangeLabel(num2str[i] + ' channel')
            self.iFrames.append(iFrame)
        
        self.outputLabel = Label(self.botFrame, image=self.outputTkImg)
        self.outputEntry = Entry(self.botFrame, textvariable=self.outputPath)
        self.outputFileBtn = Button(self.botFrame, text='save path', command=self.FindSavePath)
        self.outputWidthLable = Label(self.botFrame, text='Width')
        self.outputXEntry = Entry(self.botFrame, textvariable=self.outputWidth)
        self.outputHeightLable = Label(self.botFrame, text='Height')
        self.outputYEntry = Entry(self.botFrame, textvariable=self.outputHeight)
        self.outputBtn = Button(self.botFrame, text='Generate', command=self.Generate)

        self.outputLabel.pack()
        self.outputEntry.pack()
        self.outputFileBtn.pack()
        self.outputWidthLable.pack()
        self.outputXEntry.pack()
        self.outputHeightLable.pack()
        self.outputYEntry.pack()
        self.outputBtn.pack()

    def SetSize(self, width, height):
        self.outputWidth.set(width)
        self.outputHeight.set(height)
    
    def Generate(self):
        self.GenerateImage()
        self.SaveImg()

    def GenerateImage(self):
        channelImgs = []
        for i in range(0,4):
            outputSize = (int(self.outputWidth.get()), int(self.outputHeight.get()))
            channelImgs.append(self.iFrames[i].image.resize(outputSize))
        self.outputImg = Image.merge('RGBA', channelImgs)
        self.outputTkImg = ImageTk.PhotoImage(self.outputImg.resize((100, 100)))
        self.outputLabel.configure(image=self.outputTkImg)

    def FindSavePath(self):
        self.outputPath.set(filedialog.asksaveasfilename())

    def SaveImg(self):
        try:
            self.outputImg.save(self.outputPath.get())
            messagebox.showinfo('ok!', 'save complete!')
        except BaseException as err:
            messagebox.showerror('failed', f"save failed! {err=}")

class ImageFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.path = tk.StringVar()
        self.path.set('Black')
        self.image = Image.new('L', (100, 100), color=0)
        self.imageTk = ImageTk.PhotoImage(self.image)

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