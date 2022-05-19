import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from math import *


def draw_circle1(posx, posy, radius):
    sides = 32
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()


def init():
    pygame.init()
    display = (900, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.6, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(10, -10)
    glVertex2f(10, 10)
    glVertex2f(-10, 10)
    glVertex2f(-10, -10)
    glEnd()

    glColor3f(0.5, 0.7, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(10, 0)
    glVertex2f(10, 10)
    glVertex2f(-10, 10)
    glVertex2f(-10, 0)
    glEnd()
    # hotel
    glColor3f(0.0, 0.71, 0.58)
    # glColor3f(0.50, 0.71, 0.98)
    glBegin(GL_POLYGON)

    glVertex2f(5.50, -4.00)
    glVertex2f(5.50, 3.30)
    glVertex2f(9.50, 3.30)
    glVertex2f(9.50, -4.00)

    glEnd()

    glBegin(GL_POLYGON)

    glColor3f(0, 0, 0)
    glVertex2f(9.50, 3.30)
    glVertex2f(5.50, 3.30)
    glVertex2f(5.70, 3.70)
    glVertex2f(9.80, 3.70)

    glEnd()

    glBegin(GL_POLYGON)

    glVertex2f(9.50, -4.00)
    glVertex2f(9.50, 3.30)
    glVertex2f(9.80, 3.70)
    glVertex2f(9.80, -3.70)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(6.50, 2.70)
    glVertex2f(6.50, 3.30)
    glVertex2f(8.50, 3.30)
    glVertex2f(8.50, 2.70)

    glEnd()

    # window

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(8.50, -2.00)
    glVertex2f(8.50, -1.1)
    glVertex2f(9.30, -1.1)
    glVertex2f(9.30, -2.00)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(8.50, 0.5)
    glVertex2f(8.50, -0.4)
    glVertex2f(9.30, -0.4)
    glVertex2f(9.30, 0.5)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(5.70, 0.5)
    glVertex2f(5.70, -0.4)
    glVertex2f(6.50, -0.4)
    glVertex2f(6.50, 0.5)
    glEnd()

    glBegin(GL_POLYGON)

    glVertex2f(5.70, -2.00)
    glVertex2f(5.70, -1.1)
    glVertex2f(6.50, -1.1)
    glVertex2f(6.50, -2.00)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(5.70, 2.00)
    glVertex2f(5.70, 1.1)
    glVertex2f(6.50, 1.1)
    glVertex2f(6.50, 2.00)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(8.50, 2.00)
    glVertex2f(8.50, 1.1)
    glVertex2f(9.30, 1.1)
    glVertex2f(9.30, 2.00)
    glEnd()

    # door
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(8.00, -4.00)
    glVertex2f(8.00, -3.20)
    glVertex2f(7.00, -3.20)
    glVertex2f(7.00, -4.00)

    glEnd()

    glColor3f(0.35, 0.0, 0.0)
    glBegin(GL_POLYGON)

    glVertex2f(7.40, -4.20)
    glVertex2f(7.40, -3.00)
    glVertex2f(6.90, -3.20)
    glVertex2f(6.90, -4.00)

    glEnd()

    # hotel2
    glColor3f(0.0, 0.71, 0.58)
    # glColor3f(0.50, 0.71, 0.98)
    glBegin(GL_POLYGON)

    glVertex2f(-9.50, -4.00)
    glVertex2f(-9.50, 3.30)
    glVertex2f(-5.50, 3.30)
    glVertex2f(-5.50, -4.00)

    glEnd()

    glBegin(GL_POLYGON)

    glColor3f(0, 0, 0)
    glVertex2f(-5.50, 3.30)
    glVertex2f(-9.50, 3.30)
    glVertex2f(-9.30, 3.70)
    glVertex2f(-5.30, 3.70)

    glEnd()

    glBegin(GL_POLYGON)

    glVertex2f(-5.50, -4.00)
    glVertex2f(-5.50, 3.30)
    glVertex2f(-5.30, 3.70)
    glVertex2f(-5.30, -3.70)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(-8.50, 2.70)
    glVertex2f(-8.50, 3.30)
    glVertex2f(-6.50, 3.30)
    glVertex2f(-6.50, 2.70)

    glEnd()

    # window

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(-6.50, -2.00)
    glVertex2f(-6.50, -1.1)
    glVertex2f(-5.80, -1.1)
    glVertex2f(-5.80, -2.00)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(-6.50, 0.5)
    glVertex2f(-6.50, -0.4)
    glVertex2f(-5.80, -0.4)
    glVertex2f(-5.80, 0.5)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(-9.30, 0.5)
    glVertex2f(-9.30, -0.4)
    glVertex2f(-8.50, -0.4)
    glVertex2f(-8.50, 0.5)
    glEnd()

    glBegin(GL_POLYGON)

    glVertex2f(-9.30, -2.00)
    glVertex2f(-9.30, -1.1)
    glVertex2f(-8.50, -1.1)
    glVertex2f(-8.50, -2.00)
    glEnd()
    glBegin(GL_POLYGON)

    glVertex2f(-9.30, 2.00)
    glVertex2f(-9.30, 1.1)
    glVertex2f(-8.50, 1.1)
    glVertex2f(-8.50, 2.00)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(-6.50, 2.00)
    glVertex2f(-6.50, 1.1)
    glVertex2f(-5.80, 1.1)
    glVertex2f(-5.80, 2.00)
    glEnd()

    # door
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)

    glVertex2f(-7.00, -4.00)
    glVertex2f(-7.00, -3.20)
    glVertex2f(-8.00, -3.20)
    glVertex2f(-8.00, -4.00)

    glEnd()

    glColor3f(0.35, 0.0, 0.0)
    glBegin(GL_POLYGON)

    glVertex2f(-7.60, -4.20)
    glVertex2f(-7.60, -3.00)
    glVertex2f(-8.30, -3.20)
    glVertex2f(-8.30, -4.00)

    glEnd()

    # store
    glColor3f(0.0, 0.71, 0.58)
    glBegin(GL_POLYGON)

    glVertex2f(-1.50, -4.00)
    glVertex2f(-1.50, -1.30)
    glVertex2f(4.50, -1.30)
    glVertex2f(4.50, -4.00)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(4.50, -4.00)
    glVertex2f(4.50, -1.30)
    glVertex2f(4.80, -0.9)
    glVertex2f(4.80, -3.70)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-1.50, -1.30)
    glVertex2f(4.50, -1.30)
    glVertex2f(4.80, -0.9)
    glVertex2f(-1.20, -0.9)
    glEnd()

    # sun
    glColor3f(1, 0.9, 0.0)
    draw_circle1(-8, 7, 1)

    # cloud
    glColor3f(0.9, 0.9, 0.9)
    draw_circle1(-5.5, 7, 1)
    draw_circle1(-3.8, 7, 1)
    draw_circle1(-4.4, 8, 1)

    draw_circle1(-0.5, 7, 1)
    draw_circle1(0.8, 7, 1)
    draw_circle1(0.4, 8, 1)
    draw_circle1(1.5, 8.1, 1)
    draw_circle1(1.7, 7.1, 1)

    draw_circle1(5.5, 7, 1)
    draw_circle1(6.8, 7, 1)
    draw_circle1(6.4, 8, 1)
    draw_circle1(7.5, 8.1, 1)
    draw_circle1(7.7, 7.1, 1)

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(-1.30, -3.80)
    glVertex2f(-1.30, -1.50)
    glVertex2f(2.50, -1.50)
    glVertex2f(2.50, -3.80)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0, -3.80)
    glVertex2f(0, -1.50)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2f(1.30, -3.80)
    glVertex2f(1.30, -1.50)
    glEnd()

    # door
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(4.00, -4.00)
    glVertex2f(4.00, -3.20)
    glVertex2f(3.00, -3.20)
    glVertex2f(3.00, -4.00)
    glEnd()

    glColor3f(0.35, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(3.40, -4.20)
    glVertex2f(3.40, -3.00)
    glVertex2f(2.90, -3.20)
    glVertex2f(2.90, -4.00)
    glEnd()

    glColor3f(0.73, 0.71, 0.2)
    glBegin(GL_POLYGON)

    glVertex2f(-2.20, -4.00)
    glVertex2f(-2.20, -3.30)
    glVertex2f(-2.0, -3.30)
    glVertex2f(-2.0, -4.00)
    glEnd()

    glColor3f(0.0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-2.40, -3.30)
    glVertex2f(-1.8, -3.30)
    glVertex2f(-2.1, -2.30)
    glVertex2f(-2.1, -2.30)
    glEnd()

    glColor3f(0.165, 0.161, 0.133)
    glBegin(GL_POLYGON)
    glVertex2f(-10, -9.0)
    glVertex2f(-10, -5.0)
    glVertex2f(10, -5)
    glVertex2f(10, -9)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(-9, -7.2)
    glVertex2f(-9, -6.9)
    glVertex2f(-6, -6.9)
    glVertex2f(-6, -7.2)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(-4, -7.2)
    glVertex2f(-4, -6.9)
    glVertex2f(-1, -6.9)
    glVertex2f(-1, -7.2)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex2f(1, -7.2)
    glVertex2f(1, -6.9)
    glVertex2f(4, -6.9)
    glVertex2f(4, -7.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(6, -7.2)
    glVertex2f(6, -6.9)
    glVertex2f(9, -6.9)
    glVertex2f(9, -7.2)
    glEnd()

    # streetlight

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(-8, -5.0)
    glVertex2f(-8, -2.0)
    glVertex2f(-8.2, -2)
    glVertex2f(-8.2, -5)
    glEnd()

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(-1, -5.0)
    glVertex2f(-1, -2.0)
    glVertex2f(-1.2, -2)
    glVertex2f(-1.2, -5)
    glEnd()

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex2f(6, -5.0)
    glVertex2f(6, -2.0)
    glVertex2f(6.2, -2)
    glVertex2f(6.2, -5)
    glEnd()
    glColor3f(1, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2f(6.2, -2)
    glVertex2f(6, -2.0)
    glVertex2f(5.8, -3)
    glVertex2f(6.4, -3)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-1.2, -2)
    glVertex2f(-1, -2.0)
    glVertex2f(-0.8, -3)
    glVertex2f(-1.4, -3)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-8.2, -2)
    glVertex2f(-8, -2.0)
    glVertex2f(-7.8, -3)
    glVertex2f(-8.4, -3)
    glEnd()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
