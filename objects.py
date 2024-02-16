import Circle as c, drawcircle as d, pygame

#The looping variable to keep our game running
running = True

#Setup and initialize the pygame library
d.setup()


while running:
    ev = pygame.event.get() #capture user input

    for event in ev:

        if event.type == pygame.MOUSEBUTTONUP:
            #Mouse was clicked and released, draw circle here!
            #Get the mouse cursor position
            pos = pygame.mouse.get_pos()

            #instantiate a circle and populate it's values
            c1 = c.Circle()
            c1.radius = 25
            c1.coords.x = pos[0]
            c1.coords.y = pos[1]
            c1.color = "blue"
            c1.filled = True


            #Draw the circle to the screen
            d.drawCircle(c1)
            pygame.display.update()

        if event.type == pygame.QUIT:
            running = False