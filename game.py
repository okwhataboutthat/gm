from tkinter import *
from tkinter import ttk
from random import choice
from random import shuffle
import pygame
from tkinter import colorchooser

window = Tk()
# window.geometry("600x400")
window.config(bg='#3C57FA')
window.resizable(FALSE, FALSE)
window.title('WORD JUMBLE GAME')
window.iconbitmap('attendance/teacher.ico')

mynotebook = ttk.Notebook(window)
mynotebook.pack()


def jump():
    mynotebook.hide(0)
    window.after(1500, shuffler)


def rules():
    mynotebook.select(0)
    window.after(1000, original_color)


#effect button welcome page


def style(e):
    welcome_button.config(bg='#0C8FFA', bd=2, font=('Arial', 27, 'bold'), text='START NEW GAME', cursor='dotbox')


def styler(e):
    welcome_button.config(bg='#359CDE', bd=0, font=('Arial', 25, 'bold'), text='start new game', cursor='mouse')


def class_style(e):
    welcome_label.config(text='WELCOME TO WORD JUMBLE GAME', font=('Arial', 25, 'bold'), bd=0.5)


def class_style1(e):
    welcome_label.config(text='welcome to word jumble game'.capitalize(), font=('Arial', 29, 'bold'),
                         bg='#3294FA', bd=0)


#frames
my_frame1 = Frame(mynotebook, width=510, height=500, bg='#3294FA')
my_frame1.pack(fill=BOTH, expand=1)
my_frame2 = Frame(mynotebook, width=500, height=500, bg='#429BFA')
my_frame2.pack(fill=BOTH, expand=1)

mynotebook.add(my_frame1, text="welcome_page")
mynotebook.add(my_frame2, text='win2')

welcome_label = Button(my_frame1, text='welcome to word jumble game'.capitalize(), font=('Arial', 32, 'bold'),
                       bg='#3294FA', bd=0)

#bind welcome_label
welcome_label.bind('<Enter>', class_style)
welcome_label.bind('<Leave>', class_style1)


welcome_label.pack(pady=20, ipady=5)
welcome_button = Button(my_frame1, text='start new game', command=jump, font=('Arial', 25, 'bold'),
                        activebackground='green')

welcome_button.pack(pady=20)
#binding event
welcome_button.bind('<Enter>', style)
welcome_button.bind('<Leave>', styler)

#frame2


def color():
    global my_color
    my_color = colorchooser.askcolor()[1]
    my_frame2.configure(background=str(my_color))
    window.after(1000, reset)
    window.after(1000, original_button.config(state=NORMAL, bg='#B565A7'))


def test():
    if my_color == my_color:
        color_button.config(bg=str(my_color),)
        my_label.config(bg=str(my_color))
        answer_label.config(bg=str(my_color))


def reset():
    fix_button.config(state=NORMAL, text='color🛠️'.capitalize(), bg='#B89E1D')


my_label = Label(my_frame2, text='', font=('Helvatica', 40), bg='#429BFA')
my_label.pack()

pygame.mixer.init()
pygame.init()
#shuffle function for new word


def shuffler():
    answer_button.config(state=NORMAL, text='answer')
    # button_hint.config(state=NORMAL, text='click for hint')
    # button.config(text='new word',)

    states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut",
              "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois",
              "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota",
              "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
              "New Jersey", "New Mexico", "Nevada", "New york", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
              "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia",
              "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    global word
    word = choice(states).lower()

    change = list(word)

    shuffle(change)

    global shuflled_word
    shuflled_word = ''

    for letter in change:
        shuflled_word += letter

    my_label.config(text=shuflled_word)
    entry.delete(0, END)
    answer_label.config(text='',)


def answer():

    window.after(2500, shuffler)
    if word == entry.get().lower():
        answer_label.config(text='nice well done 🤗 it is: '.capitalize() + (word).capitalize(), fg='#5B8564',
                            font=('Arial', 20, 'bold'))

        #pygame.mixer.music.load('attendance/douha.mp3')
        pygame.mixer.music.load('attendance/cheering.mp3')
        pygame.mixer.music.play()
        window.after(4000, stop)

    else:

        answer_label.config(text='try to focus more 😔\n maybe leave space between word!: '.capitalize(),
                            fg='#B43D31', font=('Arial', 17, 'bold'))

        pygame.mixer.music.load('attendance/boo.mp3')
        pygame.mixer.music.play()
        window.after(4000, stop)


