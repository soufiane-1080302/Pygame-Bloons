import pygame
import os

# Set the root directory
root_dir = r"c:\school\wp5-2024-blobs-error-avengers"

# Construct the full paths to the images
level_1_path = os.path.join(root_dir, "images", "levels", "level_1.png")
blob_image_path = os.path.join(root_dir, "images", "bloons", "balloon_red.png")
cursor_lemming_path = os.path.join(root_dir, "images", "monkeys", "monkey_sling_lvl_1", "monkey_1.png")

# Load assets (background image and blob image)
level_1 = pygame.image.load(level_1_path).convert_alpha()
blob_image = pygame.image.load(blob_image_path).convert_alpha()
# Individuele lemming plaatje van muis
cursor_lemming = pygame.image.load(cursor_lemming_path).convert_alpha()