import pygame as pg
import math
import data.settings as settings
from classes.lemming_data import LEMMING_DATA


class Lemming(pg.sprite.Sprite):
    def __init__(self, sprite_sheets, tile_x, tile_y):
        super().__init__()
        self.upgrade_level = 1
        self.range = LEMMING_DATA[self.upgrade_level - 1]["range"]
        self.cooldown = LEMMING_DATA[self.upgrade_level - 1]["cooldown"]
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.target = None

        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = self.tile_x * settings.TILE_SIZE + settings.TILE_SIZE // 2
        self.y = (self.tile_y - 0.5) * settings.TILE_SIZE + settings.TILE_SIZE // 2

        self.sprite_sheets = sprite_sheets
        self.animation_list = self.load_images(self.sprite_sheets[self.upgrade_level - 1])
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()

        self.angle = 90
        self.original_image = self.animation_list[self.frame_index]
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.range_image = pg.Surface((self.range * 2, self.range * 2), pg.SRCALPHA)
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect(center=self.rect.center)

    def load_images(self, sprite_sheet):
        size = sprite_sheet.get_height()
        steps = settings.ANIMATION_STEPS
        if self.upgrade_level == 3:
            steps = 8
        return [sprite_sheet.subsurface(x * size, 0, size, size) for x in range(steps)]

    def update(self, enemy_group):
        if self.target:
            self.play_animation()
        else:
            if pg.time.get_ticks() - self.last_shot > self.cooldown:
                self.pick_target(enemy_group)

    def pick_target(self, enemy_group):
        for enemy in enemy_group:
            x_dist = enemy.pos[0] - self.x
            y_dist = enemy.pos[1] - self.y
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist < self.range:
                self.target = enemy
                self.angle = math.degrees(math.atan2(-y_dist, x_dist))
                enemy.take_damage(self.get_damage())

    def play_animation(self):
        self.original_image = self.animation_list[self.frame_index]
        if pg.time.get_ticks() - self.update_time > settings.ANIMATION_DELAY:
            self.update_time = pg.time.get_ticks()
            self.frame_index = (self.frame_index + 1) % len(self.animation_list)
            if self.frame_index == 0:
                self.last_shot = pg.time.get_ticks()
                self.target = None

    def upgrade(self, coins, screen, font):
        if self.upgrade_level < len(LEMMING_DATA) and coins >= LEMMING_DATA[self.upgrade_level - 1]["upgrade_cost"]:
            coins -= LEMMING_DATA[self.upgrade_level - 1]["upgrade_cost"]
            self.upgrade_level += 1
            self.range = LEMMING_DATA[self.upgrade_level - 1]["range"]
            self.cooldown = LEMMING_DATA[self.upgrade_level - 1]["cooldown"]

            self.animation_list = self.load_images(self.sprite_sheets[self.upgrade_level - 1])
            self.original_image = self.animation_list[self.frame_index]

            self.update_range_image()
            return coins
        else:
            text = font.render("Not enough coins for upgrade.", True, (255, 0, 0))
            screen.blit(text, (10, 10))
            pg.display.update()
            pg.time.wait(2000)
            return coins

    def update_range_image(self):
        self.range_image = pg.Surface((self.range * 2, self.range * 2), pg.SRCALPHA)
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect(center=self.rect.center)

    def get_damage(self):
        return LEMMING_DATA[self.upgrade_level - 1]["damage"]

    def set_attack_speed(self, new_cooldown):
        self.cooldown = new_cooldown

    def set_range(self, new_range):
        self.range = new_range
        self.update_range_image()

    def draw(self, surface):
        self.image = pg.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)
