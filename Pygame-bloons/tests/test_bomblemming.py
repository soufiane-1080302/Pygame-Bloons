import unittest
import sys
import os

# Add the root directory of the project to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.lemming_data import BOMBER_LEMMING_DATA
from data import settings

class TestBombLemmingDamage(unittest.TestCase):
    def test_damage_level_1(self):
        expected_damage_level_1 = 2
        actual_damage_level_1 = BOMBER_LEMMING_DATA[0]["damage"]
        self.assertEqual(actual_damage_level_1, expected_damage_level_1)
    

    def test_damage_level_1_unexpected_value(self):
        actual_damage_level_2 = BOMBER_LEMMING_DATA[0]["damage"]
        self.assertNotEqual(actual_damage_level_2, 1, f"Damage for level 1 should not be 1 but {actual_damage_level_2}")
        

    def test_damage_level_2(self):
        expected_damage_level_2 = 4
        actual_damage_level_2 = BOMBER_LEMMING_DATA[1]["damage"]
        self.assertEqual(actual_damage_level_2, expected_damage_level_2)
        
        
    def test_damage_level_2_unexpected_value(self):
        actual_damage_level_2 = BOMBER_LEMMING_DATA[1]["damage"]
        self.assertNotEqual(actual_damage_level_2, 3, f"Damage for level 2 should not be 3 but {actual_damage_level_2}")
        

    def test_damage_level_3(self):
        expected_damage_level_3 = 6
        actual_damage_level_3 = BOMBER_LEMMING_DATA[2]["damage"]
        self.assertEqual(actual_damage_level_3, expected_damage_level_3)

    def test_damage_level_3_unexpected_value(self):
        actual_damage_level_2 = BOMBER_LEMMING_DATA[2]["damage"]
        self.assertNotEqual(actual_damage_level_2, 5, f"Damage for level 3 should not be 5 but {actual_damage_level_2}")
        
class TestBombLemmingRange(unittest.TestCase):
    def test_range_level_1(self):
        expected_range_level_1 = 100
        actual_range_level_1 = BOMBER_LEMMING_DATA[0]["range"]
        self.assertEqual(actual_range_level_1, expected_range_level_1)
    

    def test_range_level_1_unexpected_value(self):
        actual_range_level_1 = BOMBER_LEMMING_DATA[0]["range"]
        self.assertNotEqual(actual_range_level_1, 120, f"Range for level 1 should not be 120 but {actual_range_level_1}")
        

    def test_range_level_2(self):
        expected_range_level_2 = 120
        actual_range_level_2 = BOMBER_LEMMING_DATA[1]["range"]
        self.assertEqual(actual_range_level_2, expected_range_level_2)
        
        
    def test_range_level_2_unexpected_value(self):
        actual_range_level_2 = BOMBER_LEMMING_DATA[1]["range"]
        self.assertNotEqual(actual_range_level_2, 150, f"Range for level 2 should not be 150 but {actual_range_level_2}")
        

    def test_range_level_3(self):
        expected_range_level_3 = 150
        actual_range_level_3 = BOMBER_LEMMING_DATA[2]["range"]
        self.assertEqual(actual_range_level_3, expected_range_level_3)

    def test_range_level_3_unexpected_value(self):
        actual_range_level_3 = BOMBER_LEMMING_DATA[2]["range"]
        self.assertNotEqual(actual_range_level_3, 180, f"Range for level 3 should not be 180 but {actual_range_level_3}")

class TestBombLemmingCooldown(unittest.TestCase):
    def test_cooldown_level_1(self):
        expected_cooldown_level_1 = 1000
        actual_cooldown_level_1 = BOMBER_LEMMING_DATA[0]["cooldown"]
        self.assertEqual(actual_cooldown_level_1, expected_cooldown_level_1)
    

    def test_cooldown_level_1_unexpected_value(self):
        actual_cooldown_level_1 = BOMBER_LEMMING_DATA[0]["cooldown"]
        self.assertNotEqual(actual_cooldown_level_1, 900, f"Cooldown for level 1 should not be 900 but {actual_cooldown_level_1}")
        

    def test_cooldown_level_2(self):
        expected_cooldown_level_2 = 750
        actual_cooldown_level_2 = BOMBER_LEMMING_DATA[1]["cooldown"]
        self.assertEqual(actual_cooldown_level_2, expected_cooldown_level_2)
        
        
    def test_cooldown_level_2_unexpected_value(self):
        actual_cooldown_level_2 = BOMBER_LEMMING_DATA[1]["cooldown"]
        self.assertNotEqual(actual_cooldown_level_2, 600, f"Cooldown for level 2 should not be 600 but {actual_cooldown_level_2}")
        

    def test_cooldown_level_3(self):
        expected_cooldown_level_3 = 500
        actual_cooldown_level_3 = BOMBER_LEMMING_DATA[2]["cooldown"]
        self.assertEqual(actual_cooldown_level_3, expected_cooldown_level_3)

    def test_cooldown_level_3_unexpected_value(self):
        actual_cooldown_level_3 = BOMBER_LEMMING_DATA[2]["cooldown"]
        self.assertNotEqual(actual_cooldown_level_3, 400, f"Cooldown for level 3 should not be 400 but {actual_cooldown_level_3}")
