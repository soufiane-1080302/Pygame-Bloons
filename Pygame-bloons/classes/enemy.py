import pygame as pg
from pygame.math import Vector2
from classes.blobs_data import ENEMY_DATA

class Enemy(pg.sprite.Sprite):
    def __init__(self, waypoints, image, enemy_type, coin_callback, lose_life_callback):
        super().__init__()
        self.image = pg.transform.scale(image, (48, 48))
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.rect = self.image.get_rect(center=self.pos)
        
        self.enemy_data = ENEMY_DATA[enemy_type]
        self.health = self.enemy_data["health"]
        self.max_health = self.health
        self.speed = self.enemy_data["speed"]
        self.coins_on_death = self.enemy_data["coins_on_death"]
        self.resistance = self.enemy_data.get("resistance", 0)
        self.target_waypoint = 1
        
        self.coin_callback = coin_callback
        self.lose_life_callback = lose_life_callback

    def move(self):
        if self.target_waypoint < len(self.waypoints):
            target = Vector2(self.waypoints[self.target_waypoint])
            movement = target - self.pos
            distance = movement.length()

            if distance > self.speed:
                self.pos += movement.normalize() * self.speed
            else:
                self.pos = target
                self.target_waypoint += 1

            self.rect.center = self.pos
        else:
            self.lose_life_callback()
            self.kill()

    def calculate_damage(self, incoming_damage):
        effective_damage = max(0, incoming_damage - self.resistance)
        return effective_damage

    def take_damage(self, damage):
        effective_damage = self.calculate_damage(damage)
        self.health -= effective_damage
        if self.health <= 0:
            self.die()

    def die(self):
        self.coin_callback(self.coins_on_death)
        self.kill()

    def draw_health_bar(self, surface):
        bar_width = 50
        bar_height = 5
        fill_width = max(0, (self.health / self.max_health) * bar_width)

        if self.health / self.max_health > 0.5:
            color = (0, 255, 0)
        elif self.health / self.max_health > 0.2:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)

        pg.draw.rect(surface, (255, 0, 0), (self.rect.x, self.rect.y - 10, bar_width, bar_height))
        pg.draw.rect(surface, color, (self.rect.x, self.rect.y - 10, fill_width, bar_height))

    def update(self):
        self.move()
