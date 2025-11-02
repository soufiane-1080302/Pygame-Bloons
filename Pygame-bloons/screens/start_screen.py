# start_screen.py
import pygame
import data.settings as settings

def start_screen(screen):
    screen.fill(settings.WHITE)
    font = pygame.font.SysFont('Arial', 24)

    def render_text(text, position, color=(0, 0, 0)):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, position)

    render_text("Welcome to BTD6!", (settings.SCREEN_WIDTH // 2 - 100, settings.SCREEN_HEIGHT // 2 - 50))
    render_text("Press SPACE to Start", (settings.SCREEN_WIDTH // 2 - 100, settings.SCREEN_HEIGHT // 2 + 10))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
