class Circle():
    radius = 0
    x = 0
    y = 0
    color = ""
    filled = False


circles = []

for x in range (0,10):
    c = Circle()
    c.radius = int(input("Enter the circle radius: "))
    circles.append(c)


print(circles[6].radius)