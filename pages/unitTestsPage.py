import sys
import subprocess
import shlex
import config.style as style
import os

# calls the testsuite and adds a Messagebox with the stdout
def executeSubprocess(self, tk, pathToSubprocess):
    result = subprocess.Popen("python3 -m unittest " + os.path.expanduser(os.getcwd() + "/" + pathToSubprocess), shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).communicate()[0]
    msgConsol = tk.Message(self, text=result, width=400, bg='black', fg='green', font=style.CONSOLE)
    msgConsol.grid(row=3, column=0, columnspan=4)
    msgConsol.grid(style.MARGIN10)


def show(self, tk, controller,PageMainMenu):
    label = tk.Label(self, text="Unit Tests", font=style.LARGE_FONT)
    label.grid(row=0, column=0, columnspan=4)
    label.grid(style.MARGIN20)

    button1 = tk.Button(self, text="zurück", width=20, command=lambda: controller.show_frame(PageMainMenu))
    button1.grid(row=1, column=3, columnspan=2)

    btnExec = tk.Button(self, text="Tests ausführen", width=20, command=lambda: executeSubprocess(self, tk, "/tests/testsuiteTest.py"))
    btnExec.grid(row=1, column=0, columnspan=2)
    btnExec.grid(style.MARGIN10)
