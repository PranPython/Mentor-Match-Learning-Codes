import turtle as t
import time
pen=t.Turtle()
c=t.Screen()
c.bgcolor("Black")
pen.color("Red")
ans = t.Turtle()
pen.penup()
pen.goto(-70,350)
pen.write("---Menu---",font=("Arial",30,"bold"))
pen.goto(0,200)
pen.write("1. Add a word and meaning",font=("Arial",25,"bold"),align="center")
pen.goto(0,160)
pen.write("2. View all words",font=("Arial",25,"bold"),align="center")
pen.goto(0,120)
pen.write("3. View a word",font=("Arial",25,"bold"),align="center")
pen.goto(0,80)
pen.write("4. Delete a Word",font=("Arial",25,"bold"),align="center")
pen.goto(0,40)
pen.write("5. Exit",font=("Arial",25,"bold"),align="center")
pen.goto(0,0)
pen.write("Select an option",font=("Arial",25,"bold"),align="center")
d = {}

Q = t.numinput("Enter","Enter the number of what you want to do(1-5)")
while True:
    if Q == 1:
        word = t.textinput("Enter","Enter the Word")
        meaning = t.textinput("Enter","Enter The Meaning")
        d[word]=meaning
        ans.goto(0,-100)
        ans.write(("The word has been added"),font=("Arial",25,"bold"),align="center")
        time.sleep(3)
        ans.clear()
        break
    elif Q == 2:
        for i,j in d.items():
            pen.write((i,j),font=("Arial",25,"bold"),align="center")
    elif Q == 5:
        break
















c.mainloop()
