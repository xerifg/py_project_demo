import sys
import pygame

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
color = (20, 20, 200)

ball = pygame.image.load("pig.png")
ballrect = ball.get_rect()

speed = [5, 5]
clock = pygame.time.Clock()

while True:
    clock.tick(60)  # run 60 times per second
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game Over")
            sys.exit()
    # move ball
    ballrect = ballrect.move(speed)
    # Touch the left and right edges
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # Touch the top and bottom edges
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)  # filling color
    screen.blit(ball, ballrect)  # Drawing the picture to the window
    pygame.display.flip()  # Update all displays

# pygame.quit()
