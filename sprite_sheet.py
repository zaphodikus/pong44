import pygame
import math
import configparser
import os


class FontMetaData(object):
    def __init__(self, chars, lowercase, errorchar, image_width, image_height, rows, cols):
        """
        Base class for sprite-sheets
        :param chars:
        :param errorchar: 0 based index of the error sprite in a font sheet
        :param image_width:
        :param image_height:
        :param rows:
        :param cols:
        Example configuration DAT file:
        config = configparser.ConfigParser()
        config['FONT'] = {
            'chars' : ": ><)(||1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        'errorchar' : 0,  # index for any invalid or unmapped characters
        'image_width' : 128,
        'image_height' : 190,
        'rows' : 6,
        'cols' : 8,
        }
        with open(filename, 'w') as configfile:
            config.write(configfile)

        """
        BOOLEAN_STATES = {'1': True, 'yes': True, 'true': True, 'on': True,
                          '0': False, 'no': False, 'false': False, 'off': False}
        self.chars = str(chars)
        self.lowercase = False
        if lowercase in BOOLEAN_STATES:
            self.lowercase = BOOLEAN_STATES[lowercase]
        self.errorchar = int(errorchar)
        self.image_width = int(image_width)
        self.image_height = int(image_height)
        self.rows = int(rows)
        self.cols = int(cols)
        self.glyph_height = int(math.ceil(self.image_height / self.rows))
        self.glyph_width = int(math.ceil(self.image_width / self.cols))

    @staticmethod
    def load_meta(filename):
        config = configparser.ConfigParser()
        config.read(filename)
        meta = {}
        for key in config['FONT']:
            meta[key] = config['FONT'][key]
        return meta


class FontSheet(FontMetaData):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)
        dat_filename, _ = os.path.splitext(filename)
        dat_filename += '.dat'
        conf = FontMetaData.load_meta(dat_filename)
        super().__init__(**conf)

    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def glyph_by_char(self, character):
        # return glyph using a character
        if not self.lowercase:
            character = character.upper()
        try:
            idx = self.chars.index(character)
        except ValueError:
            idx = self.errorchar
        return self.glyph(idx)

    def glyph(self, index: int):
        # return just the specific glyph
        top = math.floor(index / self.cols) * self.glyph_height
        left = index % self.cols * self.glyph_width
        return self.image_at( (left, top, self.glyph_width, self.glyph_height))
