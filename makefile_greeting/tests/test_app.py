import unittest

from app import greet


class TestApp(unittest.TestCase):
    def test_world(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_name(self):
        self.assertEqual(greet("Chris"), "Hello, Chris!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
