import unittest
from app import add, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 5), 0)

if __name__ == "__main__":
    unittest.main()
