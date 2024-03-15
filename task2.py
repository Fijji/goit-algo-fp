import turtle

def pifagor_tree(t, order, size):
    if order == 0:
        return
    else:
        t.forward(size)
        t.left(45)
        pifagor_tree(t, order - 1, size * 0.7)
        t.right(90)
        pifagor_tree(t, order - 1, size * 0.7)
        t.left(45)
        t.backward(size)

def draw_it(size=200, level=None):
    if level is None:
        level = int(input("Вкажіть рівень рекурсії (за замовчуванням 3): ") or 3)

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    
    t.speed(0)
    t.penup()
    t.goto(0, -size / 2)
    t.pendown()
    t.left(90)
    pifagor_tree(t, level, size)

    window.mainloop()

draw_it()