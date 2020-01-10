import unittest
from app import app

class TestWinter(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_helloWorld(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status,'200 OK')
        self.assertEqual(rv.data,b'Hello World')


if __name__ == '__main__':
    unittest.main()