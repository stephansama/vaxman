# Here is your task
#
# Python is an excellent choice
# for the initial development of
# various applications, including games.
# In this task you need to do the following:
#
# STEP 1 ====================================
#
# Review open-source Python Pac-Man implementations.
# We've included a couple of them for reference in the
# Resources below, but you can use any open-source
# Python implementation. We've also included a primer on PyGame.
#
# STEP 2 ====================================
#
# Pick one of the open-source implementations and download it.
#
# STEP 3 ====================================
#
# Modify it based on the rules of Vax-Man (see above).
#
# STEP 4 ====================================
#
# Go to 'Submit your work' below and upload your modified code.
# This will be your deliverable for this task.
#
# NB: if you would like some help during the task,
# you can use the Python code attached in
# the Resources section below ('Python Code With Suggestions').
# In the Python code with suggestions,
# we have highlighted the places where you need to make changes.
#
# (For reference, the original code can be found here: https://github.com/hbokmann/Pacman.)
#
# When making the modification in the code keep in mind
# that the main difference between Pac-Man and Vax-man is that,
# in Vax-man, ghosts have the ability to double and ghosts can be killed.
# As a result, the number of ghosts varies during the game depending on the circumstances,
# and you need to keep track of arrays of ghosts.


import pygame
import sys
from pygame.locals import *

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


pygame.init()


fpsClock = pygame.time.Clock()

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')


def main():
    looping = True

    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # render
        WINDOW.fill(BACKGROUND)
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
