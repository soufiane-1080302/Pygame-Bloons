import pygame
import json
import data.settings as settings
from classes.button import Button
from classes.lemmings import Lemming
from classes.bomber_lemming import BomberLemming
from classes.world import World
from classes.enemy import Enemy
from screens.start_screen import start_screen
from screens.game_over_screen import game_over_screen

pygame.init()
pygame.display.set_caption('BTD6')
screen = pygame.display.set_mode((settings.SCREEN_WIDTH + settings.SIDE_PANEL, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

game_state = "start"
coins = settings.STARTING_COINS
lives = settings.STARTING_LIVES
cooldown = 400

level_1 = pygame.image.load('images/levels/level_1/level_1.png').convert_alpha()
enemy_images = {
    "red": pygame.image.load('images/bloons/balloon_red.png').convert_alpha(),
    "green": pygame.image.load('images/bloons/balloon_green.png').convert_alpha(),
    "blue": pygame.image.load('images/bloons/balloon_blue.png').convert_alpha(),
    "black": pygame.image.load('images/bloons/balloon_black.png').convert_alpha()
}
sling_spritesheet = [pygame.image.load(f'images/monkeys/monkey_sling/level_{x}_sling.png').convert_alpha() for x in range(1, settings.LEMMING_LEVELS + 1)]
bomber_spritesheet = [pygame.image.load(f'images/monkeys/monkey_bomber/bomber_level_{x}.png').convert_alpha() for x in range(1, settings.LEMMING_LEVELS + 1)]
cursor_sling = pygame.image.load('images/monkeys/monkey_sling/placeholder.png').convert_alpha()
cursor_bomber = pygame.image.load('images/monkeys/monkey_bomber/placeholder.png').convert_alpha()

buttons = {
    "buy_sling": Button(settings.SCREEN_WIDTH + 30, 230, pygame.image.load('images/buttons/buy_sling.png').convert_alpha(), True),
    "buy_bomber": Button(settings.SCREEN_WIDTH + 30, 280, pygame.image.load('images/buttons/buy_bomber.png').convert_alpha(), True),
    "cancel": Button(settings.SCREEN_WIDTH + 30, 620, pygame.image.load('images/buttons/cancel.png').convert_alpha(), True),
    "upgrade": Button(settings.SCREEN_WIDTH + 220, 620, pygame.image.load('images/buttons/up-arrow.png').convert_alpha(), True),
    "pause": Button(settings.SCREEN_WIDTH + 210, 35, pygame.image.load('images/buttons/pause.png').convert_alpha(), True),
    "fast_forward": Button(settings.SCREEN_WIDTH + 180, 35, pygame.image.load('images/buttons/fast-forward.png').convert_alpha(), True)
}

with open('images/levels/level_1/level_1.tmj') as json_file:
    level_1_data = json.load(json_file)
world = World(level_1_data, level_1)
world.process_data()
world.process_enemies()

enemy_group = pygame.sprite.Group()
lemming_group = pygame.sprite.Group()

def render_text(text, position, color=(0, 0, 0)):
    font = pygame.font.SysFont('Arial', 24)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def update_coins(amount):
    global coins
    coins += amount

def create_lemming(mouse_pos, lemming_type="sling"):
    global coins
    mouse_tile_x, mouse_tile_y = mouse_pos[0] // settings.TILE_SIZE, mouse_pos[1] // settings.TILE_SIZE
    mouse_tile_num = (mouse_tile_y * settings.COLS) + mouse_tile_x

    if (
        0 <= mouse_tile_num < len(world.tile_map) and
        world.tile_map[mouse_tile_num] == 38 and
        world.not_allowed[mouse_tile_num] == 0
    ):
        space_is_free = all((mouse_tile_x, mouse_tile_y) != (lemming.tile_x, lemming.tile_y) for lemming in lemming_group)

        if space_is_free:
            price = settings.PRICE_BOMBER if lemming_type == "bomber" else settings.PRICE_SLING
            if coins >= price:
                coins -= price
                new_lemming = (
                    BomberLemming(bomber_spritesheet, mouse_tile_x, mouse_tile_y) 
                    if lemming_type == "bomber" 
                    else Lemming(sling_spritesheet, mouse_tile_x, mouse_tile_y)
                )
                lemming_group.add(new_lemming)

def render_game_info():
    render_text(f"Coins: {coins}", (settings.SCREEN_WIDTH + 30, 520))
    render_text(f"Lives: {lives}", (settings.SCREEN_WIDTH + 30, 200))

def lose_life():
    global lives
    lives -= 1
    if lives <= 0:
        return "game_over"

def select_sling(mouse_pos):
    for lemming in lemming_group:
        if lemming.rect.collidepoint(mouse_pos):
            return lemming
    return None

placing_sling = placing_bomber = False
selected_sling = None
is_paused = False
running = True
last_enemy_spawn = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] < settings.SCREEN_WIDTH and mouse_pos[1] < settings.SCREEN_HEIGHT:
                if placing_sling:
                    create_lemming(mouse_pos, "sling")
                elif placing_bomber:
                    create_lemming(mouse_pos, "bomber")
                else:
                    selected_sling = select_sling(mouse_pos)

    if game_state == "start":
        start_screen(screen)
        game_state = "playing"

    elif game_state == "playing":
        clock.tick(settings.FPS)

        if selected_sling:
            selected_sling.selected = True

        if not is_paused:
            enemy_group.update()
            lemming_group.update(enemy_group)

            current_time = pygame.time.get_ticks()

            # Check if it's time to spawn a new enemy
            if current_time - last_enemy_spawn > cooldown:
                if world.spawned_enemies < len(world.enemy_list):
                    enemy_type = world.enemy_list[world.spawned_enemies]
                    enemy_image = enemy_images[enemy_type]
                    enemy = Enemy(
                        waypoints=world.waypoints,
                        image=enemy_image,
                        enemy_type=enemy_type,
                        coin_callback=update_coins,
                        lose_life_callback=lose_life
                    )
                    enemy_group.add(enemy)
                    world.spawned_enemies += 1
                    last_enemy_spawn = current_time

                # Check if all enemies are defeated
                if not enemy_group:
                    world.next_level()  # Move to the next level
                    enemy_group.empty()  # Clear the current enemy group
                    last_enemy_spawn = pygame.time.get_ticks()  # Reset spawn timer

        screen.fill(settings.WHITE)
        world.draw(screen)

        if buttons["pause"].draw(screen):
            is_paused = not is_paused

        enemy_group.draw(screen)
        for lemming in lemming_group:
            lemming.draw(screen)
        for enemy in enemy_group:
            enemy.draw_health_bar(screen)

        if selected_sling:
            if selected_sling.upgrade_level < settings.LEMMING_LEVELS:
                if buttons["upgrade"].draw(screen):
                    coins = selected_sling.upgrade(coins, screen, pygame.font.SysFont('Arial', 24))  # Pass font

            if buttons["cancel"].draw(screen):
                selected_sling = None

        if buttons["buy_sling"].draw(screen):
            placing_sling = True
        if buttons["buy_bomber"].draw(screen):
            placing_bomber = True

        if placing_sling or placing_bomber:
            if placing_sling:
                cursor_lemming = cursor_sling
            elif placing_bomber:
                cursor_lemming = cursor_bomber
            cursor_rect = cursor_lemming.get_rect()
            cursor_pos = pygame.mouse.get_pos()
            cursor_rect.center = cursor_pos
            if cursor_pos[0] < settings.SCREEN_WIDTH:
                screen.blit(cursor_lemming, cursor_rect)
            if buttons["cancel"].draw(screen):
                placing_sling = placing_bomber = False

        render_game_info()
        pygame.display.update()

        if lives <= 0:
            game_state = "game_over"

    elif game_state == "game_over":
        action = game_over_screen(screen)
        if action == "restart":
            coins = settings.STARTING_COINS
            lives = settings.STARTING_LIVES
            world.reset(level_1_data)
            enemy_group.empty()
            lemming_group.empty()
            world.spawned_enemies = 0
            last_enemy_spawn = pygame.time.get_ticks()
            placing_sling = False
            placing_bomber = False
            game_state = "playing"
        elif action == "quit":
            running = False

pygame.quit()
