import tkinter as tk


class Window(tk.Tk):

    def __init__(self, parent, parametr):
        self.parametr = parametr
        self.parent = parent
        self.parent.title("Okno początkowe:")
        self.parent.configure(bg="black")

        self.label_text = tk.Label(
            parent,
            text=
            "Oto panel do wpisywania parametrów układu równań liniowych pierwszego stopnia. Wpisz parametry, a my wyrysujemy wykres i rozwiązanie."
        )
        self.label_text.grid(row=0, columnspan=5)

        self.text_variable_a1 = tk.DoubleVar(parent)
        self.entry_a1 = tk.Entry(parent, textvariable=self.text_variable_a1)
        self.entry_a1.grid(row=1, column=0)

        self.label_text_a1 = tk.Label(parent, text="x + ")
        self.label_text_a1.grid(row=1, column=1)

        self.text_variable_b1 = tk.DoubleVar(parent)
        self.entry_b1 = tk.Entry(parent, textvariable=self.text_variable_b1)
        self.entry_b1.grid(row=1, column=2)

        self.label_text_b1 = tk.Label(parent, text="y = ")
        self.label_text_b1.grid(row=1, column=3)

        self.text_variable_c1 = tk.DoubleVar(parent)
        self.entry_c1 = tk.Entry(parent, textvariable=self.text_variable_c1)
        self.entry_c1.grid(row=1, column=4)

        self.text_variable_a2 = tk.DoubleVar(parent)
        self.entry_a2 = tk.Entry(parent, textvariable=self.text_variable_a2)
        self.entry_a2.grid(row=2, column=0)

        self.label_text_a2 = tk.Label(parent, text="x + ")
        self.label_text_a2.grid(row=2, column=1)

        self.text_variable_b2 = tk.DoubleVar(parent)
        self.entry_b2 = tk.Entry(parent, textvariable=self.text_variable_b2)
        self.entry_b2.grid(row=2, column=2)

        self.label_text_b2 = tk.Label(parent, text="y = ")
        self.label_text_b2.grid(row=2, column=3)

        self.text_variable_c2 = tk.DoubleVar(parent)
        self.entry_c2 = tk.Entry(parent, textvariable=self.text_variable_c2)
        self.entry_c2.grid(row=2, column=4)

        def clicked():
            self.parametr = True

        self.button = tk.Button(parent, text="Oblicz!", command=clicked)
        self.button.grid(row=3, columnspan=5)