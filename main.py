from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    words_to_learn = data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def remove_word():
    global current_card, words_to_learn
    words_to_learn.remove(current_card)
    df = pandas.DataFrame(words_to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card
    canvas.itemconfig(canvas_img, image=front_card_img)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.update()
    window.after(3000, func=flip_card())


def flip_card():
    global current_card
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- UI --------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 260, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 35, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 55, "bold"))

# Buttons
right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)

left_button_img = PhotoImage(file="./images/wrong.png")
left_button = Button(image=left_button_img, highlightthickness=0, command=next_card)
left_button.grid(column=0, row=1)

next_card()

window.mainloop()
