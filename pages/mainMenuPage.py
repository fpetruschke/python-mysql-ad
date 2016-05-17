# import sys module
import sys
# importing styles
import config.style as style
# importing possibility to combine functions on button click
import projectModules.combineFunctions as combine
# import csv manager
import projectModules.executeCsv as executeCsv


def show(self, tk, controller, PageCreateUser, PageShowAll, PageCsvImport, PageSettings, PageTests, PageAbout):
    """
    show - mainMenuPage

    Contains all elements of the mainMenuPage.
    In the main menu you can choose between the different pages.

    :param tk: parent tkinter object
    :param controller: controller object
    :param PageCreateUser: page for creating new user
    :param PageShowAll: page for showing all entries inside the master MySQL table
    :param PageCsvImport: page for importing csv-files
    :param PageSettings: page for configuring the connections
    :param PageTests: page for displaying the unit tests
    :param PageAbout: page for displaying the static about text
    :return: does not return a value but is responsible for displaying the pages' content
    """
    label = tk.Label(self, text="python-mysql-ad-Tool", font=style.LARGE_FONT)
    label.pack(style.MARGIN10)

    btnCreate = tk.Button(self, text="Neuen Nutzer anlegen", width=20,command=lambda: controller.show_frame(PageCreateUser))
    btnCreate.pack(style.MARGIN10)

    btnShowAll = tk.Button(self, text="Alle Nutzer anzeigen", width=20, command=lambda: controller.show_frame(PageShowAll))
    btnShowAll.pack(style.MARGIN10)

    btnImport = tk.Button(self, text=".csv-Import", width=20, command=lambda: combine.combine_funcs(controller.show_frame(PageCsvImport)))
    btnImport.pack(style.MARGIN10)

    btnExport = tk.Button(self, text=".csv-Export", width=20, command=lambda: executeCsv.exportToCsv())
    btnExport.pack(style.MARGIN10)

    btnSettings = tk.Button(self, text="Einstellungen", width=20, command=lambda: controller.show_frame(PageSettings))
    btnSettings.pack(style.MARGIN10)

    btnTests = tk.Button(self, text="Unit-Tests", width=20, command=lambda: controller.show_frame(PageTests))
    btnTests.pack(style.MARGIN10)

    btnAbout = tk.Button(self, text="Über", width=20, command=lambda: controller.show_frame(PageAbout))
    btnAbout.pack(style.MARGIN10)

    btnExit = tk.Button(self, text="Beenden", width=20, command=lambda: sys.exit(0))
    btnExit.pack(style.MARGIN10)