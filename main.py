import sys
import tkinter as tk

# contains e.g. font styles
import config.style as style
# contains the mysql execute methods which open and close db connections for statements
from projectModules import executeSql

# Method for centering the application window in the center of the screen
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


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
        tk.Tk.minsize(self, width=500, height=400)
        tk.Tk.maxsize(self, width=500, height=400)

        # define container as a tk.Frame
        container = tk.Frame(self)

        #centering the window on the screen
        center(self)

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
        label = tk.Label(self, text="python-mysql-ad-Tool", font=style.LARGE_FONT)
        # add the label object to the container
        # padding x and y axis
        label.pack(pady=10, padx=10)

        # creating a button
        # Parameters: self, title, command/function
        # lambda : run command immediately
        button1 = tk.Button(self, text="Neuen Nutzer anlegen", width=20 ,command=lambda: controller.show_frame(PageSettings))
        button1.pack(pady=10, padx=10)

        button4 = tk.Button(self, text="Alle Nutzer anzeigen", width=20, command=lambda: controller.show_frame(PageShowAll))
        button4.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Über", width=20, command=lambda: controller.show_frame(PageAbout))
        button2.pack(pady=10, padx=10)

        button3 = tk.Button(self, text="Beenden", width=20, command=lambda: sys.exit(0))
        button3.pack(pady=10, padx=10)


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
        labelNote = tk.Label(self, text="Legen Sie einen neuen Nutzer an.", font=style.LARGE_FONT)
        labelNote.grid(row=0, column=0, columnspan=2)
        labelNote.grid(padx=20, pady=20)

        labelFirstname = tk.Label(self, text="Vorname", font=style.MEDIUM_FONT)
        labelFirstname.grid(row=1, column=0)
        inputFirstname = tk.Entry(self)
        inputFirstname.grid(row=1, column=1)
        inputFirstname.grid(pady=10, padx=10)

        labelName = tk.Label(self, text="Name", font=style.MEDIUM_FONT)
        labelName.grid(row=2, column=0)
        inputName = tk.Entry(self)
        inputName.grid(row=2, column=1)
        inputName.grid(pady=10, padx=10)

        labelPassword = tk.Label(self, text="Passwort", font=style.MEDIUM_FONT)
        labelPassword.grid(row=3, column=0)
        inputPassword= tk.Entry(self)
        inputPassword.grid(row=3, column=1)
        inputPassword.grid(pady=10, padx=10)

        labelClass = tk.Label(self, text="Klasse", font=style.MEDIUM_FONT)
        labelClass.grid(row=4, column=0)
        inputClass = tk.Entry(self)
        inputClass.grid(row=4, column=1)
        inputClass.grid(pady=10, padx=10)

        button2 = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
        button2.grid(row=999, column=0)
        button2.grid(padx=20, pady=20)

        # when button is clicked, get values from input fields and hand them to the mysql execution
        button1 = tk.Button(self, text="Anlegen", command=lambda: combine_funcs(executeSql.executeMysqlInsert('user',{'name' : inputName.get(),'firstname' : inputFirstname.get(),'password' : inputPassword.get(),'class' : inputClass.get()}),controller.show_frame(PageMainMenu)))
        button1.grid(row=999, column=1)

