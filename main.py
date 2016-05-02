import sys
import tkinter as tk

from projectModules import executeSql

#Defining Font style
LARGE_FONT = ("Helvetica", 12)
MEDIUM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

'''Start class'''
# initialising class
# inherits from tk.TK class
class Start(tk.Tk):
    # init method: works like constructor
    # self: standard implied parameter
    # *args: arguments --> any number or variable
    # **kwargs: keyword arguments --> e.g. dictionaries
    def __init__(self,*args, **kwargs):

        # call the init again
        tk.Tk.__init__(self,*args,**kwargs)

        # setting the windows size
        tk.Tk.minsize(self, width=400, height=300)
        tk.Tk.maxsize(self, width=500, height=400)

        # define container as a tk.Frame
        container = tk.Frame(self)

        # pack: packs the element just into wherever is place for it
        # fill: fills the entire space, expand: can get bigger than initialised
        container.pack(side="top", fill="both", expand=True)
        # gird: you can define exactly where the element should be placed
        # 0 = minimum size, weight: priority level
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        '''PAGES - all pages must be defined inside the F tupel !!!'''
        # dictionary for all the frames
        self.frames = {}
        for F in (PageMainMenu, PageExecuteQuery, PageShowAll, PageSettings, PageAbout):
            # initial page which will be run
            frame = F(container, self)
            self.frames[F] = frame
            # assigning the frame to the grid with row and column
            # empty rows/columns will be ignored
            # sticky: north south east west: direction to align + stretch
            frame.grid(row=0, column=0, sticky="nsew")

        # decide what page/frame will be shown
        self.show_frame(PageMainMenu)

    # method for switching pages
    # takes self and name of the container/frame content
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

'''PageMainMenu class'''
# inherits from tk.Frame class
# represents the "PageMainMenu"
class PageMainMenu(tk.Frame):
    #initialize method
    # parent: main class
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # defining a label OBJECT
        label = tk.Label(self, text="python-mysql-ad-Tool", font=LARGE_FONT)
        # add the label object to the container
        # padding x and y axis
        label.pack(pady=10, padx=10)

        # creating a button
        # Parameters: self, title, command/function
        # lambda : run command immediately
        button1 = tk.Button(self, text="Neuen Schüler anlegen", command=lambda: controller.show_frame(PageSettings))
        button1.pack()

        button4 = tk.Button(self, text="Alle Schüler anzeigen", command=lambda: controller.show_frame(PageShowAll))
        button4.pack()

        button2 = tk.Button(self, text="Über", command=lambda: controller.show_frame(PageAbout))
        button2.pack()

        button3 = tk.Button(self, text="Beenden", command=lambda: sys.exit(0))
        button3.pack()


# function for call more than one function after button click
# add to the button: command=combie_funcs(funtion1, function2)
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func

'''PageSettings class '''
class PageSettings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # defining label OBJECTs
        # adding the label object to the container
        # padding x and y axis
        labelNote = tk.Label(self, text="Legen Sie einen neuen Schüler an.", font=LARGE_FONT)
        labelNote.pack(pady=15, padx=10)

        labelFirstname = tk.Label(self, text="Vorname", font=MEDIUM_FONT)
        labelFirstname.pack(pady=15, padx=15)

        labelName = tk.Label(self, text="Name", font=MEDIUM_FONT)
        labelName.pack(pady=20, padx=15)

        labelPassword = tk.Label(self, text="Passwort", font=MEDIUM_FONT)
        labelPassword.pack(pady=20, padx=15)

        labelClass = tk.Label(self, text="Klasse", font=MEDIUM_FONT)
        labelClass.pack(pady=20, padx=15)

        button1 = tk.Button(self, text="Anlegen", command=lambda: combine_funcs(controller.show_frame(PageExecuteQuery)))
        button1.pack()

        button2 = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
        button2.pack()

# initialisation of the button dictionary - MUST be set!
button = [[0 for x in range(999)] for x in range(999)]

'''PageShowAll class '''
class PageShowAll(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # calling the executeSql method for showing all data
        rows = executeSql.executeSqlShow(""" select * from user""")
        # creating labels for each tupel
        for row in rows:
            label = tk.Label(self, text=row, fg="red", justify="left", font=SMALL_FONT)
            label.pack()

        buttonBack = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
        buttonBack.pack()

'''PageExecuteQuery class'''
class PageExecuteQuery(tk.Frame):
    def showGrid(self, controller):
        # defining a label OBJECT
        label = tk.Label(self, text="Hier würde Ausgabe stehen", font=LARGE_FONT)
        label.grid(row=0, column=0, sticky="s")

        # creating a button
        # Parameters: self, title, command/function
        # lambda : run command immediately
        buttonBackToMain = tk.Button(self, text="Hauptmenü", command=lambda: controller.show_frame(PageMainMenu))
        buttonBackToMain.grid(row=998, column=0, sticky="n")

        buttonExitGame = tk.Button(self, text="Beenden", command=lambda: sys.exit(0))
        buttonExitGame.grid(row=999, column=0, sticky="n")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.showGrid(controller)


'''PageAbout'''
class PageAbout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Über", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        labelText = tk.Label(self, text="python-mysql-ad\n"
                                    "Tool um neue user im internen\n"
                                    "active directory anzulegen\n"
                                    "", font=MEDIUM_FONT)
        labelText.pack(pady=10, padx=10)

        labelCopyr = tk.Label(self, text="(c) 2016 - A.Neeven, F.Kaya, D.Lentz, F.Petruschke", font=SMALL_FONT)
        labelCopyr.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
        button1.pack()

# initialising the main function
app=Start()
#setting icon and title
app.title("python-mysql-ad-Tool")
# DOES NOT WORK WITH .ICO ON LINUX:
#app.iconbitmap()
#app.wm_iconbitmap("/home/petrusp/PycharmProjects/gui/Start/bomb.ico")
#app.iconbitmap(r'/home/petrusp/PycharmProjects/gui/Start/bomb.ico')
# WORKAROUND (not really working)
#img = tk.Image("photo", file="bomb.png")
#app.tk.call('wm','iconphoto',app._w,img)
app.mainloop()