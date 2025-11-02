# game_over_screen.py
import pygame
import data.settings as settings

def game_over_screen(screen):
    screen.fill(settings.WHITE)
    font = pygame.font.SysFont('Arial', 24)

    def render_text(text, position, color=(0, 0, 0)):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, position)

    render_text("Game Over", (settings.SCREEN_WIDTH // 2 - 50, settings.SCREEN_HEIGHT // 2 - 50), color=(255, 0, 0))
    render_text("Press R to Restart or Q to Quit", (settings.SCREEN_WIDTH // 2 - 140, settings.SCREEN_HEIGHT // 2 + 10))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_q:
                    return "quit"
    return "quit"
