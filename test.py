import unittest
from unittest import result
import equation


class test(unittest.TestCase):
    def test_equation1(self):
        result=equation.equation1(2,4)
        self.assertEqual(result,-2)
    def test_equation(self):
        result=equation.equation1(0,4)
        self.assertEqual(result,"pas de solution")
    def test_equation2(self):
        result=equation.equation1(0,0)
        self.assertEqual(result,"tout reel est solution")


if __name__ == '__main__':
    unittest.main()
