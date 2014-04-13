import pygame
from pygame.locals import *
import cevent

class App(cevent.CEvent):
	def __init__(self):
		self._running = True
		self._display_surf = None
		self._image_surf = None

	def on_init(self): 
		pygame.init()
		self._display_surf = pygame.display.set_mode((700,500))
		self._running = True
		self._caption = pygame.display.set_caption('Fifa 2015......fucked for life version')
		self._image_surf = pygame.image.load('ball.jpg').convert()
		self._fps_time = pygame.time.Clock()
#		self._single_pixel = pygame.PixelArray(self._display_surf)

		self.yellow = (255,255,0)
		self.x = 10
		self.y = 10
		self.pixmove = 5
		self.movement = "down"
		self.FPS = 60

#	def on_event(self, event):
#		if event.type == QUIT:
#			self._running = False

	def on_loop(self):
		pass

	def on_render(self):
		self._display_surf.blit(self._image_surf, (self.x,self.y))
		self._fps_time.tick(self.FPS)
#		self._single_pixel[100][100] = self.yellow
		pygame.display.flip()

	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		if self.on_init() == False:
			self._running = False

		while(self._running):
			if self.movement == "down":
				self.y += self.pixmove
				if self.y > 300:
					self._image_surf = pygame.transform.rotate(self._image_surf,90)
					self.movement = "right"

			elif self.movement == "right":
				self.x += self.pixmove
				if self.x > 400:
					self.movement = "up"

			elif self.movement == "up":
				self.y -= self.pixmove
				if self.y < 10:
					self.movement = "left"

			elif self.movement == "left":
				self.x -= self.pixmove
				if self.x < 10:
					self.movement = "down"


			for event in pygame.event.get():
				self.on_event(event)
			
			self.on_loop()
			self.on_render()
			

		self.on_cleanup()


if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()
