from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#------------------- Logic ---------------------#

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_word():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])




#------------------- FRONT CARD UI ---------------------#

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=next_word)
right_button.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button_button = Button(image=wrong_button_img, highlightthickness=0, command=next_word)
wrong_button_button.grid(row=1, column=0)



next_word()

window.mainloop()