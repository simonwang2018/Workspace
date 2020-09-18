import turtle
t = turtle.Pen()
for x in range(360):
    t.forward(x)
    t.left(80)
turtle.done() #在pycharm加了这条命令不会使turtle窗口一闪即逝