import unittest
import sys
import os

# Add the root directory of the project to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import settings
class TestWorld(unittest.TestCase):
    def test_tilesize(self):
        expected_tile_size = 32
        actual_tile_size = settings.TILE_SIZE
        self.assertEqual(actual_tile_size, expected_tile_size)
    

    def test_tilesize_unexpected_value(self):
        actual_tile_size = settings.TILE_SIZE
        self.assertNotEqual(actual_tile_size, 1, f"Tile size should not be 1 but {actual_tile_size}")

    def test_rows(self):
        expected_rows = 25
        actual_rows = settings.ROWS
        self.assertEqual(actual_rows, expected_rows)

    def test_rows_unexpected_value(self):
        actual_rows = settings.ROWS
        self.assertNotEqual(actual_rows, 30, f"Rows should not be 30 but {actual_rows}")
    
    def test_cols(self):
        expected_cols = 40
        actual_cols = settings.COLS
        self.assertEqual(actual_cols, expected_cols)

    def test_cols_unexpected_value(self):
        actual_cols = settings.COLS
        self.assertNotEqual(actual_cols, 50, f"Cols should not be 50 but {actual_cols}")
    
    def test_side_panel(self):
        expected_side_panel = 300
        actual_side_panel = settings.SIDE_PANEL
        self.assertEqual(actual_side_panel, expected_side_panel)
    
    def test_side_panel_unexpected_value(self):
        actual_side_panel = settings.SIDE_PANEL
        self.assertNotEqual(actual_side_panel, 400, f"Side panel should not be 400 but {actual_side_panel}")
    
    def test_screen_width(self):
        expected_screen_width = 1280
        actual_screen_width = settings.SCREEN_WIDTH
        self.assertEqual(actual_screen_width, expected_screen_width)
    
    def test_screen_width_unexpected_value(self):
        actual_screen_width = settings.SCREEN_WIDTH
        self.assertNotEqual(actual_screen_width, 1000, f"Screen width should not be 1000 but {actual_screen_width}")

    def test_screen_height(self):
        expected_screen_height = 800
        actual_screen_height = settings.SCREEN_HEIGHT
        self.assertEqual(actual_screen_height, expected_screen_height)
    
    def test_screen_height_unexpected_value(self):
        actual_screen_height = settings.SCREEN_HEIGHT
        self.assertNotEqual(actual_screen_height, 700, f"Screen height should not be 700 but {actual_screen_height}")

    def test_fps(self):
        expected_fps = 60
        actual_fps = settings.FPS
        self.assertEqual(actual_fps, expected_fps)
    
    def test_fps_unexpected_value(self):
        actual_fps = settings.FPS
        self.assertNotEqual(actual_fps, 50, f"FPS should not be 50 but {actual_fps}")
    
    
        
if __name__ == '__main__':
    unittest.main()