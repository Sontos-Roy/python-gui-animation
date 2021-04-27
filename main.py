from tkinter import Tk, Label
from time import sleep

class LoadingSplash:
    def __init__(self):
        #setting root window:
        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Custom Loader")
        self.root.attributes("-fullscreen", True)

        #loading text:
        Label(self.root, text="Loading....", font="Bahnschrift 15", bg="black", fg="#FFBD09").place(x=490, y=320)

        #loading blocks
        for i in range(16):
            Label(self.root,bg="#1F2732", width=2, height=1).place(x=(i+22)*22, y=350)

        #updae root to see animation:
        self.root.update()
        self.play_animation()

        #window in mainloop:
        self.root.mainloop()

    #loader animation:
    def play_animation(self):
        for i in range(200):
            for j in range(16):
                #make bloack yellow:
                Label(self.root, bg="#FFBD09", width=2, height=1).place(x=(j+22)*22, y=350)
                sleep(0.06)
                self.root.update_idletasks()
                #make block dark:   
                Label(self.root,bg="#1F2732", width=2, height=1).place(x=(j+22)*22, y=350)

        else:
            self.root.destroy()
            exit(0)


if __name__ == "__main__":
    LoadingSplash()