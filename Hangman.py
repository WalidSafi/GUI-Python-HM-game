from tkinter import *
from tkinter import messagebox
import time

inputValue = ""
inputGuess = ""
failCounter = 0
strGuessedLetters = []
hiddenDisplay = []
blank = []
str1 = ""


def recieve_input():

    global hiddenDisplay
    global blank

    inputValue = textBox.get()
    inputValue = inputValue.lower()

    ind = 0
    blank = list(inputValue)
    for x in range(10):
        blank.append(" ")

    hiddenDisplay = list(inputValue)

    while ind <= (len(inputValue) * 2):

        if blank[ind].isalpha() or blank[ind].isdigit():

            blank.insert(ind + 1, " ")
            hiddenDisplay.insert(ind + 1, " ")
            blank[ind] = "_"

            if blank[ind] == " ":
                blank[ind] = " "
        ind = ind + 1

    c.itemconfig(head, fill="white", outline="")
    c.itemconfig(body, fill="white")
    c.itemconfig(leftArm, fill="white")
    c.itemconfig(rightArm, fill="white")
    c.itemconfig(leftLeg, fill="white")
    c.itemconfig(rightLeg, fill="white")

    gameWord.set(str1.join(blank))
    print(gameWord.get())


def Categorybutton():

    inputVal = catBox.get('1.0', END)
    var.set(inputVal)
    catBox.delete('1.0', END)
    catBox.update()

def check_solve():

    global blank

    if "_" in blank :
        print("Not done")
    else:
        messagebox.showinfo('You Win!', 'You Won Hangman!')
        time.sleep(1)
        reset()

def reset():

    global failCounter
    global strGuessedLetters

    c.itemconfig(head, fill="white", outline="")
    c.itemconfig(body, fill="white")
    c.itemconfig(leftArm, fill="white")
    c.itemconfig(rightArm, fill="white")
    c.itemconfig(leftLeg, fill="white")
    c.itemconfig(rightLeg, fill="white")

    failCounter = 0
    gameWord.set(str1.join("Hidden Word"))
    var.set(str1.join("Category"))
    used.set(str1.join("Used Letters"))
    strGuessedLetters = []
    print(strGuessedLetters)



def CharGuess():

    global failCounter
    global hiddenDisplay
    global blank
    global strGuessedLetters
    global correctCounter

    inputGuess = GuessTextBox.get('1.0', END)
    GuessTextBox.delete('1.0', END)
    inputGuess = inputGuess.lower()
    inputGuess = inputGuess[:-1]

    if len(inputGuess) > 1 or len(inputGuess) < 1 or len(blank) < 1:
        messagebox.showinfo('Invalid Guess', 'Please enter only One letter or check if a word is chosen')
    else:

        if inputGuess in strGuessedLetters:
            messagebox.showinfo('Invalid Guess', 'That Letter has already been guessed my dude')
        else:
             if inputGuess in hiddenDisplay:

                 for x in range(len(hiddenDisplay)):

                    if inputGuess == hiddenDisplay[x]:
                       blank[x] = inputGuess
                       gameWord.set(str1.join(blank))
             else:

                failCounter = failCounter + 1

                if failCounter == 1:
                    c.itemconfig(head, fill="black", outline="")
                elif failCounter == 2:
                    c.itemconfig(body, fill="black")
                elif failCounter == 3:
                    c.itemconfig(leftArm, fill="black")
                elif failCounter == 4:
                    c.itemconfig(rightArm, fill="black")
                elif failCounter == 5:
                    c.itemconfig(leftLeg, fill="black")
                elif failCounter == 6:
                    c.itemconfig(rightLeg, fill="black")
                    messagebox.showinfo('You have lost!', 'you guessed incorrectly too many times, the poor man has been hung')


             strGuessedLetters.append(inputGuess)
             strGuessedLetters.append(" ")
             used.set(str1.join(strGuessedLetters))
             print(strGuessedLetters)

             check_solve()

             if failCounter >= 6 :
                 reset()

    GuessTextBox.update()


root = Tk()

root.geometry('1500x900')

var = StringVar(value="Category")
gameWord = StringVar(value="Hidden Word ")
used = StringVar(value="Used Letters")

c = Canvas(root, height=1300, width=1500, bg="white")
c.pack(fill=BOTH, expand=YES)

title = Label(c, height=3, text="Hint: ", textvariable=var, font="Times 16 ", background="white").pack()

photo = PhotoImage(file="hg2.png")

c.create_image(0, 125, image=photo, anchor=NW)

head = c.create_oval(410, 260, 470, 310, fill="white", outline="")
body = c.create_line(440, 310, 440, 500, fill="white", width=4)
leftArm = c.create_line(430, 330, 400, 400, fill="white", width=3)
rightArm = c.create_line(450, 330, 480, 400, fill="white", width=3)
leftLeg = c.create_line(435, 505, 390, 550, fill="white", width=3)
rightLeg = c.create_line(445, 505, 500, 550, fill="white", width=3)


inputPrompt= Label(c, height=2, text="Enter the word for the game: ", background="white", font="Times 16 ").place(x=900, y=50)

textBox = Entry(c, show="*", width=20, font="Times 20", background="white")
textBox.place(x=1150, y=60)

catPrompt = Label(c, height=2, text="Category: ", background="white", font="Times 14 ").place(x=500, y=50)

catBox = Text(c, height=2, width=20, background="white")
catBox.place(x=600, y=60)

buttonCommit = Button(c, height=1, width=20, text="Confirm", command=lambda: recieve_input()).place(x=1200, y=120)
buttonCat = Button(c, height=1, width=20, text="Confirm Category", command=Categorybutton).place(x=600, y=120)

hiddenWord = Label(c, textvariable=gameWord, height=10, width=40, font="Times 30").place(x=600, y=200)

GuessTextBox = Text(c, height=0, width=10, font="Times 20", background="silver")
GuessTextBox.place(x=650, y=700)
buttonGuess = Button(c, height=4, width=19, text="Guess Letter!", command=CharGuess).place(x=650, y=750)

guessed_letters_display = Label(c, textvariable=used, height=3, width=30, font="Times 30").place(x=820, y=700)

root.mainloop()

