import pygame, sys, random
from pygame.locals import *
pygame.init()
screen_info = pygame.display.Info()
size = (width,height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color=(225,225,225)
fish_image=pygame.image.load("chickenn.png")
fish_image = pygame.transform.smoothscale(fish_image,(80,80))
fish_rect = fish_image.get_rect()
fish_rect.center=(width//2,height//2)
speed = pygame.math.Vector2(0,10)
rotation=random.randint(0,360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image,180-rotation)
def main():
    while True:
        clock.tick(60)
        screen.All(color)
        pygame.display.flip()
if __name__=='__main__':
    main()
