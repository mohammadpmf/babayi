from turtle import *
shape = textinput("?", "Enter Shape:")
c = textinput("?", "Enter color:")
s = numinput("?", "Enter size:")
color(c)
begin_fill()
if shape == 'circle':
    circle(s)
else:
    for i in range(4):
        fd(s)
        lt(90)
end_fill()
done()