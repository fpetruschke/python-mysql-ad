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
    label = tk.Label(self, text="Einstellungen", font=style.LARGE_FONT)
    label.grid(row=0, column=0)
    label.grid(style.MARGIN10)

    # ACTIVE DIRECTORY
    labelAD = tk.Label(self, text="ActiveDir.", font=style.MEDIUM_FONT_BOLD)
    labelAD.grid(row=1, column=0)
    labelAD.grid(style.MARGIN10)

    labelAdHost = tk.Label(self, text="IP/Hostname: ", font=style.MEDIUM_FONT)
    labelAdHost.grid(row=2, column=0)
    inputAdHost = tk.Entry(self)
    inputAdHost.insert(0, adConf.server)
    inputAdHost.grid(row=2, column=1, pady=10, padx=10)

    labelAdUsername = tk.Label(self, text="Nutzername: ", font=style.MEDIUM_FONT)
    labelAdUsername.grid(row=3, column=0)
    inputAdUsername = tk.Entry(self)
    inputAdUsername.insert(0, adConf.username)
    inputAdUsername.grid(row=3, column=1, pady=10, padx=10)

    labelAdUserpwd = tk.Label(self, text="Passwort: ", font=style.MEDIUM_FONT)
    labelAdUserpwd.grid(row=4, column=0)
    inputAdUserpwd = tk.Entry(self)
    inputAdUserpwd.insert(0, adConf.password)
    inputAdUserpwd.grid(row=4, column=1, pady=10, padx=10)

    # check if config should be written to file - not only be temporary
    writeConfigToFile = tk.BooleanVar()
    checkboxWriteConfigToFile = tk.Checkbutton(self, text="dauerhaft Speichern", fg='red',
                                               font=style.MEDIUM_FONT_BOLD,
                                               variable=writeConfigToFile)
    checkboxWriteConfigToFile.grid(row=5, column=1)

    # MYSQL
    labelMysql = tk.Label(self, text="MYSQL", font=style.MEDIUM_FONT_BOLD)
    labelMysql.grid(row=1, column=2, pady=10, padx=10)

    labelMysqlHost = tk.Label(self, text="IP/Hostname: ", font=style.MEDIUM_FONT)
    labelMysqlHost.grid(row=2, column=2)
    inputMysqlHost = tk.Entry(self)
    inputMysqlHost.insert(0, mysqlConf.hostName)
    inputMysqlHost.grid(row=2, column=3, pady=10, padx=10)

    labelMysqlDb = tk.Label(self, text="DB-Name: ", font=style.MEDIUM_FONT)
    labelMysqlDb.grid(row=3, column=2)
    inputMysqlDb = tk.Entry(self)
    inputMysqlDb.insert(0, mysqlConf.dbName)
    inputMysqlDb.grid(row=3, column=3, pady=10, padx=10)

    labelMysqlUser = tk.Label(self, text="DB-Nutzer: ", font=style.MEDIUM_FONT)
    labelMysqlUser.grid(row=4, column=2)
    inputMysqlUser = tk.Entry(self)
    inputMysqlUser.insert(0, mysqlConf.dbUser)
    inputMysqlUser.grid(row=4, column=3, pady=10, padx=10)

    labelMysqlPwd = tk.Label(self, text="Nutzer-Passwort: ", font=style.MEDIUM_FONT)
    labelMysqlPwd.grid(row=5, column=2)
    inputMysqlPwd = tk.Entry(self)
    inputMysqlPwd.insert(0, mysqlConf.dbPassword)
    inputMysqlPwd.grid(row=5, column=3, pady=10, padx=10)

    notifySave = "Ist die Checkbox aktiviert, wird die Konfiguration nach einem Neustart dauerhaft vorgenommen."
    lblNote = tk.Label(self, text=notifySave, font=style.SMALL_FONT_BOLD)
    lblNote.grid(row=998, column=0, columnspan=4, pady=10, padx=10)

    btnSave = tk.Button(self, text="Speichern", command=lambda: combine.combine_funcs(configManager.setConfig({
        'writeToFile': writeConfigToFile.get(),
        'adHost': inputAdHost.get(),
        'adUser': inputAdUsername.get(),
        'adPwd': inputAdUserpwd.get(),
        'mysqlHost': inputMysqlHost.get(),
        'mysqlDb': inputMysqlDb.get(),
        'mysqlUser': inputMysqlUser.get(),
        'mysqlPwd': inputMysqlPwd.get()
    }), controller.show_frame(PageMainMenu)))
    btnSave.grid(row=999, column=1)

    btnBack = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
    btnBack.grid(row=999, column=0)