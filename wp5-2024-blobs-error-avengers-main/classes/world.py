import pygame as pg
import random
from classes.blobs_data import ENEMY_SPAWN_DATA  # Import enemy spawn data for levels

class World:
    def __init__(self, data, map_image):
        self.tile_map = []
        self.level = 1
        self.level_data = data
        self.image = map_image
        self.waypoints = []
        self.not_allowed = []
        self.enemy_list = []
        self.spawned_enemies = 0
        self.process_data()  # Process initial level data
        self.process_enemies()  # Process enemies for the initial level

    def process_data(self):
        for layer in self.level_data['layers']:
            if layer['name'] == 'map':
                self.tile_map = layer['data']

            elif layer['name'] == 'lemming_places':
                self.not_allowed = layer['data']

            elif layer['name'] == 'waypoints':
                for obj in layer['objects']:
                    waypoint_data = obj["polyline"]
                    self.process_waypoints(waypoint_data)

    def reset(self, data):
        self.level = 1  # Reset the level to 1
        self.spawned_enemies = 0
        self.enemy_list.clear()  
        self.tile_map = []  
        self.not_allowed = []  
        self.waypoints = []  
        self.level_data = data 
        self.process_data()  # Re-process level data
        self.process_enemies()  # Process enemies for the new level

    def process_waypoints(self, data):
        self.waypoints = [(point['x'], point['y']) for point in data]

    def process_enemies(self):
        enemies = ENEMY_SPAWN_DATA[self.level - 1]
        self.enemy_list = []
        self.spawned_enemies = 0
        for enemy_type, count in enemies.items():
            if count > 0:  
                self.enemy_list.extend([enemy_type] * count)
        random.shuffle(self.enemy_list)

    def next_level(self):
        self.level += 1
        if self.level > len(ENEMY_SPAWN_DATA):
            self.level = 1  # Loop back to level 1 if there are no more levels
        self.process_enemies()  # Populate self.enemy_list with the enemies for the current level
        self.spawned_enemies = 0  # Reset to zero to start spawning from the beginning

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
