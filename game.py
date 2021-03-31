import pygame
import random
import sys
screen_size = [360 , 640]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()
background = pygame.image.load('scene.jpg')
character = pygame.image.load('character.png')
bhoot1 = pygame.image.load('bhoot.png')
def random_fall():
    return -1*random.randint(50,1000)
bhoot1_y = [random_fall(),random_fall(),random_fall()]
character_x = 150
score = 0
def count_score(i):
    global score
    global keep_alive
    score = score - 50
    bhoot1_y[i] = random_fall()
    if score <= -300:
        keep_alive = False

def bhoot1_random_fall(i):
    global score
    if bhoot1_y[i] > 640:
        bhoot1_y[i] = random_fall()
        score = score + 5
        print('score', score)
    else:
        bhoot1_y[i] = bhoot1_y[i] + 5
def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'Score: ' + str(score)
    text_image = font.render(score_text,True, (0,255,0))
    screen.blit(text_image,[20,10])
keep_alive=True
speed_control_of_bhoot1 = pygame.time.Clock()
while keep_alive:
    # if bhoot1_y > 640:
    #     bhoot1_y = 0
    # else:
    #     bhoot1_y = bhoot1_y + 1
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and character_x < 280:
        character_x = character_x + 6
    elif keys[pygame.K_LEFT] and character_x > 0:
        character_x = character_x - 6
    bhoot1_random_fall(0)
    bhoot1_random_fall(1)
    bhoot1_random_fall(2)
    screen.blit(background,[0,0])
    screen.blit(character,[character_x,560])
    screen.blit(bhoot1,[0,bhoot1_y[0]])
    screen.blit(bhoot1,[140,bhoot1_y[1]])
    screen.blit(bhoot1,[280,bhoot1_y[2]])
    if bhoot1_y[0] > 500 and character_x < 70:
        count_score(0)
    if bhoot1_y[1] > 500 and character_x > 70 and character_x < 200:
        count_score(1)
    if bhoot1_y[2] > 500 and character_x > 220:
        count_score(2)
    display_score(score)
    pygame.display.update()
    speed_control_of_bhoot1.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
    