#to remove the hint
def vanish():
    answer_label.config(text='')


def hint():
    answer_label.config(text='the word start with: ' + word[:3], fg='#1441E3')
    window.after(1300, vanish)


#creat hover effect function for new word
def enter(e):
    status_label.config(text='New word ', fg='black', font=('Arial', 12, 'bold'), anchor=E)


def leave(e):
    status_label.config(text='', fg='white', font=('Arial', 8, 'bold'))


#creat hover effect function for hint
def show(e):
    status_label.config(text='Hint! ', fg='black', font=('Arial', 12, 'bold'), anchor=E)


def remove(e):
    status_label.config(text='')


#creat hover effect function for answer

def apear(e):
    status_label.config(text='Answer ', fg='#429BFA', font=('Arial', 12, 'bold'), anchor=E)


def dont_apear(e):
    status_label.config(text='')


def stop():
    pygame.mixer.music.stop()


def activate():
    button_hint.config(state=DISABLED, text='click for hint')
    status_label.config(text='hard mode activated good luck', fg='#FF4F47', font=('Arial', 12, 'bold'), anchor=W)
    # window.after(1000, reset)


def deactivate():
    button_hint.config(state=NORMAL, text='click for hint')
    status_label.config(text='hard mode deactivated enjoy learning  '.capitalize(), fg='#1441E3',
                        font=('Arial', 12, 'bold'), anchor=E)
    # window.after(1000, hint)


def fix():
    fix_button.config(state=DISABLED, text='fix_color_bug', bg='white smoke')
    window.after(1000, test)
    my_label.config(fg='black')

    if my_color =='#000000':
        my_label.config(fg='white')
        answer_label.config(fg='white')
        color_button.config(fg='#34568B')


def timing_original():
    my_frame2.config(background='#429BFA')
    my_label.config(bg='#429BFA', fg='black')
    answer_label.config(bg='#429BFA', fg='black')
    original_button.config(state=DISABLED, activebackground='red', cursor='man',bg='white smoke')


def original_color():
    window.after(2000, timing_original)
    # my_frame2.config(background='#429BFA')
    # my_label.config(bg='#429BFA', fg='black')
    # answer_label.config(bg='#429BFA', fg='black')
    pass


#entry widget
entry = Entry(my_frame2, font=('Helvatica', 25, 'bold '))
entry.pack(pady=20)
answer_label = Label(my_frame2, text='', font=('Helvatica', 17, 'bold '), bg='#429BFA')
answer_label.pack(pady=10)
#BUTTONS
answer_button = Button(my_frame2, text='Answer', command=answer, state=DISABLED)
answer_button.pack(pady=10)

button = Button(my_frame2, text='new word'.capitalize(),  command=shuffler,)
button.pack(pady=10)

button_hint = Button(my_frame2, text='click for Hint', command=hint,)
button_hint.pack(pady=10)

hard_button = Button(my_frame2, text='hard mode'.capitalize(), command=activate, activebackground='red', bg='#FF4F47')
hard_button.place(x=0, y=310)

normal_button = Button(my_frame2, text='normal mode'.capitalize(), command=deactivate, state=NORMAL, bg='green')
normal_button.place(x=540, y=310)

front_button = Button(my_frame2, text='home 🏰'.upper(), command=rules, state=NORMAL, bg='#FAB74B',
                      cursor='heart')

front_button.place(x=5, y=10)

original_button = Button(my_frame2, text='reset_color', command=original_color, state=DISABLED, bg='white')
original_button.place(x=5, y=40)

color_button = Button(my_frame2, text='set color'.title(), bg='#429BFA', cursor='spraycan', command=color)
color_button.place(x=545, y=9)

fix_button = Button(my_frame2, text='fix_bugs'.capitalize(), command=fix, state=DISABLED, bg='white smoke')
fix_button.place(x=545, y=40)

#status
status_label = Label(my_frame2, text='', bd=1, relief=SUNKEN, anchor=E, bg='#ADD8E6')
status_label.pack(fill=X, side=BOTTOM, ipady=2)

#Hover effect
button.bind('<Enter>', enter)
button.bind('<Leave>', leave)
button_hint.bind('<Enter>', show)
button_hint.bind('<Leave>', remove)
answer_button.bind('<Enter>', apear)
answer_button.bind('<Leave>', dont_apear)


window.mainloop()
