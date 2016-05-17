# importing styles
import config.style as style
# importing possibility to combine functions on button click
import projectModules.combineFunctions as combine
# csv manager
import projectModules.executeCsv as executeCsv


def show(self, tk, controller, PageMainMenu):
    """
    show - csvImportPage

    Contains all elements of the csvImportPage.
    Lets you import a csv-file into MySql master table and active directory or just the active directory

    :param tk: parent tkinter object
    :param controller: controller object
    :param PageMainMenu: PageMainMenu for switching pages
    :return: does not return a value but is responsible for displaying the pages' content
    """
    lblTitle = tk.Label(self, text="Importieren einer .csv-Datei", font=style.LARGE_FONT_BOLD)
    lblTitle.grid(row=0, column=1, columnspan=2)
    lblTitle.grid(style.MARGIN10)

    lblDescription1 = tk.Label(self, text="Folgende Formatierung wird erwartet:", justify="left",
                               font=style.SMALL_FONT_BOLD)
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

    btnChooseToImportIntoMysql = tk.Button(self, text="Vollständiger Import",
                                           command=lambda: combine.combine_funcs(executeCsv.importFromCsv(),
                                                                         controller.show_frame(PageMainMenu)))
    btnChooseToImportIntoMysql.grid(row=998, column=1)
    btnChooseToImportIntoMysql.grid(style.MARGIN10)

    btnChooseToImportOnlyAD = tk.Button(self, text="Import NUR nach AD", fg='red',
                                        command=lambda: combine.combine_funcs(executeCsv.importToAD(),
                                            controller.show_frame(PageMainMenu)))
    btnChooseToImportOnlyAD.grid(row=998, column=2)
    btnChooseToImportOnlyAD.grid(style.MARGIN10)

    # button for going back to the main menu
    buttonBack = tk.Button(self, text="zurück", width=35, command=lambda: controller.show_frame(PageMainMenu))
    buttonBack.grid(row=999, column=0, columnspan=3)
    buttonBack.grid(style.MARGIN10)