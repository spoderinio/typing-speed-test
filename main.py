from msilib.schema import Font
import tkinter as tk
import random
import tkinter
from tkinter.ttk import Label
from PIL import ImageTk, Image
from pyparsing import col


f = open("words_en.txt", "r")
wlen = f.readlines()
f.close()

f_bg = open("words_bg.txt", "r")
wlbg = f_bg.readlines()
f_bg.close()


# FUNTIONALLITY #####################e

def choose_language():
    if clicked.get() == "English":
        global word_list_en
        word_list = []
        for word in wlen:
            word_list.append(word.replace("\n", ""))

    else:
        global word_list_bg
        word_list = []
        for word in wlbg:
            word_list.append(word.replace("\n", ""))
        word_list = list(dict.fromkeys(word_list))
    random.shuffle(word_list)
    start_words.insert(tkinter.END, word_list)
    start_words.config(state=tk.DISABLED)
    return word_list


def test_score():
    usr_words = usr_entry.get("1.0", tk.END)
    usr_words = usr_words.split()
    usr_score = set(usr_words).intersection(choose_language())
    print(len(usr_score))


def start_test():
    usr_entry.focus_set()


###################### USR INTERFACE ###############################

window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(300, 720)
window.config(bg="#4AC3BE")

img = ImageTk.PhotoImage(Image.open("logo.PNG"))
panel = Label(window, image=img)
panel.grid(row=0, column=0, columnspan=3)

options = ["English", "Български"]

clicked = tk.StringVar()
clicked.set(options[0])

option = tk.OptionMenu(window, clicked, *options)
option.config(bg="#E6EFBF")
option["highlightthickness"] = 0
option.grid(row=2, column=0)

start_words = tk.Text(window, wrap=tk.WORD, height=10, width=80, font="Ubuntu")
start_words.grid(row=3, column=0, rowspan=2, columnspan=2)

############### LABELS ########################

choose_lang_lable = tk.Label(
    text="Choose language/Изберете език", background="#4AC3BE").grid(row=1, column=0)

timer_label = tk.Label(window, text=f"Timer:",
                       background="#4AC3BE").grid(row=4, column=2, padx=(0, 20))


################ ENTRYS ########################


usr_entry = tk.Text(window, wrap=tk.WORD, height=10,
                    width=80, font="Ubuntu", bg="#E6EFBF")
usr_entry.grid(row=5, column=0, rowspan=2, columnspan=2,
               padx=(10, 10), pady=(10, 10))

#################### BUTTONS ########################

check_button = tk.Button(window, text="Check score",
                         command=test_score, bg="#E6EFBF").grid(row=5, column=2)

start_button = tk.Button(window, text="Start",
                         command=start_test, bg="#E6EFBF").grid(row=3, column=2)

select_button = tk.Button(window, text="Select",
                          command=choose_language, bg="#E6EFBF").grid(row=2, column=1)


window.mainloop()
