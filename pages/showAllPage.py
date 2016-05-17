# importing styles
import config.style as style
# importing possibility to combine functions on button click
import projectModules.combineFunctions as combine
# importing sql manager
import projectModules.executeSql as executeSql
import projectModules.adPython as adPython
import config.adConfig as adConf


def show(self, tk, controller,PageMainMenu):
    """
    show - showAllPage

    Contains all elements of the showAllPage.
    Is responsible for showing the content of the mysql master table in a data grid.

    :param tk: parent tkinter object
    :param controller: controller object
    :param PageMainMenu: PageMainMenu for switching pages
    :return: does not return a value but is responsible for displaying the pages' content
    """
    labelrow = []

    # calling the executeSql method for showing all data
    rows = executeSql.executeMysqlShow('*', 'user')

    labelNote = tk.Label(self, text="Auflistung aller Nutzer", font=style.LARGE_FONT)
    labelNote.grid(row=0, column=0, columnspan=2)
    labelNote.grid(style.MARGIN20)

    # button for refreshing the list after inserting new entries
    buttonRefresh = tk.Button(self, text="Synchronisieren", command=lambda: refreshAfterDelete(self, tk, labelrow))
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


def refreshShowAll(self, tk, labelrow):
    """
    refreshShowAll

    :param tk: parent tkinter object
    :param labelrow: the list of labels to display
    :return: doesn't actually hava a return value but is responsible for showing the grid with the current mysql data
    """
    adobj = adPython.AdPython(adConf.server,adConf.username,adConf.password)
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
        labels.append(tk.Button(self, text="X", fg="red", justify="center", font=style.MEDIUM_FONT_BOLD,
                                command=lambda tmprow=row: combine.combine_funcs(
                                    executeSql.executeMysqlDelete('user', 'user_id', tmprow[0]),
                                    refreshAfterDelete(self, tk, labelrow),
                                    adobj.deleteUser(tmprow[3]))))
        labels[6].grid(row=counter, column=6)
        labelrow.append(labels)
        counter += 1

    adobj.syncsql(rows,True)


def refreshAfterDelete(self, tk, labelrow):
    """
    refreshAfterDelete

    :param tk: parent tkinter object
    :param labelrow: list of all existing rows
    :return: function does not return a value but is responsible for calling the refreshShowAll function
    """
    for row in labelrow:
        for label in row:
            label.destroy()

    refreshShowAll(self, tk, labelrow)