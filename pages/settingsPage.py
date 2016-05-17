# importing styles
import config.style as style
# importing ad and mysql configs
import config.adConfig as adConf
import config.mysqlConfig as mysqlConf
# importing possibility to combine functions on button click
import projectModules.combineFunctions as combine
# importing config manager for saving new settings
import projectModules.configManager as configManager

def show(self, tk, controller,PageMainMenu):
    """
    show - settingsPage

    Contains all elements of the settingsPage.
    Lets you set the connection settings to mysql server and active directory host.

    :param tk: parent tkinter object
    :param controller: controller object
    :param PageMainMenu: PageMainMenu for switching pages
    :return: does not return a value but is responsible for displaying the pages' content
    """
    label = tk.Label(self, text="Einstellungen", font=style.LARGE_FONT)
    label.grid(row=0, column=0, columnspan=6)
    label.grid(style.MARGIN10)

    # ACTIVE DIRECTORY
    labelAD = tk.Label(self, text="ActiveDir.", font=style.MEDIUM_FONT_BOLD)
    labelAD.grid(row=1, column=0, columnspan=4)
    labelAD.grid(style.MARGIN10)

    labelAdHost = tk.Label(self, text="IP/Hostname: ", font=style.MEDIUM_FONT)
    labelAdHost.grid(row=2, column=0)
    inputAdHost = tk.Entry(self, width=25)
    inputAdHost.insert(0, adConf.server)
    inputAdHost.grid(row=2, column=1, columnspan=3, pady=10, padx=10)

    labelAdDomain = tk.Label(self, text="Domäne: ", font=style.MEDIUM_FONT)
    labelAdDomain.grid(row=3, column=0)
    inputAdDomain1 = tk.Entry(self, width=10)
    inputAdDomain1.insert(0, adConf.domain1)
    inputAdDomain1.grid(row=3, column=1, pady=10, padx=10)

    labelAdDomain = tk.Label(self, text=".", font=style.MEDIUM_FONT)
    labelAdDomain.grid(row=3, column=2)

    inputAdDomain2 = tk.Entry(self, width=10)
    inputAdDomain2.insert(0, adConf.domain2)
    inputAdDomain2.grid(row=3, column=3, pady=10, padx=10)

    labelAdUsername = tk.Label(self, text="Nutzername: ", font=style.MEDIUM_FONT)
    labelAdUsername.grid(row=4, column=0)
    inputAdUsername = tk.Entry(self, width=25)
    inputAdUsername.insert(0, adConf.username)
    inputAdUsername.grid(row=4, column=1, columnspan=3, pady=10, padx=10)

    labelAdUserpwd = tk.Label(self, text="Passwort: ", font=style.MEDIUM_FONT)
    labelAdUserpwd.grid(row=5, column=0)
    inputAdUserpwd = tk.Entry(self, width=25)
    inputAdUserpwd.insert(0, adConf.password)
    inputAdUserpwd.grid(row=5, column=1, columnspan=3, pady=10, padx=10)

    # check if config should be written to file - not only be temporary
    writeConfigToFile = tk.BooleanVar()
    checkboxWriteConfigToFile = tk.Checkbutton(self, text="dauerhaft Speichern", fg='red',
                                               font=style.MEDIUM_FONT_BOLD,
                                               variable=writeConfigToFile)
    checkboxWriteConfigToFile.grid(row=6, column=0, columnspan=6)

    # MYSQL
    labelMysql = tk.Label(self, text="MYSQL", font=style.MEDIUM_FONT_BOLD)
    labelMysql.grid(row=1, column=4, pady=10, padx=10)

    labelMysqlHost = tk.Label(self, text="IP/Hostname: ", font=style.MEDIUM_FONT)
    labelMysqlHost.grid(row=2, column=4)
    inputMysqlHost = tk.Entry(self, width=10)
    inputMysqlHost.insert(0, mysqlConf.hostName)
    inputMysqlHost.grid(row=2, column=5, pady=10, padx=10)

    labelMysqlDb = tk.Label(self, text="DB-Name: ", font=style.MEDIUM_FONT)
    labelMysqlDb.grid(row=3, column=4)
    inputMysqlDb = tk.Entry(self, width=10)
    inputMysqlDb.insert(0, mysqlConf.dbName)
    inputMysqlDb.grid(row=3, column=5, pady=10, padx=10)

    labelMysqlUser = tk.Label(self, text="DB-Nutzer: ", font=style.MEDIUM_FONT)
    labelMysqlUser.grid(row=4, column=4)
    inputMysqlUser = tk.Entry(self, width=10)
    inputMysqlUser.insert(0, mysqlConf.dbUser)
    inputMysqlUser.grid(row=4, column=5, pady=10, padx=10)

    labelMysqlPwd = tk.Label(self, text="Nutzer-Passwort: ", font=style.MEDIUM_FONT)
    labelMysqlPwd.grid(row=5, column=4)
    inputMysqlPwd = tk.Entry(self, width=10)
    inputMysqlPwd.insert(0, mysqlConf.dbPassword)
    inputMysqlPwd.grid(row=5, column=5, pady=10, padx=10)

    notifySave = "Ist die Checkbox aktiviert, wird die Konfiguration nach einem Neustart dauerhaft vorgenommen."
    lblNote = tk.Label(self, text=notifySave, font=style.SMALL_FONT_BOLD)
    lblNote.grid(row=7, column=0, columnspan=6, pady=10, padx=10)

    # btnSave is responsible to get all the input values into the configManager which will either store the setting
    # temporary or overwrite the existing config file
    btnSave = tk.Button(self, text="Speichern", command=lambda: combine.combine_funcs(configManager.setConfig({
        'writeToFile': writeConfigToFile.get(),
        'adHost': inputAdHost.get(),
        'adUser': inputAdUsername.get(),
        'adPwd': inputAdUserpwd.get(),
        'adDomain1' : inputAdDomain1.get(),
        'adDomain2' : inputAdDomain2.get(),
        'mysqlHost': inputMysqlHost.get(),
        'mysqlDb': inputMysqlDb.get(),
        'mysqlUser': inputMysqlUser.get(),
        'mysqlPwd': inputMysqlPwd.get()
    }), controller.show_frame(PageMainMenu)))
    btnSave.grid(row=8, column=4)

    btnBack = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
    btnBack.grid(row=8, column=0)