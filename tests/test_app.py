# datasys/tests/test_app.py
import unittest
from datasys.frontend.app import demo

class TestApp(unittest.TestCase):
    def test_demo(self):
        self.assertIsNotNone(demo)

if __name__ == '__main__':
    unittest.main()