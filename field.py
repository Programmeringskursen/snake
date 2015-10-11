import pygame

class Field():
    fieldColor = (0, 50, 0)

    def __init__(self, screen, width, height, blockSize):
        self.screen = screen
        self.width = width
        self.height = height
        self.blockSize = blockSize

    def draw(self):
        self.screen.fill(self.fieldColor)
