import sys
import tkinter as tk

# contains e.g. font styles
import config.style as style
# contains the mysql execute methods which open and close db connections for statements
from projectModules import executeSql
# module for executing csv actions
import projectModules.executeCsv as executeCsv
# module for managing the status of checkboxes while creating new user
import projectModules.checkboxManager as checkboxManager

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
        tk.Tk.minsize(self, width=550, height=400)
        tk.Tk.maxsize(self, width=550, height=400)

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
        for F in (PageMainMenu, PageCsvImport, PageShowAll, PageCreateUser, PageAbout):
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
        btnCreate = tk.Button(self, text="Neuen Nutzer anlegen", width=20 ,command=lambda: controller.show_frame(PageCreateUser))
        btnCreate.pack(pady=10, padx=10)

        btnShowAll = tk.Button(self, text="Alle Nutzer anzeigen", width=20, command=lambda: controller.show_frame(PageShowAll))
        btnShowAll.pack(pady=10, padx=10)

        btnImport = tk.Button(self, text=".csv-Import", width=20, command=lambda: combine_funcs(controller.show_frame(PageCsvImport)))
        btnImport.pack(pady=10, padx=10)

        btnExport = tk.Button(self, text=".csv-Export", width=20, command=lambda: executeCsv.exportToCsv())
        btnExport.pack(pady=10, padx=10)

        btnAbout = tk.Button(self, text="Über", width=20, command=lambda: controller.show_frame(PageAbout))
        btnAbout.pack(pady=10, padx=10)

        btnExit = tk.Button(self, text="Beenden", width=20, command=lambda: sys.exit(0))
        btnExit.pack(pady=10, padx=10)


# function for call more than one function after button click
# add to the button: command=combie_funcs(funtion1, function2)
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


'''PageCreateUser class '''
class PageCreateUser(tk.Frame):
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

        btnBackToMainMenu = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
        btnBackToMainMenu.grid(row=999, column=0)
        btnBackToMainMenu.grid(padx=20, pady=20)

        # checkboxes for choosing method whether to create user into mysql or directly to AD
        # onlyAd = 1 if box is checked!
        # onlyAd = 0 if box is unchecked
        onlyAd = tk.IntVar()
        checkboxCreateAD = tk.Checkbutton(self, text="NUR im AD anlegen", fg='red', font=style.MEDIUM_FONT_BOLD ,variable=onlyAd)
        checkboxCreateAD.grid(row=998, column=1)

        # when button is clicked, get values from input fields and hand them to the mysql execution
        btnCreateUser = tk.Button(self, text="Anlegen", command=lambda: combine_funcs(
            checkboxManager.checkBoxStatus(onlyAd, 'user', inputName.get(),inputFirstname.get(),inputPassword.get(),inputClass.get()),
            #executeSql.executeMysqlInsert('user',{'name' : inputName.get(),'firstname' : inputFirstname.get(),'password' : inputPassword.get(),'class' : inputClass.get()}),
            controller.show_frame(PageMainMenu))
          )
        btnCreateUser.grid(row=999, column=1)

