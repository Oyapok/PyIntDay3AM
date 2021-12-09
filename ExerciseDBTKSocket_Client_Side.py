import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as mb

class MyWindow(tk.Tk):
    
    def __init__(self):
        super().__init__() # To call the method __init__() of the "super" class (here Tk)
        
        self.minsize(900,300)
        self.maxsize(1200,600)
        self.title("Tkinter Exercise")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        
        # Binding variables:
        self.nameStr=tk.StringVar()
        self.priceFloat=tk.DoubleVar()
        self.qtyInt=tk.IntVar()

        
        
        nameL=tk.Label(self, text="Name")
        nameL.grid(row=0, column=0, padx=10, pady=10)
        
        nameE=tk.Entry(self, textvariable=self.nameStr)
        nameE.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E+tk.W)
        
        priceL=tk.Label(self, text="Price")
        priceL.grid(row=0, column=1, padx=10, pady=10)
        
        priceE=tk.Entry(self, textvariable=self.priceFloat)
        priceE.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E+tk.W)
        
        qtyL=tk.Label(self, text="Qty")
        qtyL.grid(row=0, column=2, padx=10, pady=10)
        
        qtyE=tk.Entry(self, textvariable=self.qtyInt)
        qtyE.grid(row=1, column=2, padx=10, pady=10, sticky=tk.E+tk.W)
        
        loadB=tk.Button(self, text="Load", command=self.load)
        loadB.grid(row=1, column=3, padx=10, pady=10)
        
        self.setMenu()

        
    def setMenu(self):
        import sys
        mainmenu = tk.Menu(self)  # MenuBar 
        menuFile = tk.Menu(mainmenu)  # Menu 
        menuFile.add_command(label="Quit", command=sys.exit) 
  
        menuHelp = tk.Menu(mainmenu) # Menu
        menuHelp.add_command(label="About", command=self.about) 
        
        mainmenu.add_cascade(label = "File", menu=menuFile) 
        mainmenu.add_cascade(label = "Help", menu=menuHelp) 
        
        # display the menu
        self.config(menu = mainmenu) 
        
    def load(self):

        import socket
        try:
            sock_cli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_cli.connect(("localhost", 34566))
            
            sock_cli.send(self.nameStr.get().encode())
            resp=sock_cli.recv(40)
            import pickle
            row=pickle.loads(resp)
            print(f"Response from server: {row}")
            
            if len(row) != 0: # The rodu
                self.priceFloat.set(row[1])
                self.qtyInt.set(row[2])
            else:
                self.nameStr.set("Not Found!")
                self.priceFloat.set(0.)
                self.qtyInt.set(0)
                
            sock_cli.close()
            
        except Exception as ex:
            print(ex)

      
    def about(self): 
        mb.showinfo("A tkinter example", "Version 1.0")       
               
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()