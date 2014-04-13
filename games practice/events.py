import pygame
from pygame.locals import *
import cevent
import sys
import random

class App(cevent.CEvent):
	def __init__(self):
		self._running = True
		self._display_surface = None
		self._image_surface = None

	def on_init(self):
		pygame.init()
		self._running = True
		self._display_surface = pygame.display.set_mode((800, 600))
		self._caption = pygame.display.set_caption("Event Handling")
		self._fps_time = pygame.time.Clock()

		self.disp_width = 800
		self.disp_height = 600
		self.FPS = 20
		self.cellsize = 10
		self.black = (0,0,0)
		self.white = (255,255,255)
		self.red = (200,0,0)
		self.UP = 'up'
		self.DOWN = 'down'
		self.RIGHT = 'right'
		self.LEFT = 'left'
		self.startx = 3
		self.starty = 3
		self.coords = [{'x':self.startx, 'y':self.starty}]
		self.direction = self.RIGHT

		self.evil_coords1 = [{'x':5, 'y':5}]
		self.evil_coords2 = [{'x':85, 'y':15}]
		self.evil_coords3 = [{'x':25, 'y':75}]
		self.evil_coords4 = [{'x':15, 'y':35}]
		self.evil_coords5 = [{'x':75, 'y':40}]
		self.evil_coords6 = [{'x':35, 'y':95}]
		self.evil_coords7 = [{'x':95, 'y':50}]
		self.evil_coords8 = [{'x':45, 'y':15}]
		self.evil_coords9 = [{'x':25, 'y':55}]
		self.evil_coords10 = [{'x':15, 'y':20}]
		self.evil_coords11 = [{'x':60, 'y':30}]
		self.evil_coords12 = [{'x':35, 'y':25}]

		self.dead_zones = []
		self.evil_coordinates = []
		self.current_position = []

	def on_loop(self):
		pass

	def draw_cell(self, coordinates, cell_color):
		for coord in coordinates:
			x = coord['x']*self.cellsize
			y = coord['y']*self.cellsize
		makecell = pygame.Rect(x, y, self.cellsize, self.cellsize)
		pygame.draw.rect(self._display_surface, cell_color, makecell)
		
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

#			return event.key
		return None

	def _message_surface(self, text):
		small_text = pygame.font.Font('freesansbold.ttf', 20)
		large_text = pygame.font.Font('freesansbold.ttf', 30)

		title_surface, title_rect = self.make_text_object(text, large_text, self.red)
		title_rect.center = (int(self.disp_width/2), int(self.disp_height)/2)
		self._display_surface.blit(title_surface, title_rect)

		"Press enter to continue"
		info_surface, info_rect = self.make_text_object("Press enter to continue", small_text, self.white)
		info_rect.center = (int(self.disp_width/2), int(self.disp_height)/2 + 100)
		self._display_surface.blit(info_surface, info_rect)


		self.on_render()

		while self.what_next() == None:
			for event in pygame.event.get():
				self.on_event(event)

	def evil_move(self, coord):
		self.evil_coordinates = []

		x_move = random.randrange(-1,2)
		y_move = random.randrange(-1,2)

		newcell = {'x':coord[0]['x']+x_move, 'y':coord[0]['y']+y_move}

		if (newcell['x'] < 0 or newcell['y'] < 0 or newcell['x'] > self.disp_width/self.cellsize or newcell['y'] > self.disp_height/self.cellsize):
			newcell = {'x':self.disp_width/(2*self.cellsize), 'y':self.disp_height/(2*self.cellsize)}
		
		del coord[-1]
		
		self.evil_coordinates.append(newcell['x'])
		self.evil_coordinates.append(newcell['y'])
		self.dead_zones.append(self.evil_coordinates)

		coord.insert(0, newcell)

		

	def on_render(self):
		self._fps_time.tick(self.FPS)
		pygame.display.flip()

	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		if self.on_init() ==  False:
			self._running = False

		while(self._running):
			for event in pygame.event.get():
				self.on_event(event)

			if self.direction == self.UP:
				self.newcell = {'x':self.coords[0]['x'], 'y':self.coords[0]['y']-1}
			elif self.direction == self.DOWN:
				self.newcell = {'x':self.coords[0]['x'], 'y':self.coords[0]['y']+1}
			elif self.direction == self.LEFT:
				self.newcell = {'x':self.coords[0]['x']-1, 'y':self.coords[0]['y']}
			elif self.direction == self.RIGHT:
				self.newcell = {'x':self.coords[0]['x']+1, 'y':self.coords[0]['y']}

			del self.coords[-1]

			self.coords.insert(0, self.newcell)
			self._display_surface.fill(self.black)

			self.draw_cell(self.coords, self.white)
		
			self.draw_cell(self.evil_coords1, self.red)
			self.draw_cell(self.evil_coords2, self.red)
			self.draw_cell(self.evil_coords3, self.red)
			self.draw_cell(self.evil_coords4, self.red)
			self.draw_cell(self.evil_coords5, self.red)
			self.draw_cell(self.evil_coords6, self.red)
			self.draw_cell(self.evil_coords7, self.red)
			self.draw_cell(self.evil_coords8, self.red)
			self.draw_cell(self.evil_coords9, self.red)
			self.draw_cell(self.evil_coords10, self.red)
			self.draw_cell(self.evil_coords11, self.red)
			self.draw_cell(self.evil_coords12, self.red)

			self.dead_zones = []

			self.evil_move(self.evil_coords1)
			self.evil_move(self.evil_coords2)
			self.evil_move(self.evil_coords3)
			self.evil_move(self.evil_coords4)
			self.evil_move(self.evil_coords5)
			self.evil_move(self.evil_coords6)
			self.evil_move(self.evil_coords7)
			self.evil_move(self.evil_coords8)
			self.evil_move(self.evil_coords9)
			self.evil_move(self.evil_coords10)
			self.evil_move(self.evil_coords11)
			self.evil_move(self.evil_coords12)

			self.current_position = [self.newcell['x'], self.newcell['y']]
#			print self.current_position
#			print self.dead_zones
			for death_coord in self.dead_zones:
				if death_coord == self.current_position:
					self._message_surface("You Died Asshole...You Cock-sucking Bastard")
	
			self.on_loop()
			self.on_render()

			if (self.newcell['x'] < 0 or self.newcell['y'] < 0 or self.newcell['x'] > self.disp_width/self.cellsize or self.newcell['y'] > self.disp_height/self.cellsize):
				self._message_surface("You Died Asshole...You Cock-sucking Bastard")
#				self._running = False

		self.on_cleanup()

if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()


