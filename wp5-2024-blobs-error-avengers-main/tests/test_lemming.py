import unittest
import sys
import pygame as pg
import os

# Add the root directory of the project to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.lemmings import Lemming
from data.settings import TILE_SIZE, ANIMATION_STEPS  
from classes.lemming_data import LEMMING_DATA

class TestLemmingDamage(unittest.TestCase):
    def test_damage_level_1(self):
        expected_damage_level_1 = 10
        actual_damage_level_1 = LEMMING_DATA[0]["damage"]
        self.assertEqual(actual_damage_level_1, expected_damage_level_1)

    def test_damage_level_1_unexpected_value(self):
        actual_damage_level_1 = LEMMING_DATA[0]["damage"]
        self.assertNotEqual(actual_damage_level_1, 15, "Damage for level 1 should not be 15")

    def test_damage_level_2(self):
        expected_damage_level_2 = 20 
        actual_damage_level_2 = LEMMING_DATA[1]["damage"]
        self.assertEqual(actual_damage_level_2, expected_damage_level_2)
        
    def test_damage_level_2_unexpected_value(self):
        actual_damage_level_2 = LEMMING_DATA[1]["damage"]
        self.assertNotEqual(actual_damage_level_2, 25, "Damage for level 2 should not be 25")

    def test_damage_level_3(self):
        expected_damage_level_3 = 30
        actual_damage_level_3 = LEMMING_DATA[2]["damage"]
        self.assertEqual(actual_damage_level_3, expected_damage_level_3)

    def test_damage_level_3_unexpected_value(self):
        actual_damage_level_3 = LEMMING_DATA[2]["damage"]
        self.assertNotEqual(actual_damage_level_3, 35, "Damage for level 3 should not be 35")


if __name__ == '__main__':
    unittest.main()