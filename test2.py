import unittest
from unittest import result
import equation2


class test2(unittest.TestCase):
    def test_equation1(self):
        result=equation2.equation1(1, -3, 2)
        self.assertEqual(result,(1,2))
    def test_equation(self):
        result=equation2.equation1(1,2,1)
        self.assertEqual(result,-1)
    def test_equation3(self):
        result=equation2.equation1(2,3,4)
        self.assertEqual(result,"pas de solution")


if __name__ == '__main__':
    unittest.main()
