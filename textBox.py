class TextBox(DrawableObj):
    def __init__(self, level, position, width, text, scroll = False, font_size = 5 , font_path = "/Library/Fonts/pixel-art_1.ttf"):  # other option: "/Library/Fonts/pixel-art_2.ttf"
        super(TextBox, self).__init__(level)
 
        self.scale_factor = copy.copy(self.level.scale_factor)
 
        self.tag = "TextBox"
        self.position = position
        self.font = pygame.font.Font(font_path, int(font_size * self.scale_factor))
        self.is_static = False
        self.dialog = []
        self.width = int(width * self.scale_factor)
 
        self.timer = 0
 
        self.text_color = (0,0,0)
        self.background_color = (255,255,255)
        self.border_color = (0,0,0)
 
        self.border_width = int(1.25 * self.scale_factor)
        self.margin = int(2 * self.scale_factor)
        self.space_between_lines = int(0.75 * self.scale_factor)
 
        self.character_number = 0
        self.scroll = scroll
        self.done_with_scroll = False
 
        self.set_text(text)
 
    def set_text(self, text):
        if self.scroll == True:
            self.final_text = text
            self.text = ""
        else:
            self.final_text = text
            self.text = self.final_text
 
        self.make_box(self.width)
        self.make_text(self.width)
 
    def make_box(self, width = None):
        if width == None:
            width = self.width
       
        # calculate the height of the message box width the given width
        xpos = copy.copy(self.margin)
        ypos = copy.copy(self.margin)
        for word in self.final_text.split(" "):
            ren = self.font.render(word + " ", True, self.text_color)
            w = ren.get_width()
            if xpos > width - w:
                ypos += ren.get_height() + self.space_between_lines
                xpos = copy.copy(self.margin)
            xpos += w
 
        if ypos == self.margin:
            width = xpos
 
        height = ypos + ren.get_height() + self.margin
        self.image = pygame.Surface((width, height))
        self.scale = Vector(width, height)
        self.image.fill(self.background_color)
        if self.border_width != 0:
            pygame.draw.rect(self.image, self.border_color, (0, 0, width, height), self.border_width)
           
    def make_text(self, width = None):
        if width == None:
            width = self.width
           
        # actually draw the text on the created surface (above)
        xpos = copy.copy(self.margin)
        ypos = copy.copy(self.margin)
        for word in self.text.split(" "):
            ren = self.font.render(word + " ", True, self.text_color)
            w = ren.get_width()
            if xpos > width - w:
                ypos += ren.get_height() + self.space_between_lines
                xpos = copy.copy(self.margin)
            self.image.blit(ren, (xpos, ypos))
            xpos += w