from tkinter import *
import time

class Stopwatch:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x200")
        self.window.title("Stop Watch")
        self.window.config(bg="black")
        self.window.resizable(height=False, width=False)

        self.label = Label(self.window, text="0.00", fg="White", font=("Arial", 30), bg="Black")
        self.label.pack(expand=True)

        self.running = False
        self.starting_time = 0
        self.elapsed_time = 0

        start_button = Button(self.window, text="Start", command=self.start, font=("Arial", 15), fg = "White", bg = "Red")
        start_button.pack(side=LEFT, padx=10, pady=10)

        stop_button = Button(self.window, text="Stop", command=self.stop, font=("Arial", 15), fg = "White", bg = "Blue")
        stop_button.pack(side=LEFT, padx=10, pady=10)

        reset_button = Button(self.window, text="Reset", command=self.reset, font=("Arial", 15), fg = "White", bg = "Green")
        reset_button.pack(side=LEFT, padx=10, pady=10)

        self.update()

    def start(self):
        if not self.running:
            self.starting_time = time.time() - self.elapsed_time
            self.running = True


    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.starting_time
            self.running = False
        

    def reset(self):
        self.elapsed_time = 0
        self.running = False
        self.label.config(text="0.00")

    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.starting_time
            self.label.config(text=f"{self.elapsed_time:.2f}")
    
        self.window.after(50, self.update)


if __name__ == "__main__":
    s = Stopwatch()
    s.window.mainloop()