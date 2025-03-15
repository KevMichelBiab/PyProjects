import pygame
"""import random

pygame.init() #initialize the python module
window = pygame.display.set_mode((640, 480)) #Set the size of the window

robot = pygame.image.load('robot.png')
width = robot.get_width();
height = robot.get_height();
window.fill((0,0,0)) #Make the window black


for _ in range(1000):
    x = random.randint(0, 640 - width)  # Random x coordinate (must fit in the window)
    y = random.randint(0, 480 - height)  # Random y coordinate (must fit in the window)
    window.blit(robot, (x, y))  # Draw the robot at the random position
    

pygame.display.flip() # Make sure the contents is being updated as we add things

while True:
    for event in pygame.event.get(): # Return a list of events that happened since the last iteration
        if event.type == pygame.QUIT: # pygame.QUIT is the even being triggered and it is triggered when we press on the exit button of the window
            exit() # When the even is triggered then we exit the function
"""

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()

to_right = False
to_left = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 2
    if to_left:
        x -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)

