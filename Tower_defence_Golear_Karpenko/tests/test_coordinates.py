import unittest

from Tower_defence_Golear_Karpenko.base_classes.coordinate import Coordinate


class TestCoordinates(unittest.TestCase):
    def test_init(self):
        left = Coordinate(1, 1)
        right = Coordinate((1, 1))
        mid = Coordinate(x=1, y=1)
        self.assertEqual(left, Coordinate(1, 1))
        self.assertEqual(right, Coordinate(1, 1))
        self.assertEqual(mid, Coordinate(1, 1))

    def test_equality(self):
        left = Coordinate(1, 1)
        right = Coordinate(2, 2)
        mid = Coordinate(2, 2)
        self.assertNotEqual(left, right)
        self.assertEqual(right, mid)

    def test_addition(self):
        left = Coordinate(3, 4)
        ans = Coordinate(5, 6)
        right = Coordinate(2, 2)
        left += right
        self.assertEqual(left, ans)
        ans = Coordinate(7, 8)
        self.assertEqual(left + right, ans)
        self.assertEqual(ans + 5, Coordinate(12, 13))
        ans += 5
        self.assertEqual(ans, Coordinate(12, 13))

    def test_subtraction(self):
        left = Coordinate(0, 0)
        right = Coordinate(5, 6)
        left -= right
        self.assertEqual(left, Coordinate(-5, -6))
        self.assertEqual(left - left, Coordinate(0, 0))
        self.assertEqual(left - 5, Coordinate(-10, -11))
        left -= 5
        self.assertEqual(left, Coordinate(-10, -11))

    def test_multiplication(self):
        left = Coordinate(2, 2)
        right = Coordinate(3, 3)
        self.assertEqual(left * right, Coordinate(6, 6))
        left *= right
        self.assertEqual(left, Coordinate(6, 6))
        left = Coordinate(2, 2)
        self.assertEqual(left * 3, Coordinate(6, 6))
        left *= 3
        self.assertEqual(left, Coordinate(6, 6))

    def test_division(self):
        left = Coordinate(2, 2)
        right = Coordinate(2, 2)
        self.assertEqual(left // right, Coordinate(1, 1))
        left //= right
        self.assertEqual(left, Coordinate(1, 1))
        left = Coordinate(2, 2)
        self.assertEqual(left // 2, Coordinate(1, 1))
        left //= 2
        self.assertEqual(left, Coordinate(1, 1))

    def test_unpacking(self):
        left = Coordinate(2, 2)
        mapped = {'x': 2, 'y': 2}
        self.assertEqual(left.keys(), ['x', 'y'])
        var = {key: left.__getitem__(key) for key in left.keys()}
        self.assertEqual(var, mapped)
        self.assertEqual(*left, mapped.values())


if __name__ == '__main__':
    unittest.main()
