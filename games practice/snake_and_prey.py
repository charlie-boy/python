import pygame
from pygame.locals import *
import cevent
import random
import sys

class App(cevent.CEvent):
	def __init__(self):
		self._running = True
		self._display_surface = None
		self._image_surface = None

	def on_init(self):
		pygame.init()
		self._running = True
		self._display_surface = pygame.display.set_mode((400,300))
		self._caption = pygame.display.set_caption("Snake and preys")
#		self._image_surface = pygame.image.load("grass.jpg")
#		self._background_rect = self._image_surface.get_rect()
#		self
		self._fps_time = pygame.time.Clock()

		self.disp_width = 400
		self.disp_height = 300
		self.FPS = 10
		self.cellsize = 10
		self.black = (0,0,0)
		self.white = (255,255,255)
		self.red = (200,0,0)
		self.UP = 'up'
		self.DOWN = 'down'
		self.RIGHT = 'right'
		self.LEFT = 'left'
		self.x = 20
		self.y = 25
		self.snake_coords = [
						[self.x, self.y],
						[self.x, self.y+1],
						[self.x, self.y+2],
						[self.x, self.y+3],
						[self.x, self.y+4],
						[self.x, self.y+5],		
						] 
		self.snake_length = 6
		self.previous_direction = self.UP
		self.direction = self.UP
		self.prey_x = 30
		self.prey_y = 20
		self.count_prey = 0


	def draw_snake(self):
		for l in range(0,self.snake_length-1):
			x = self.snake_coords[l][0]*self.cellsize
			y = self.snake_coords[l][1]*self.cellsize
			makecell = pygame.Rect(x, y, self.cellsize, self.cellsize)
			pygame.draw.rect(self._display_surface, self.white, makecell)

	def draw_prey(self):
		makecell = pygame.Rect(self.prey_x*self.cellsize, self.prey_y*self.cellsize, self.cellsize, self.cellsize)
		pygame.draw.rect(self._display_surface, self.white, makecell)

	def prey_coordinates(self):
		self.prey_x = random.randrange(0, self.disp_width/self.cellsize)
		self.prey_y = random.randrange(0, self.disp_height/self.cellsize)
		self.count_prey = self.count_prey + 1
		self.draw_prey()

	def snake_movement(self):
		temp = [2*[0] for i in range(self.snake_length)]
		for i in range(self.snake_length):
			for j in range(2):
				temp[i][j] = self.snake_coords[i][j]

		if self.direction == self.UP:
			self.snake_coords[0][1] = self.snake_coords[0][1] - self.cell_number

		elif self.direction == self.LEFT:
			self.snake_coords[0][0] = self.snake_coords[0][0] - self.cell_number

		elif self.direction == self.RIGHT:
			self.snake_coords[0][0] = self.snake_coords[0][0] + self.cell_number

		elif self.direction == self.DOWN:
			self.snake_coords[0][1] = self.snake_coords[0][1] + self.cell_number

#		print self.snake_coords[0], self.prey_x, self.prey_y
		
		for i in range(1, self.snake_length):
			for j in range(2):
				self.snake_coords[i][j] = temp[i-1][j]

		if (self.snake_coords[0][0] == self.prey_x and self.snake_coords[0][1] == self.prey_y):
			self.snake_length = self.snake_length + 1
			self.snake_coords.append(temp[i])
			self.prey_coordinates()

	def make_text_object(self, text, font, text_color):
		text_surface = font.render(text, True, text_color)
		return text_surface, text_surface.get_rect()

	def what_next(self):
		for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				self.on_execute()

	def _message_surface(self, text):
		small_text = pygame.font.Font('freesansbold.ttf', 20)
		large_text = pygame.font.Font('freesansbold.ttf', 30)

		title_surface, title_rect = self.make_text_object(text, large_text, self.red)
		title_rect.center = (int(self.disp_width/2), int(self.disp_height)/2)
		self._display_surface.blit(title_surface, title_rect)

		score = str(self.count_prey*10)

		title_surface, title_rect = self.make_text_object("Your score is : " + score, large_text, self.white)
		title_rect.center = (int(self.disp_width/2), int(self.disp_height)/2+30)
		self._display_surface.blit(title_surface, title_rect)

		"Press enter to continue"
		info_surface, info_rect = self.make_text_object("Press enter to continue", small_text, self.white)
		info_rect.center = (int(self.disp_width/2), int(self.disp_height)/2 + 60)
		self._display_surface.blit(info_surface, info_rect)


		self.on_render()

		while self.what_next() == None:
			for event in pygame.event.get():
				self.on_event(event)

	def on_render(self):
		self._fps_time.tick(self.FPS)
#		self._display_surface.blit(self._image_surface, self._background_rect)
		pygame.display.flip()

	def on_loop(self):
		pass

	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		self.cell_number = 1

		if self.on_init() ==  False:
			self._running = False

		while(self._running):
			for event in pygame.event.get():
				self.on_event(event)

			if event.type == KEYDOWN:
				if self.previous_direction != self.UP and self.direction == self.DOWN:
					self.direction = self.DOWN

				elif self.previous_direction != self.DOWN and self.direction == self.UP:
					self.direction = self.UP

				elif self.previous_direction != self.LEFT and self.direction == self.RIGHT:
					self.direction = self.RIGHT

				elif self.previous_direction != self.RIGHT and self.direction == self.LEFT:
					self.direction = self.LEFT

				else:
					self.direction = self.previous_direction

			self._display_surface.fill(self.black)

			self.draw_prey()
			self.snake_movement()

			self.draw_snake()
			
			self.on_loop()
			self.on_render() 

			if (self.snake_coords[0][0]<0 or self.snake_coords[0][1]<0 or self.snake_coords[0][0]>self.disp_width/self.cellsize or self.snake_coords[0][1]>self.disp_height/self.cellsize):
				self._message_surface("you lost")

			for j in range(1, self.snake_length):
				if (self.snake_coords[0] == self.snake_coords[j]):
					self._message_surface("you lost")

			self.previous_direction = self.direction

		self.on_cleanup()


if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()
