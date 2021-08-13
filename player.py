import pygame


class Player(object):
    def __init__(self, x, y, width, height, colour):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.vel = 3
        self.rect = None
        self.update()

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


# defines a type
PlayersListType = list[Player]
