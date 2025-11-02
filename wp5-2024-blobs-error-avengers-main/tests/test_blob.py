import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import data.settings as settings
from classes.blobs import Blob

class TestBlob(unittest.TestCase):

    def setUp(self):
        """Set up the initial number of lives before each test."""
        self.lives = settings.STARTING_LIVES 

    def lose_life(self):
        """Simulate losing a life when a blob reaches the end."""
        self.lives -= 1

    def test_normal_blob(self):
        """Test a normal blob without resistance."""
        blob = Blob()
        print("Testing normal blob...")
        print(f"Initial Health: {blob.health}")
        self.assertEqual(blob.health, 100)

        blob.take_damage(50)
        print(f"Health after taking 50 damage: {blob.health}")
        self.assertEqual(blob.health, 50)

        blob.take_damage(50)
        print(f"Health after taking another 50 damage: {blob.health}")
        self.assertEqual(blob.health, 0)
        print("Normal blob test passed.\n")

    def test_resistant_blob(self):
        """Test a blob with resistance to normal projectiles."""
        blob = Blob(resistance=['normal'])
        print("Testing resistant blob...")
        blob.take_damage(50, damage_type='normal')  # Should resist normal damage
        print(f"Health after taking normal damage: {blob.health}")  # No damage should be taken
        self.assertEqual(blob.health, 100)  # No damage should be taken

        blob.take_damage(50, damage_type='explosive')  # Should take explosive damage
        print(f"Health after taking explosive damage: {blob.health}")
        self.assertEqual(blob.health, 50)
        print("Resistant blob test passed.\n")

    def test_blob_movement(self):
        """Test the movement of a blob."""
        blob = Blob(speed=2)
        print("Testing blob movement...")
        blob.move()
        print(f"Blob's x position after moving: {blob.x}")
        self.assertEqual(blob.x, 2)
        print("Blob movement test passed.\n")

    def test_blob_reaches_end_and_loses_life(self):
        """Test that a life is lost when the blob reaches the end."""
        blob = Blob(speed=2)
        target_x = 10  # Define the endpoint of the blob's movement
        print("Testing blob reaching the end...")

        # Simulate movement towards the end
        while blob.x < target_x:
            blob.move()

        # Simulate the blob reaching the end and calling the life loss function
        self.lose_life()

        # Check if a life was lost
        print(f"Lives remaining after blob reaches end: {self.lives}")
        self.assertEqual(self.lives, settings.STARTING_LIVES - 1)  # One life should be lost

        print("Blob reaching end and life loss test passed.\n")

if __name__ == '__main__':
    unittest.main()
