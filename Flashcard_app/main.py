from tkinter import *
import pandas
import random

import pandas as pd

FONT_BOLD = ("ARIEL",60,"bold")
FONT = ("ARIEL",40,"italic")
BACKGROUND_COLOR = "#B1DDC6"


#Generate Random Word#
try: words_csv = pandas.read_csv("known_words.csv")  #data/french_words2.csv

except FileNotFoundError:
    words_csv = pandas.read_csv("data/french_words.csv")

to_learn = pandas.DataFrame.to_dict(words_csv, orient="records")
current_card = {}
def next_word():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(languge_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text= current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card_image)
    flip_timer = screen.after(3000, func = flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(languge_canvas, fill="white" , text="English" )
    canvas.itemconfig(word_canvas, fill="white", text= current_card["English"])

def known_word():
    global current_card, to_learn
    to_learn.remove(current_card)
    known_words_csv = pandas.DataFrame(to_learn)
    known_words_csv.to_csv("known_words.csv", index=False)
    next_word()



#screen#
screen = Tk()
screen.title("GO GO HANGUL")
screen.config(padx=50 , pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = screen.after(3000, func=flip_card)
# YES/NO BUTTON#
yes_image = PhotoImage(file="images/right.png")
yes_button = Button (image=yes_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=known_word)
yes_button.grid(column= 0, row= 1)
no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_word)
no_button.grid(column= 1, row= 1)


#canvas#
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(800/2,526/2, image=front_card_image)
languge_canvas = canvas.create_text(400, 150 , text="French" , fill="black" ,font=(FONT))
word_canvas = canvas.create_text(400,263, text="네", fill="black",font=(FONT_BOLD))
canvas.grid(column= 0, row= 0, columnspan=2)

next_word()

mainloop()