import pygame
import button
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Main Menu')

game_pause = False
menu_state = 'Main'

random_x1 = random.randint(0, 800)
random_y1 = random.randint(0, 400)
random_x2 = random.randint(0, 800)
random_y2 = random.randint(0, 400)
random_x3 = random.randint(0, 800)
random_y3 = random.randint(0, 400)
x = 200
y = 200
width = 20
height = 20
vel = 0.125

font = pygame.font.SysFont('arialblack', 40)

TEXT_COL = (255, 255, 255)

end_img = pygame.image.load('end.jpg').convert_alpha()
resume_img = pygame.image.load('resume.jpg').convert_alpha()
option_img = pygame.image.load('OPTIONS.jpg').convert_alpha()
nooption_img = pygame.image.load('nooptions.jpg').convert_alpha()
back_img = pygame.image.load('back.jpg').convert_alpha()
pussy_img = pygame.image.load('pussy.jpg').convert_alpha()
lessgoo_img = pygame.image.load('lessgoo.jpg').convert_alpha()
customize_img = pygame.image.load('customize.jpg').convert_alpha()

end_button = button.Button(276, 265, end_img, 0.115)
resume_button = button.Button(276, 15, resume_img, 0.115)
option_button = button.Button(276, 140, option_img, 0.115)
nooption_button = button.Button(100, 200, nooption_img, 0.130)
back_button = button.Button(450, 200, back_img, 0.130)
pussy_button = button.Button(276, 265, pussy_img, 0.115)
lessgoo_button = button.Button(276, 15, lessgoo_img, 0.115)
customize_button = button.Button(276, 140, customize_img, 0.115)

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(x, y, width, height)
    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for enemy in enemy:
            if self.rect.colliderect(enemy.rect):
                if dx > 0:
                    self.rect.right = enemy.rect.left
                if dx < 0:
                    self.rect.left = enemy.rect.right
                if dy > 0:
                    self.rect.bottom = enemy.rect.top
                if dy < 0:
                    self.rect.top = enemy.rect.bottom


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

text ="Enemies are purple.\n Soup is orange.\n Sword is gold.\n"
run = True
while run:
    
    screen.fill((0,0,0))

    if game_pause == True:
        if menu_state == 'Main':
            if resume_button.draw(screen):
                game_pause = False
            if option_button.draw(screen):
                menu_state = 'Options'
            if end_button.draw(screen):
                run = False
        if menu_state == 'Options':
            if nooption_button.draw(screen):
                pass
            if back_button.draw(screen):
                menu_state = 'Main'
    else:
        draw_text('Press ESC to pause', font, TEXT_COL, 185, 340)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x>0:
            x -= vel

        if keys[pygame.K_RIGHT] and x<800-width:
            x += vel
        
        if keys[pygame.K_UP] and y>0:
            y -= vel
        
        if keys[pygame.K_DOWN] and y<400 - height:
            y += vel

        player = pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))
        enemy = pygame.draw.rect(screen, (255, 0, 255), (random_x1, random_y1, width, height))
        soup = pygame.draw.rect(screen, (255, 67, 0), (random_x2, random_y2, width, height))
        sword = pygame.draw.rect(screen, (255, 255, 0), (random_x3, random_y3, width, height))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()