class TestBombLemmingUpgradeCost(unittest.TestCase):
    def test_upgrade_cost_level_1(self):
        expected_upgrade_cost_level_1 = 300
        actual_upgrade_cost_level_1 = BOMBER_LEMMING_DATA[0]["upgrade_cost"]
        self.assertEqual(actual_upgrade_cost_level_1, expected_upgrade_cost_level_1)
    

    def test_upgrade_cost_level_1_unexpected_value(self):
        actual_upgrade_cost_level_1 = BOMBER_LEMMING_DATA[0]["upgrade_cost"]
        self.assertNotEqual(actual_upgrade_cost_level_1, 200, f"Upgrade cost for level 1 should not be 200 but {actual_upgrade_cost_level_1}")
        

    def test_upgrade_cost_level_2(self):
        expected_upgrade_cost_level_2 = 450
        actual_upgrade_cost_level_2 = BOMBER_LEMMING_DATA[1]["upgrade_cost"]
        self.assertEqual(actual_upgrade_cost_level_2, expected_upgrade_cost_level_2)
        
        
    def test_upgrade_cost_level_2_unexpected_value(self):
        actual_upgrade_cost_level_2 = BOMBER_LEMMING_DATA[1]["upgrade_cost"]
        self.assertNotEqual(actual_upgrade_cost_level_2, 400, f"Upgrade cost for level 2 should not be 400 but {actual_upgrade_cost_level_2}")
        

    def test_upgrade_cost_level_3(self):
        expected_upgrade_cost_level_3 = 600
        actual_upgrade_cost_level_3 = BOMBER_LEMMING_DATA[2]["upgrade_cost"]
        self.assertEqual(actual_upgrade_cost_level_3, expected_upgrade_cost_level_3)

    def test_upgrade_cost_level_3_unexpected_value(self):
        actual_upgrade_cost_level_3 = BOMBER_LEMMING_DATA[2]["upgrade_cost"]
        self.assertNotEqual(actual_upgrade_cost_level_3, 500, f"Upgrade cost for level 3 should not be 500 but {actual_upgrade_cost_level_3}")

class TestBombLemming(unittest.TestCase):
    def test_levels(self):
        expected_levels = 3
        actual_levels = settings.LEMMING_LEVELS
        self.assertEqual(actual_levels, expected_levels)
    

    def test_levels_unexpected_value(self):
        actual_levels = settings.LEMMING_LEVELS
        self.assertNotEqual(actual_levels, 1, f"Tile size should not be 1 but {actual_levels}")
    
    def test_animation_steps(self):
        expected_animation_steps = 7
        actual_animation_steps = settings.ANIMATION_STEPS_BOMBER
        self.assertEqual(actual_animation_steps, expected_animation_steps)

    def test_animation_steps_unexpected_value(self):
        actual_animation_steps = settings.ANIMATION_STEPS_BOMBER
        self.assertNotEqual(actual_animation_steps, 1, f"Animation steps should not be 1 but {actual_animation_steps}")
    
    def test_animation_delay(self):
        expected_animation_delay = 30
        actual_animation_delay = settings.ANIMATION_DELAY
        self.assertEqual(actual_animation_delay, expected_animation_delay)
    
    def test_animation_delay_unexpected_value(self):
        actual_animation_delay = settings.ANIMATION_DELAY
        self.assertNotEqual(actual_animation_delay, 40, f"Animation delay should not be 40 but {actual_animation_delay}")
if __name__ == '__main__':
    unittest.main()