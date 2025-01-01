import pygame
from constants import *
from player import Player

def main():
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        dt = 0

        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return

                player.update(dt)
                screen.fill("black")
                player.draw(screen)
                pygame.display.flip()
                clock.tick(60) / 1000

if __name__ == "__main__":
    main()import pygame
from constants import *
from player import Player

def main():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		player.update(dt)	
		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		clock.tick(60) / 1000

if __name__ == "__main__":
    main()
