from my_tkinter import *
from compute import *
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = Window(root, False)
    root.mainloop()

    if my_gui.parametr:
        compute = LinearEquations(float(my_gui.text_variable_a1.get()),
                                  float(my_gui.text_variable_b1.get()),
                                  float(my_gui.text_variable_c1.get()),
                                  float(my_gui.text_variable_a2.get()),
                                  float(my_gui.text_variable_b2.get()),
                                  float(my_gui.text_variable_c2.get()))

        bool_var = compute.is_compute()

        if bool_var:
            co_ordinates = compute.equal_equations_linear()
        else:
            string_var = compute.equal_equations_linear()

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        x = np.linspace(-5, 5, 100)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        num_1 = -1 * float(my_gui.text_variable_a1.get()) / float(
            my_gui.text_variable_b1.get())
        free_word_1 = float(my_gui.text_variable_c1.get()) / float(
            my_gui.text_variable_b1.get())
        num_2 = -1 * float(my_gui.text_variable_a2.get()) / float(
            my_gui.text_variable_b2.get())
        free_word_2 = float(my_gui.text_variable_c2.get()) / float(
            my_gui.text_variable_b2.get())
        plt.plot(x,
                 num_1 * x + free_word_1,
                 '-r',
                 label='{a1}x + {b1}y = {c1}'.format(
                     a1=my_gui.text_variable_a1.get(),
                     b1=my_gui.text_variable_b1.get(),
                     c1=my_gui.text_variable_c1.get()))
        plt.plot(x,
                 num_2 * x + free_word_2,
                 '-g',
                 label='{a2}x + {b2}y = {c2}'.format(
                     a2=my_gui.text_variable_a2.get(),
                     b2=my_gui.text_variable_b2.get(),
                     c2=my_gui.text_variable_c2.get()))
        plt.legend(loc='upper left')
        plt.show()