##################################################################################################################
# PROBLEM WITH REFRESHING
##################################################################################################################
'''PageShowAll class '''
class PageShowAll(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # calling the executeSql method for showing all data
        rows = executeSql.executeMysqlShow('*', 'user')

        labelNote = tk.Label(self, text="Auflistung aller Nutzer", font=style.LARGE_FONT)
        labelNote.grid(row=0, column=1)
        labelNote.grid(padx=20, pady=20)

        # button for refreshing the list after inserting new entries
        buttonRefresh = tk.Button(self, text="Synchronisieren", command=combine_funcs(self.refreshShowAll))
        buttonRefresh.grid(row=0, column=2)

        # button for going back to the main menu
        buttonBack = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
        buttonBack.grid(row=0, column=3)

        # labels for user data grid
        label1 = tk.Label(self, text='Id', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        label1.grid(row=1, column=0)
        label2 = tk.Label(self, text='Name', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        label2.grid(row=1, column=1)
        label3 = tk.Label(self, text='Vorname', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        label3.grid(row=1, column=2)
        label4 = tk.Label(self, text='Passwort', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        label4.grid(row=1, column=3)
        label5 = tk.Label(self, text='Klasse', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        label5.grid(row=1, column=4)

        # creating labels for each tupel
        counter = 3
        for row in rows:
            if(counter % 2 == 0):
                label1 = tk.Label(self, text=row[0], fg="red", bg="white", justify="left", font=style.SMALL_FONT)
                label1.grid(row=counter, column=0)
                label2 = tk.Label(self, text=row[1], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label2.grid(row=counter, column=1)
                label3 = tk.Label(self, text=row[2], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label3.grid(row=counter, column=2)
                label4 = tk.Label(self, text=row[3], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label4.grid(row=counter, column=3)
                label5 = tk.Label(self, text=row[4], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label5.grid(row=counter, column=4)
            else:
                label1 = tk.Label(self, text=row[0], fg="red", justify="left", font=style.SMALL_FONT)
                label1.grid(row=counter, column=0)
                label2 = tk.Label(self, text=row[1], fg="black", justify="left", font=style.SMALL_FONT)
                label2.grid(row=counter, column=1)
                label3 = tk.Label(self, text=row[2], fg="black", justify="left", font=style.SMALL_FONT)
                label3.grid(row=counter, column=2)
                label4 = tk.Label(self, text=row[3], fg="black", justify="left", font=style.SMALL_FONT)
                label4.grid(row=counter, column=3)
                label5 = tk.Label(self, text=row[4], fg="black", justify="left", font=style.SMALL_FONT)
                label5.grid(row=counter, column=4)
            counter += 1

    # function for refreshing the user data grid
    def refreshShowAll(self):
        rows = executeSql.executeMysqlShow('*', 'user')
        counter = 3
        for row in rows:
            if (counter % 2 == 0):
                label1 = tk.Label(self, text=row[0], fg="red", bg="white", justify="left", font=style.SMALL_FONT)
                label1.grid(row=counter, column=0)
                label2 = tk.Label(self, text=row[1], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label2.grid(row=counter, column=1)
                label3 = tk.Label(self, text=row[2], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label3.grid(row=counter, column=2)
                label4 = tk.Label(self, text=row[3], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label4.grid(row=counter, column=3)
                label5 = tk.Label(self, text=row[4], fg="black", bg="white", justify="left", font=style.SMALL_FONT)
                label5.grid(row=counter, column=4)
            else:
                label1 = tk.Label(self, text=row[0], fg="red", justify="left", font=style.SMALL_FONT)
                label1.grid(row=counter, column=0)
                label2 = tk.Label(self, text=row[1], fg="black", justify="left", font=style.SMALL_FONT)
                label2.grid(row=counter, column=1)
                label3 = tk.Label(self, text=row[2], fg="black", justify="left", font=style.SMALL_FONT)
                label3.grid(row=counter, column=2)
                label4 = tk.Label(self, text=row[3], fg="black", justify="left", font=style.SMALL_FONT)
                label4.grid(row=counter, column=3)
                label5 = tk.Label(self, text=row[4], fg="black", justify="left", font=style.SMALL_FONT)
                label5.grid(row=counter, column=4)
            counter += 1

'''PageExecuteQuery class'''
class PageExecuteQuery(tk.Frame):
    def showGrid(self, controller):
        # defining a label OBJECT
        label = tk.Label(self, text="Hier würde Ausgabe stehen", font=style.LARGE_FONT)
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
        label = tk.Label(self, text="Über", font=style.LARGE_FONT)
        label.pack(pady=10, padx=10)

        labelText = tk.Label(self, text="python-mysql-ad\n"
                                        "Tool um neue user im internen\n"
                                        "active directory anzulegen\n"
                                        "", font=style.MEDIUM_FONT)
        labelText.pack(pady=10, padx=10)

        labelCopyr = tk.Label(self, text="(c) 2016 - A.Neeven, F.Kaya, D.Lentz, F.Petruschke",
                              font=style.SMALL_FONT)
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