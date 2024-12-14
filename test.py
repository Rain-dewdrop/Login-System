import tkintertools as tkt
import tkintertools.animation as animation

root = tkt.Tk()
cv = tkt.Canvas(root)
cv.place(width=1280, height=720)

ball_1 = cv.create_oval(100, 100, 200, 200, fill="red", outline="")
ball_2 = cv.create_oval(100, 100+200, 200, 200+200, fill="green", outline="")
ball_3 = cv.create_oval(100, 100+400, 200, 200+400, fill="royalblue", outline="")

# animation.MoveItem(cv, ball_1, 1000, (840, 0), fps=60, controller=animation.flat).start(delay=1000)
# animation.MoveItem(cv, ball_2, 1000, (840, 0), fps=60, controller=animation.smooth).start(delay=1000)
# animation.MoveItem(cv, ball_3, 1000, (840, 0), fps=60, controller=animation.rebound).start(delay=1000)

root.mainloop()