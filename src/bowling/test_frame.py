import unittest
from .frame import Frame

class TestFrames(unittest.TestCase):
    def test_score_normal_frame(self):
        """ The score of a single frame """
        frame = Frame(2, 3)
        self.assertEqual(frame.score(), 5)

    def test_bonus(self):
        """ The score of a single frame """
        frame = Frame(2, 8)
        frame.bonus(5)
        self.assertEqual(frame.score(), 15)
        self.assertRaises(ValueError, frame.bonus, 11)
        frame = Frame(0, 10)
        frame.bonus(15, True)
        self.assertEqual(frame.score(), 25)
        frame = Frame(0, 10)
        self.assertRaises(ValueError, frame.bonus, 25, True)


    def test_valid_frame(self):
        self.assertRaises(ValueError, Frame, 2, 10)
        self.assertRaises(ValueError, Frame, -2, 10)
        self.assertRaises(ValueError, Frame, -2, -10)
        self.assertRaises(ValueError, Frame, 2, -10)

    def test_is_strike(self):
        """ Return whether the frame is a strike or not """
        strike = Frame(10, 0)
        spare = Frame(0, 10)
        normal = Frame(5, 3)
        self.assertTrue(strike.is_strike())
        self.assertFalse(spare.is_strike())
        self.assertFalse(normal.is_strike())

    def test_is_spare(self):
        """ Return whether the frame is a spare or not """
        strike = Frame(10, 0)
        spare = Frame(0, 10)
        normal = Frame(5, 3)
        self.assertFalse(strike.is_spare())
        self.assertTrue(spare.is_spare())
        self.assertFalse(normal.is_spare())


if __name__ == '__main__':
    unittest.main()
