# import tkinter for gui
import tkinter as tk

# import script for centering the gui on the display
import projectModules.positionAppOnDisplay as positionAppOnDisplay

# import pages
import pages.aboutPage as about
import pages.settingsPage as settings
import pages.csvImportPage as csvImport
import pages.showAllPage as showAll
import pages.createUserPage as createUser
import pages.mainMenuPage as mainMenu


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
        tk.Tk.minsize(self, width=580, height=400)
        tk.Tk.maxsize(self, width=580, height=400)

        # define container as a tk.Frame
        container = tk.Frame(self)

        #centering the window on the screen
        positionAppOnDisplay.center(self)

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
        for F in (PageMainMenu, PageCsvImport, PageShowAll, PageCreateUser, PageSettings, PageAbout):
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
        mainMenu.show(self, tk, controller, PageCreateUser, PageShowAll, PageCsvImport, PageSettings, PageAbout)


'''PageCreateUser class '''
class PageCreateUser(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        createUser.show(self, tk, controller, PageMainMenu)


'''PageShowAll class '''
class PageShowAll(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        showAll.show(self, tk, controller, PageMainMenu)


'''PageCsvImport class'''
class PageCsvImport(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        csvImport.show(self, tk, controller, PageMainMenu)


'''PageSettings'''
class PageSettings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        settings.show(self, tk, controller, PageMainMenu)


'''PageAbout'''
class PageAbout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        about.show(self,tk,controller,PageMainMenu)


# initialising the main function
app=Start()
#setting icon and title
app.title("python-mysql-ad-Tool")
# starting mainloop
app.mainloop()