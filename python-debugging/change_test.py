from change import ChangeItForMe
import unittest


class TestChange(unittest.TestCase):
    def test_calculate(self):
        changer = ChangeItForMe()

        self.assertEqual(changer.calculate(100), [0, 0, 0, 0, 1])
        self.assertEqual(changer.calculate(25), [0, 0, 0, 1, 0])
        self.assertEqual(changer.calculate(10), [0, 0, 1, 0, 0])
        self.assertEqual(changer.calculate(5), [0, 1, 0, 0, 0])
        self.assertEqual(changer.calculate(1), [1, 0, 0, 0, 0])

        self.assertEqual(changer.calculate(141), [1, 1, 1, 1, 1])
        self.assertEqual(changer.calculate(99), [4, 0, 2, 3, 0])
        self.assertEqual(changer.calculate(207), [2, 1, 0, 0, 2])

    def test_transact(self):
        changer = ChangeItForMe()

        self.assertEqual(changer.transact(20, 100), [0, 1, 0, 3, 0])
        self.assertEqual(changer.transact(56, 100), [4, 1, 1, 1, 0])


if __name__ == "__main__":
    unittest.main()
