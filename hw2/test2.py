""" Created by Egor Iudin """
import unittest
from meta import CustomClass


class TestMetaClass(unittest.TestCase):
    """ Test class """

    def setUp(self):
        """ Set up """
        self.inst = CustomClass()

    def test_old_var_x(self):
        """ Test """
        with self.assertRaises(AttributeError):
            self.inst.x

    def test_old_func_line(self):
        """ Test """
        with self.assertRaises(AttributeError):
            self.inst.line()

    def test_new_var_x(self):
        """ Test """
        self.assertEqual(self.inst.custom_x, 50)

    def test_new_func_line(self):
        """ Test """
        self.assertEqual(self.inst.custom_line(), 100)


if __name__ == "__main__":
    unittest.main()
