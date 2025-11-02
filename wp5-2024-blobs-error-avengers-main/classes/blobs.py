import pygame

class Blob:
    def __init__(self, health=100, speed=1, resistance=None):
        self.health = health
        self.speed = speed
        self.resistance = resistance or []
        self.x = 0
        self.y = 100

    def take_damage(self, damage, damage_type='normal'):
        if damage_type in self.resistance:
            return
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print("Blob destroyed")

    def move(self):
        self.x += self.speed

    def render(self, screen, image):
        screen.blit(image, (self.x, self.y))
