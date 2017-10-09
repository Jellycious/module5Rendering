import pygame
import time
import random
from OpenGL.GL import *
from OpenGL.GLU import *

oldTime = 0
colour_delta = 0.01
colours = []
verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def cube():

    global colours
    global colour_delta

    for index, colour in enumerate(colours):
        r = colour[0] + colour_delta
        g = colour[1] + colour_delta
        b = colour[2] + colour_delta
        if r > 1:
            r = 0
        if g > 1:
            g = 0
        if b > 1:
            b = 0

        colour = (r, g, b)
        colours[index] = colour
    glBegin(GL_LINES)
    for index, edge in enumerate(edges):
        glColor3f(float(colours[index][0]), float(colours[index][1]), float(colours[index][2]))
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def new_colours():
    global colours
    new_colours = []
    for x in range(len(edges)):
        r = random.random()
        g = random.random()
        b = random.random()
        new_colours.append((r, g, b))
    print(new_colours)
    colours = new_colours


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)


new_colours()
main()
