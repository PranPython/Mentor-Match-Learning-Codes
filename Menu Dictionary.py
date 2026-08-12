import turtle as t
import time
pen=t.Turtle()
c=t.Screen()
c.bgcolor("Black")
pen.color("Red")
ans = t.Turtle()
ans.penup()
ans.color("Red")
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
def quest():
    return t.numinput("Enter","Enter the number of what you want to do(1-5)")
while True:
    choice = quest()
    if choice == 1:
        w = t.textinput("Enter","Enter the Word")
        meaning = t.textinput("Enter","Enter The Meaning")
        d[w]=meaning
        ans.goto(0,-100)
        ans.write(("The word has been added"),font=("Arial",25,"bold"),align="center")
        time.sleep(3)
        ans.clear()
    elif choice == 2:
        y = -40
        for i,j in d.items():
            ans.goto(0,y)
            ans.write((i,j),font=("Arial",25,"bold"),align="center")
            time.sleep(5)
            ans.clear()
            y = y-40
    elif choice == 3:
        z = t.textinput("Enter","What word do you want to view")
        if z in d:
            ans.write((z,d[z]),font=("Arial",25,"bold"),align="center")
            time.sleep(3)
            ans.clear()
        else:
            ans.write("The word you searched is not in the dictionary",font=("Arial",25,"bold"),align="center")
            time.sleep(3)
            ans.clear()
    elif choice == 4:
        b = t.textinput("Enter","What word do you want to delete?")
        del d[b]
        ans.write(("The word has been deleted"),font=("Arial",25,"bold"),align="center")
        time.sleep(3)
        ans.clear()
    elif choice == 5:
        break
















c.mainloop()
