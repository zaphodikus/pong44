import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from colours import *
from ponglogger import MyLoggerBase
from network import Network
from client_base import ClientBase
from player import Player,PlayersListType
from sprite_sheet import FontSheet

# client globals
clientnumber = 0

# constants
BORDER_THICK = 5


class Client(MyLoggerBase, ClientBase):

    def run_game(self, width=500, height=500):

        icon = pygame.image.load('images/Pong.png')
        self.win = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Pong game", "Pong")
        pygame.display.set_icon(icon)
        self.width = width
        self.height = height

        clock = pygame.time.Clock()
        n = Network(role='client')
        startpos = self.read_pos(n.get_pos())
        p = Player(startpos[0], startpos[1], 20, 100, RED)
        p2 = Player(0, 0, 20, 100, BLUE)
        self.sp = FontSheet('images/digital_font_sheet.png')
        run = True
        while run:
            clock.tick(60)
            p2pos = self.read_pos(n.send(self.make_pos((p.x, p.y))))
            p2.x = p2pos[0]
            p2.y = p2pos[1]
            p2.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            if run:
                p.move()
                self.redraw_window([p, p2])

    def redraw_window(self, players: PlayersListType):
        # redraw the game screen
        self.win.fill(BLACK)
        x = self.width/2
        length = int(self.height/20/2)
        stroke = int(length/2)
        for segment in range(0, int(self.height/length)):
            pygame.draw.line(self.win, WHITE, (x, segment*length), (x, segment*length+stroke))
        # draw top and bottom borders (temporary)
        pygame.draw.rect(self.win, WHITE, (0, 0,              self.width, BORDER_THICK))
        pygame.draw.rect(self.win, WHITE, (0, self.height-(BORDER_THICK-1), self.width, self.height-1))
        self.win.blit(self.sp.glyph(' '), (10,10, 10 + self.sp.glyph_width, 10 + self.sp.glyph_height))

        # redraw player sprites
        for p in players:
            p.draw(self.win)
        pygame.display.update()
