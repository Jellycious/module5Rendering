from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random
import sys
import time

import Shapes

spheres = []
window_width = 1000
window_height = 1000
pause = False
clear_screen = True
running = True
fps = 0
lightZeroPosition = [0., 4., 10, 1.]
lightZeroColor = [0.8, 1.0, 0.8, ]  # green tinged


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000,1000)
    glutCreateWindow(b'spheres')
    glutKeyboardFunc(key_pressed)
    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(90.,1.,1.,100.)
    gluLookAt(0, 0, 20,
              0, 0, 0,
              0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutMainLoop()
    return


# This is run everytime the frame is redrawn
old_time = time.time()


def display():
    global old_time
    if running:
        global clear_screen
        global pause
        if clear_screen:
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        # draw stuff here
        render()
        # ----------------
        glPopMatrix()
        new_time = time.time()
        # 120 up/s
        if (new_time - old_time) > (1/120):
            old_time = new_time
            if not pause:
                update()
        glutSwapBuffers()
        glutPostRedisplay()
    else:
        exit(0)


frame_count = 0
frame_time = time.time()


def render():
    global fps
    global frame_count
    global frame_time
    frame_count += 1
    for sphere in spheres:
        draw_sphere(sphere)
    # One second has passed
    curr_time = time.time()
    if curr_time - frame_time >= 1:
        frame_count = 0
        frame_time = curr_time;


def update():
    glRotate(1, 0, 1, 0)


def move_object(to_move):
    coordinates = to_move.get_coordinates()
    direction = to_move.get_direction_matrix()
    new_coordinates = []
    for i in range(len(coordinates)):
        new_coordinates.append(coordinates[i] + direction[i])
    to_move.set_coordinates(new_coordinates)


def key_pressed(key, x, y):
    global spheres
    if key == b'o':
        save_image()
    if key == b'n':
        spheres = []
        for x in range(25):
            sphere = random_sphere()
            spheres.append(sphere)
    if key == b'+':
        sphere = random_sphere()
        spheres.append(sphere)

    if key == b'-':
        if len(spheres) > 0:
            spheres.pop(len(spheres) - 1)

    if key == b'c':
        global clear_screen
        if clear_screen:
            clear_screen = False
        else:
            clear_screen = True

    if key == b'p':
        global pause
        if pause:
            pause = False
        else:
            pause = True

    if key == b'\x1b':
        global running
        running = False


def draw_sphere(sphere):
    coordinates = sphere.get_coordinates()
    colour = sphere.get_colour()
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, colour)
    glTranslatef(coordinates[0], coordinates[1], coordinates[2])
    glutSolidSphere(sphere.get_radius(), sphere.get_slices(), sphere.get_stacks())
    glTranslatef(-coordinates[0], -coordinates[1], -coordinates[2])


def draw_edge_object(edge_object):
    colour = edge_object.get_colour()
    edges = edge_object.get_edges()
    verticies = edge_object.get_verticies()
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, colour)
    glBegin(GL_LINES)
    for index, edge in enumerate(edges):
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def random_sphere():
    r = random.random()
    g = random.random()
    b = random.random()
    x = random.randint(0, 10) * (random.random() * 2 - 1)
    y = random.randint(0, 10) * (random.random() * 2 - 1)
    z = random.randint(0, 10) * (random.random() * 2 - 1)
    sphere = Shapes.Sphere(1, 20, 20, (x, y, z), (r, g, b),(0, 0, 0))
    return sphere


def save_image():
    data = glReadPixels(0, 0, window_width, window_height, GL_RGB, GL_UNSIGNED_BYTE)
    render_image_to_file("test.png", data)


def render_image_to_file(filename, data, file_format="PNG"):
    from PIL import Image
    pixel_format = 'RGB'
    image = Image.frombytes(pixel_format, (window_width, window_height), data)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(filename, file_format)
    print('Saved image to' + (os.path.abspath(filename)))
    return image


main()
