# importing styles
import config.style as style
# importing possibility to combine functions on button click
import projectModules.combineFunctions as combine
# module for managing the status of checkboxes while creating new user
import projectModules.checkboxManager as checkboxManager
# use inputValidation module
import projectModules.inputValidation as validator


def show(self, tk, controller,PageMainMenu):
    """
    show - createUserPage

    Contains all elements of the createUserPage.
    This page contains a form for insert new user into the MySQL master table and the active directory or just the ad.

    :param tk: parent tkinter object
    :param controller: controller object
    :param PageMainMenu: PageMainMenu for switching pages
    :return: does not return a value but is responsible for displaying the pages' content
    """
    labelNote = tk.Label(self, text="Legen Sie einen neuen Nutzer an.", font=style.LARGE_FONT)
    labelNote.grid(row=0, column=0, columnspan=2)
    labelNote.grid(style.MARGIN20)

    labelFirstname = tk.Label(self, text="Vorname", font=style.MEDIUM_FONT)
    labelFirstname.grid(row=1, column=0)
    inputFirstname = tk.Entry(self)
    inputFirstname.grid(row=1, column=1)
    inputFirstname.grid(style.MARGIN10)

    labelName = tk.Label(self, text="Name", font=style.MEDIUM_FONT)
    labelName.grid(row=2, column=0)
    inputName = tk.Entry(self)
    inputName.grid(row=2, column=1)
    inputName.grid(style.MARGIN10)

    labelPassword = tk.Label(self, text="Passwort", font=style.MEDIUM_FONT)
    labelPassword.grid(row=3, column=0)
    inputPassword = tk.Entry(self)
    inputPassword.grid(row=3, column=1)
    inputPassword.grid(style.MARGIN10)

    labelClass = tk.Label(self, text="Klasse", font=style.MEDIUM_FONT)
    labelClass.grid(row=4, column=0)
    inputClass = tk.Entry(self)
    inputClass.grid(row=4, column=1)
    inputClass.grid(style.MARGIN10)

    btnBackToMainMenu = tk.Button(self, text="zurück",
                                  command=lambda: combine.combine_funcs(controller.show_frame(PageMainMenu)))
    btnBackToMainMenu.grid(row=999, column=0)
    btnBackToMainMenu.grid(style.MARGIN20)

    # checkboxes for choosing method whether to create user into mysql or directly to AD
    # onlyAd = True if box is checked!
    # onlyAd = False if box is unchecked
    onlyAd = tk.BooleanVar()
    checkboxCreateAD = tk.Checkbutton(self, text="NUR im AD anlegen", fg='red', font=style.MEDIUM_FONT_BOLD,
                                      variable=onlyAd)
    checkboxCreateAD.grid(row=998, column=1)

    # when button is clicked, get values from input fields and hand them to the mysql execution
    btnCreateUser = tk.Button(self, text="Anlegen", command=lambda: combine.combine_funcs(
        checkIfValid(labelNote, onlyAd.get(), inputName.get(), inputFirstname.get(), inputPassword.get(),
                     inputClass.get())
    ))
    btnCreateUser.grid(row=999, column=1)


def checkIfValid(labelNote, onlyAd, inputName, inputFirstname, inputPassword, inputClass):
    """
    checkIfValid

    Checks if the user input for creating a new user entry is valid

    :param labelNote: Label will be set after button "save" is clicked and will display status
    :param onlyAd: stands for the checkbox state True or False - if checked, data should only be inserted into AD
    :param inputName: the name of the new user
    :param inputFirstname: the firstname of the new user
    :param inputPassword: the entered password for the new user
    :param inputClass: the class the new user belongs to
    :return: method will not return a value but be responsible for displaying the current status of the last request
    """
    validName = validator.validateIfEmpty(inputName)
    validFirstname = validator.validateIfEmpty(inputFirstname)
    validPassword = validator.validateIfEmpty(inputPassword)
    validClass = validator.validateIfEmpty(inputClass)
    emptyInputs = [validName, validFirstname, validPassword, validClass].count(False)
    if emptyInputs > 0:
        noteText = "Eingabe ungültig! \n Es müssen alle Felder ausgefüllt werde."
        labelNote.config(text=noteText, fg="red", font=style.SMALL_FONT_BOLD)
        labelNote.grid(row=0, column=0, columnspan=2)
        labelNote.grid(style.MARGIN20)
    else:
        result = validator.validatePassword(inputPassword)
        if result:
            checkboxManager.checkBoxStatus(onlyAd, 'user', inputName, inputFirstname, inputPassword, inputClass),

            noteText = "Nutzer erfolgreich angelegt."
            labelNote.config(text=noteText, fg="green", font=style.LARGE_FONT_BOLD)
            labelNote.grid(row=0, column=0, columnspan=2)
            labelNote.grid(style.MARGIN20)

            # optional: go back to main menu afterwards -> uncomment
            # controller.show_frame(PageMainMenu)
        else:
            noteText = "Passwort ungültig! \n min. 7 Zeichen, min. 1 Großbuchstabe, min. 1 Zahl"
            labelNote.config(text=noteText, fg="red", font=style.SMALL_FONT_BOLD)
            labelNote.grid(row=0, column=0, columnspan=2)
            labelNote.grid(style.MARGIN20)