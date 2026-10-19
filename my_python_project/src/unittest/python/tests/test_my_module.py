import unittest

from my_module import greet


class TestMyModule(unittest.TestCase):
    def test_world(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_pybuilder(self):
        self.assertEqual(greet("PyBuilder"), "Hello, PyBuilder!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
