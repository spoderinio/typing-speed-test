import tkinter as tk
import random
import tkinter
from tkinter.ttk import Label


f = open("words_en.txt", "r")
wlen = f.readlines()
f.close()

f_bg = open("words_bg.txt", "r")
wlbg = f_bg.readlines()
f_bg.close()


def choose_language():
    if clicked.get() == "English":
        word_list_en = []
        for word in wlen:
            word_list_en.append(word.replace("\n", ""))
        r_word_list_en = random.choices(word_list_en, k=200)
        T = tk.Text(window, wrap=tk.WORD, height=17, width=100)
        T.pack()
        T.insert(tkinter.END, r_word_list_en)

    else:
        word_list_bg = []
        for word in wlbg:
            word_list_bg.append(word.replace("\n", ""))

        def my_function(x):
            return list(dict.fromkeys(x))
        word_list_bg = my_function(word_list_bg)
        r_word_list_bg = random.choices(word_list_bg, k=200)
        T = tk.Text(window, wrap=tk.WORD, height=17, width=100)
        T.pack()
        T.insert(tkinter.END, r_word_list_bg)


window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(1080, 720)

options = ["English", "Български"]

clicked = tk.StringVar()
clicked.set(options[0])
choose_lang_lable = Label(text="Choose language/Изберете език").pack()
option = tk.OptionMenu(window, clicked, *options).pack(pady=20)

select_button = tk.Button(window, text="Select",
                          command=choose_language).pack()


window.mainloop()
