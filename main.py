from msilib.schema import Font
import tkinter as tk
import random
import tkinter


f = open("words_en.txt", "r")
wlen = f.readlines()
f.close()

f_bg = open("words_bg.txt", "r")
wlbg = f_bg.readlines()
f_bg.close()


def choose_language():
    if clicked.get() == "English":
        global word_list_en
        word_list_en = []
        for word in wlen:
            word_list_en.append(word.replace("\n", ""))
        random.shuffle(word_list_en, random.random)
        T = tk.Text(window, wrap=tk.WORD, height=17, width=100, font="Ubuntu")
        T.grid(row=3, column=0)
        T.insert(tkinter.END, word_list_en)

    else:
        global word_list_bg
        word_list_bg = []
        for word in wlbg:
            word_list_bg.append(word.replace("\n", ""))
        word_list_bg = list(dict.fromkeys(word_list_bg))
        random.shuffle(word_list_bg, random.random)
        T = tk.Text(window, wrap=tk.WORD, height=17, width=100, font="Ubuntu")
        T.grid(row=3, column=0)
        T.insert(tkinter.END, word_list_bg)


def test_score():
    usr_words = usr_entry.get("1.0", tk.END)
    usr_words = usr_words.split()
    usr_score = set(usr_words).intersection(word_list_bg)
    print(len(usr_score))


window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(300, 720)
window.config(bg="#4AC3BE")

options = ["English", "Български"]

clicked = tk.StringVar()
clicked.set(options[0])
choose_lang_lable = tk.Label(
    text="Choose language/Изберете език", background="#4AC3BE").grid(row=0, column=0)
option = tk.OptionMenu(window, clicked, *options)
option.config(bg="#E6EFBF")
option["highlightthickness"] = 0
option.grid(row=1, column=0)

select_button = tk.Button(window, text="Select",
                          command=choose_language, bg="#E6EFBF").grid(row=2, column=0)

usr_entry = tk.Text(window, wrap=tk.WORD, height=17,
                    width=100, font="Ubuntu", bg="#E6EFBF")
usr_entry.grid(row=4,
               column=0)

check_button = tk.Button(window, text="Check score",
                         command=test_score, bg="#E6EFBF").grid(row=5, column=0)


window.mainloop()
