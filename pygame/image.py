import pygame
import os

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
#surface = pygame.Surface((100,100))
#image = pygame.image.load('irongirl.png')

pygame.init()

screen = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()
done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done =True

	screen .fill((0,0,0))
	screen.blit(get_image('irongirl.png'), (10, 10))

	pygame.display.flip()
	clock.tick(60)
