# importing styles
import config.style as style
# importing possibility to combine functions on button click
import projectModules.combineFunctions as combine
# importing sql manager
import projectModules.executeSql as executeSql


def show(self, tk, controller,PageMainMenu):
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


# function for refreshing the user data grid
def refreshShowAll(self, tk, labelrow):
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
                                command=lambda userId=row[0]: combine.combine_funcs(
                                    executeSql.executeMysqlDelete('user', 'user_id', userId),
                                    refreshAfterDelete(self, tk, labelrow))))
        labels[6].grid(row=counter, column=6)
        labelrow.append(labels)
        counter += 1


# function for refreshing data from user grid after deleting data
def refreshAfterDelete(self, tk, labelrow):
    for row in labelrow:
        for label in row:
            label.destroy()

    refreshShowAll(self, tk, labelrow)