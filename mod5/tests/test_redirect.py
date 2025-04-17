import io
import unittest
import sys
from mod5.Task4 import Redirect


class Test(unittest.TestCase):
    def setUp(self):
        """ Инициализация. Функция запускается перед каждым тестом """
        self.test_file_stream = sys.stdout
        self.redirect = Redirect()

    def test_define_type(self):
        self.assertIsInstance(sys.stdout, io.IOBase)

    def test_is_empty(self):
        self.assertIsNone(self.redirect.stderr)


if __name__ == '__main__':
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
