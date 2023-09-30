import pygame 
class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""
	def __init__(self):
		"""Инициализирует настройки игры."""
		self.screen_width=1000
		self.screen_heigh=600
		self.bg_color=(0,0,230)
		

class Batman():
	def __init__(self,screen):
		self.screen = screen
		self.image=pygame.image.load('images/batman.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=self.screen_rect.centery
	def blitme(self):
		self.screen.blit(self.image,self.rect)