##################################################################################################################
# PROBLEM WITH REFRESHING
##################################################################################################################
'''PageShowAll class '''
class PageShowAll(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        labelrow = []

        # calling the executeSql method for showing all data
        rows = executeSql.executeMysqlShow('*', 'user')

        labelNote = tk.Label(self, text="Auflistung aller Nutzer", font=style.LARGE_FONT)
        labelNote.grid(row=0, column=0, columnspan=2)
        labelNote.grid(padx=20, pady=20)

        # button for refreshing the list after inserting new entries
        buttonRefresh = tk.Button(self, text="Synchronisieren", command=lambda: self.refreshAfterDelete(labelrow))
        buttonRefresh.grid(row=0, column=2)

        # button for going back to the main menu
        buttonBack = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
        buttonBack.grid(row=0, column=3)

        # labels for user data grid
        lblId = tk.Label(self, text='Id', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        lblId.grid(row=1, column=0)
        lblName = tk.Label(self, text='Name', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        lblName.grid(row=1, column=1)
        lblFirstname = tk.Label(self, text='Vorname', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        lblFirstname.grid(row=1, column=2)
        lblUsername = tk.Label(self, text='Username', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        lblUsername.grid(row=1, column=3)
        lblPassword = tk.Label(self, text='Passwort', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        lblPassword.grid(row=1, column=4)
        lblClass = tk.Label(self, text='Klasse', fg="black", justify="left", font=style.SMALL_FONT_BOLD)
        lblClass.grid(row=1, column=5)


    # function for refreshing the user data grid
    def refreshShowAll(self,labelrow):
        rows = executeSql.executeMysqlShow('*', 'user')
        sumOfNewRows = len(rows)
        counter = 3
        for row in rows:
            labels = []
            if (counter % 2 == 0):
                labels.append(tk.Label(self, text=row[0], fg="red", bg="white", justify="left", font=style.SMALL_FONT))
                labels[0].grid(row=counter, column=0)
                labels.append(tk.Label(self, text=row[1], fg="black", bg="white", justify="left", font=style.SMALL_FONT))
                labels[1].grid(row=counter, column=1)
                labels.append(tk.Label(self, text=row[2], fg="black", bg="white", justify="left", font=style.SMALL_FONT))
                labels[2].grid(row=counter, column=2)
                labels.append(tk.Label(self, text=row[3], fg="black", bg="white", justify="left", font=style.SMALL_FONT))
                labels[3].grid(row=counter, column=3)
                labels.append(tk.Label(self, text=row[4], fg="black", bg="white", justify="left", font=style.SMALL_FONT))
                labels[4].grid(row=counter, column=4)
                labels.append(tk.Label(self, text=row[5], fg="black", bg="white", justify="left", font=style.SMALL_FONT))
                labels[5].grid(row=counter, column=5)
            else:
                labels.append(tk.Label(self, text=row[0], fg="red", justify="left", font=style.SMALL_FONT))
                labels[0].grid(row=counter, column=0)
                labels.append(tk.Label(self, text=row[1], fg="black", justify="left", font=style.SMALL_FONT))
                labels[1].grid(row=counter, column=1)
                labels.append(tk.Label(self, text=row[2], fg="black", justify="left", font=style.SMALL_FONT))
                labels[2].grid(row=counter, column=2)
                labels.append(tk.Label(self, text=row[3], fg="black", justify="left", font=style.SMALL_FONT))
                labels[3].grid(row=counter, column=3)
                labels.append(tk.Label(self, text=row[4], fg="black", justify="left", font=style.SMALL_FONT))
                labels[4].grid(row=counter, column=4)
                labels.append(tk.Label(self, text=row[5], fg="black", justify="left", font=style.SMALL_FONT))
                labels[5].grid(row=counter, column=5)
            labels.append(tk.Button(self, text="X", fg="red", justify="center", font=style.MEDIUM_FONT_BOLD, command=lambda userId=row[0]: combine_funcs(executeSql.executeMysqlDelete('user', 'user_id', userId), self.refreshAfterDelete(labelrow))))
            labels[6].grid(row=counter, column=6)
            labelrow.append(labels)
            counter += 1
    # function for refreshing data from user grid after deleting data
    def refreshAfterDelete(self, labelrow):
        for row in labelrow:
            for label in row:
                label.destroy()

        self.refreshShowAll(labelrow)

'''PageCsvImport class'''
class PageCsvImport(tk.Frame):
    def showGrid(self, controller):
        # defining a label OBJECT
        lblTitle = tk.Label(self, text="Importieren einer .csv-Datei", font=style.LARGE_FONT_BOLD)
        lblTitle.grid(row=0, column=1, columnspan=2)
        lblTitle.grid(padx=10, pady=10)

        lblDescription1 = tk.Label(self, text="Folgende Formatierung wird erwartet:", justify="left", font=style.SMALL_FONT_BOLD)
        lblDescription1.grid(row=1, column=1, columnspan=2)
        lblDescription1.grid(padx=10)
        lblDescription2 = tk.Label(self, text=" - Head-Zeile mit Spaltennamen", justify="left", font=style.SMALL_FONT_BOLD)
        lblDescription2.grid(row=2, column=1, columnspan=2)
        lblDescription2.grid(padx=10)
        lblDescription3 = tk.Label(self, text=" - Komma-separierte Werte", justify="left", font=style.SMALL_FONT_BOLD)
        lblDescription3.grid(row=3, column=1, columnspan=2)
        lblDescription3.grid(padx=10)
        lblDescription4 = tk.Label(self, text=" - Pro Zeile EIN Datensatz", justify="left", font=style.SMALL_FONT_BOLD)
        lblDescription4.grid(row=4, column=1, columnspan=2)
        lblDescription4.grid(padx=10)

        btnChooseToImportIntoMysql = tk.Button(self, text="Vollständiger Import", command=lambda: combine_funcs(executeCsv.importFromCsv(),controller.show_frame(PageMainMenu)))
        btnChooseToImportIntoMysql.grid(row=998, column=1)
        btnChooseToImportIntoMysql.grid(padx=10, pady=10)

        btnChooseToImportOnlyAD = tk.Button(self, text="Import NUR nach AD", fg='red', command=lambda: combine_funcs(#@toDo: call function for inserting into AD
                                                                             controller.show_frame(PageMainMenu)))
        btnChooseToImportOnlyAD.grid(row=998, column=2)
        btnChooseToImportOnlyAD.grid(padx=10, pady=10)

        # button for going back to the main menu
        buttonBack = tk.Button(self, text="zurück", width=35, command=lambda: controller.show_frame(PageMainMenu))
        buttonBack.grid(row=999, column=0, columnspan=3)
        buttonBack.grid(padx=10, pady=10)

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