import config.style as style

def show(self, tk, controller,PageMainMenu):
    label = tk.Label(self, text="Über", font=style.LARGE_FONT)
    label.pack(style.MARGIN10)

    labelText = tk.Label(self, text="python-mysql-ad\n"
                                    "Tool um neue user im internen\n"
                                    "active directory anzulegen\n"
                                    "", font=style.MEDIUM_FONT)
    labelText.pack(style.MARGIN10)

    labelCopyr = tk.Label(self, text="(c) 2016 - A.Neeven, F.Kaya, D.Lentz, F.Petruschke",
                          font=style.SMALL_FONT)
    labelCopyr.pack(style.MARGIN10)

    button1 = tk.Button(self, text="zurück", command=lambda: controller.show_frame(PageMainMenu))
    button1.pack()