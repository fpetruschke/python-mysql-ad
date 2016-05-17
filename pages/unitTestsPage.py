# importing styles
import config.style as style
# importing modules for processing subprocesses and displaying their results
import subprocess
import os


def executeSubprocess(self, tk, pathToSubprocess):
    """
    executeSubprocess

    Executes the given subprocess - which is a unit test for the testsuite located and registered under tests/testsuiteTest.py

    :param tk: parent tkinter objet
    :param pathToSubprocess: path the the testsuite
    :return: function does not have a return value but is responsible for displaying the result of the subprocess
    """
    result = subprocess.Popen("python3 -m unittest " + os.path.expanduser(os.getcwd() + "/" + pathToSubprocess), shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
    msgConsol = tk.Message(self, text=result, width=400, bg='black', fg='green', font=style.CONSOLE)
    msgConsol.grid(row=3, column=0, columnspan=4)
    msgConsol.grid(style.MARGIN10)


def show(self, tk, controller, PageMainMenu):
    """
    show - unitTestsPage

    Contains all elements of the unitTestsPage.
    Is responsible for executing the unit testsuite and making it possible to display the results.

    :param tk: parent tkinter object
    :param controller: controller object
    :param PageMainMenu: PageMainMenu for switching pages
    :return: does not return a value but is responsible for displaying the pages' content
    """
    label = tk.Label(self, text="Unit Tests", font=style.LARGE_FONT)
    label.grid(row=0, column=0, columnspan=4)
    label.grid(style.MARGIN20)

    button1 = tk.Button(self, text="zurück", width=20, command=lambda: controller.show_frame(PageMainMenu))
    button1.grid(row=1, column=3, columnspan=2)

    btnExec = tk.Button(self, text="Tests ausführen", width=20, command=lambda: executeSubprocess(self, tk, "/tests/testsuiteTest.py"))
    btnExec.grid(row=1, column=0, columnspan=2)
    btnExec.grid(style.MARGIN10)
