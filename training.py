import sys 
import pygame
from class_training import Settings,Batman
def run():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_heigh))
	pygame.display.set_caption("abracadabra")
	bg_color=(0,0,230)
	x=Batman(screen)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		screen.fill(ai_settings.bg_color)
		x.blitme()
		pygame.display.flip()
run()
