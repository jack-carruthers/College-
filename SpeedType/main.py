import tkinter as tk 
import time 
import threading 
import random 


class TypeSpeedGUI: 
    
    def __init__(self):
         
        self.root =tk.Tk()
        self.root.title("Type Speed App")  # Title
        self.root.geometry("800x400")

 
        
        
        self.texty = open("start.txt", "r").read().split("\n") 
        

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texty), font =("Helvetica", 18)) # Text 
        self.sample_label.grid(row=1, column = 3, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=2, column=3, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)

        self.speed_label = tk.Label(self.frame, text ="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPM\n0.00 WPS", font=("Helvetica", 18))
        self.speed_label.grid(row=4, column=3, columnspan=2, padx=5, pady=10)
        
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=5, column=3, columnspan=2, padx=5, pady=10)

        self.level1_button = tk.Button(self.frame, text="Level 1", command=self.level1)
        self.level1_button.grid(row=0, column=2, columnspan=2, padx=5, pady=10)

        self.level2_button = tk.Button(self.frame, text="Level 2", command=self.level2)
        self.level2_button.grid(row=0, column=3, columnspan=2, padx=5, pady=10)

        self.level3_button = tk.Button(self.frame, text="Level 3", command=self.level3)
        self.level3_button.grid(row=0, column=4, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0 
        self.started = False

        self.root.mainloop()

    def start(self, event):
        if not self.started: 
            if not event.keycode in [16, 17, 18]: 
                self.started = True 
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget("text").startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget("text")[:-1]:
            self.started = False 
            self.input_entry.config(fg="green")
                        

    def time_thread(self):
        while self.started:
            time.sleep(0.1)
            self.counter += 0.1 
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM")

    def level1(self):
        self.levelsel = 1
        print("reached level def")
        self.test_name(self.levelsel)
        
    
    def level2(self):
        self.levelsel = 2
        self.test_name(self.levelsel)

    def level3(self):
        self.levelsel = 3
        self.test_name(self.levelsel)

    def reset(self):
        self.sample_label.after(1000, self.sample_label.destroy())	
        self.texty = open("start.txt", "r").read().split("\n")
        self.sample_label = tk.Label(self.frame, text=random.choice(self.texty), font =("Helvetica", 18))
        self.started = False 
        self.counter = 0 
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPM\n0.00 WPS")
        self.sample_label.config(text=random.choice(self.texty))
        self.input_entry.delete(0, tk.END)
    
    def test_name(self, levelsel):

        print("reached test name")
        levelsel = 0 
        if self.levelsel == 1:
            self.sample_label.after(1000, self.sample_label.destroy())
            texty = open("texts1.txt", "r").read().split("\n") 
            self.sample_label = tk.Label(self.frame, text=random.choice(texty), font =("Helvetica", 18)) # Text 
            self.sample_label.grid(row=1, column = 3, columnspan=5, padx=5, pady=5)

        elif self.levelsel == 2:
            texty = open("texts2.txt", "r").read().split("\n")
            self.sample_label.after(1000, self.sample_label.destroy())
            self.sample_label = tk.Label(self.frame, text=random.choice(texty), font =("Helvetica", 18)) # Text 
            self.sample_label.grid(row=1, column = 3, columnspan=5, padx=5, pady=5)

        elif self.levelsel == 3:
            texty = open("texts3.txt", "r").read().split("\n")#
            self.sample_label.after(1000, self.sample_label.destroy())
            self.sample_label = tk.Label(self.frame, text=random.choice(texty), font =("Helvetica", 18)) # Text 
            self.sample_label.grid(row=1, column = 3, columnspan=5, padx=5, pady=5) 
        else: 
            texty = open("start.txt", "r").read().split("\n") 
            
            self.sample_label = tk.Label(self.frame, text=random.choice(texty), font =("Helvetica", 18)) # Text 
            self.sample_label.grid(row=1, column = 3, columnspan=5, padx=5, pady=5)

    
        

TypeSpeedGUI() 
