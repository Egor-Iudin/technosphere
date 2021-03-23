""" Created by Egor Iudin """
import unittest
from .custom_list import CustomList


class TestMetaClass(unittest.TestCase):
    """ Test class """

    def test_add_sim(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a, CustomList([1, 7, 5, 4]))
        self.assertEqual(b, CustomList([8, 5, 11]))
        self.assertEqual(a+b, CustomList([9, 12, 16, 4]))

    def test_add_dif(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = [8, 5, 11]
        self.assertEqual(a, CustomList([1, 7, 5, 4]))
        self.assertEqual(b, [8, 5, 11])
        self.assertEqual(a+b, CustomList([9, 12, 16, 4]))

    def test_radd_dif(self):
        """ Test """
        a = [1, 7, 5, 4]
        b = CustomList([8, 5, 11])
        self.assertEqual(a, [1, 7, 5, 4])
        self.assertEqual(b, CustomList([8, 5, 11]))
        self.assertEqual(a+b, CustomList([9, 12, 16, 4]))

    def test_sub_sim(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a, CustomList([1, 7, 5, 4]))
        self.assertEqual(b, CustomList([8, 5, 11]))
        self.assertEqual(a-b, CustomList([-7, 2, -6, 4]))

    def test_add_dif(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = [8, 5, 11]
        self.assertEqual(a, CustomList([1, 7, 5, 4]))
        self.assertEqual(b, [8, 5, 11])
        self.assertEqual(a-b, CustomList([-7, 2, -6, 4]))

    def test_radd_dif(self):
        """ Test """
        a = [1, 7, 5, 4]
        b = CustomList([8, 5, 11])
        self.assertEqual(a, [1, 7, 5, 4])
        self.assertEqual(b, CustomList([8, 5, 11]))
        self.assertEqual(a-b, CustomList([-7, 2, -6, 4]))

    def test_eq(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a == b, False)

        a = CustomList([1, 5, 66, 4])
        b = CustomList([8, 5, 11, -7])
        self.assertEqual(a == b, False)

    def test_ne(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a != b, True)

        a = CustomList([1, 5, 66, 4])
        b = CustomList([8, 5, 11, -7])
        self.assertEqual(a != b, True)

    def test_ge(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a >= b, False)

        a = CustomList([1, 5, 66, 4])
        b = CustomList([8, 5, 11, -7])
        self.assertEqual(a >= b, True)

    def test_le(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a <= b, True)

        a = CustomList([1, 5, 66, 4])
        b = CustomList([8, 5, 11, -7])
        self.assertEqual(a <= b, False)

    def test_gt(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a > b, False)

        a = CustomList([1, 5, 66, 4])
        b = CustomList([8, 5, 11, -7])
        self.assertEqual(a > b, True)

    def test_lt(self):
        """ Test """
        a = CustomList([1, 7, 5, 4])
        b = CustomList([8, 5, 11])
        self.assertEqual(a < b, True)

        a = CustomList([1, 5, 66, 4])
        b = CustomList([8, 5, 11, -7])
        self.assertEqual(a < b, False)


if __name__ == "__main__":
    unittest.main()
