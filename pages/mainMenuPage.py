# import sys module
import sys
# importing styles
import config.style as style
# importing possibility to combine functions on button click
import projectModules.combineFunctions as combine
# import csv manager
import projectModules.executeCsv as executeCsv


def show(self, tk, controller, PageCreateUser, PageShowAll, PageCsvImport, PageSettings, PageAbout):
    # defining a label OBJECT
    label = tk.Label(self, text="python-mysql-ad-Tool", font=style.LARGE_FONT)
    # add the label object to the container
    label.pack(style.MARGIN10)

    # creating a button
    # Parameters: self, title, command/function
    btnCreate = tk.Button(self, text="Neuen Nutzer anlegen", width=20,
                          command=lambda: controller.show_frame(PageCreateUser))
    btnCreate.pack(style.MARGIN10)

    btnShowAll = tk.Button(self, text="Alle Nutzer anzeigen", width=20,
                           command=lambda: controller.show_frame(PageShowAll))
    btnShowAll.pack(style.MARGIN10)

    btnImport = tk.Button(self, text=".csv-Import", width=20,
                          command=lambda: combine.combine_funcs(controller.show_frame(PageCsvImport)))
    btnImport.pack(style.MARGIN10)

    btnExport = tk.Button(self, text=".csv-Export", width=20, command=lambda: executeCsv.exportToCsv())
    btnExport.pack(style.MARGIN10)

    btnSettings = tk.Button(self, text="Einstellungen", width=20, command=lambda: controller.show_frame(PageSettings))
    btnSettings.pack(style.MARGIN10)

    btnAbout = tk.Button(self, text="Über", width=20, command=lambda: controller.show_frame(PageAbout))
    btnAbout.pack(style.MARGIN10)

    btnExit = tk.Button(self, text="Beenden", width=20, command=lambda: sys.exit(0))
    btnExit.pack(style.MARGIN10)