import unittest
from bowling.frame import Frame

from bowling.game import BowlingGame


class FrameList:
    def __init__(self, frames: list[Frame]) -> None:
        self.frames = frames

    def __getitem__(self, key):
        return self.frames[key]

    def clear_bonus(self):
        for frame in self.frames:
            frame._bonus_score = 0

    def __iter__(self):
        for frame in self.frames:
            yield frame

class TestGames(unittest.TestCase):
    game1 = FrameList([Frame(0, 2), Frame(1, 2), Frame(2, 2), Frame(2, 8), Frame(5, 2), Frame(10, 0), Frame(5, 2)])
    game2 = FrameList([Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0), Frame(10, 0)])
    almost_perfect_game = FrameList([Frame(10, 0) for _ in range(9)])


    def clear_bonus(self):
        self.game1.clear_bonus()
        self.game2.clear_bonus()
        self.almost_perfect_game.clear_bonus()

    def test_add_frame_game1(self):
        game = BowlingGame()
        list(map(game.add_frame, self.game1))

        self.assertEqual(len(game.frames), 7)
        self.assertEqual(game.frames[0].score(), 2)
        self.assertEqual(game.frames[1].score(), 3)
        self.assertEqual(game.frames[2].score(), 4)
        self.assertEqual(game.frames[3].score(), 15)
        self.assertEqual(game.frames[4].score(), 7)
        self.assertEqual(game.frames[5].score(), 17)
        self.assertEqual(game.frames[6].score(), 7)

        game.add_frame(self.game1[6])
        game.add_frame(self.game1[6])
        game.add_frame(self.game1[6])
        self.assertRaises(ValueError, game.add_frame, self.game1[6])
        self.clear_bonus()

    def test_add_frame_game2(self):
        game = BowlingGame()
        list(map(game.add_frame, self.game2))
        self.assertEqual(len(game.frames), 6)
        self.assertEqual(game.frames[0].score(), 30)
        self.assertEqual(game.frames[1].score(), 30)
        self.assertEqual(game.frames[2].score(), 30)
        self.assertEqual(game.frames[3].score(), 30)
        self.assertEqual(game.frames[4].score(), 20)
        self.assertEqual(game.frames[5].score(), 10)
        self.clear_bonus()


    def test_set_bonus(self):
        game = BowlingGame()
        list(map(game.add_frame, self.almost_perfect_game))
        game.add_frame(Frame(10, 0))
        game.set_bonus(10, 10)
        self.assertEqual(game.score(), 300)
        self.clear_bonus()

        game = BowlingGame()
        list(map(game.add_frame, self.almost_perfect_game))
        game.add_frame(Frame(0, 10))
        game.set_bonus(10, 0)
        self.assertEqual(game.score(), 270)
        self.clear_bonus()

        game = BowlingGame()
        list(map(game.add_frame, self.almost_perfect_game))
        game.add_frame(Frame(0, 10))
        self.assertRaises(ValueError, game.set_bonus, 10, 10)
        self.clear_bonus()

        game = BowlingGame()
        list(map(game.add_frame, self.almost_perfect_game))
        game.add_frame(Frame(0, 9))
        self.assertRaises(ValueError, game.set_bonus, 10, 10)
        self.clear_bonus()

        game = BowlingGame()
        list(map(game.add_frame, self.almost_perfect_game))
        game.add_frame(Frame(10, 0))
        self.assertRaises(ValueError, game.set_bonus, -1, 10)
        self.assertRaises(ValueError, game.set_bonus, 10, -1)
        self.assertRaises(ValueError, game.set_bonus, -1, -1)
        self.clear_bonus()


    def test_score_game2(self):
        game = BowlingGame()
        list(map(game.add_frame, self.game2))
        self.assertEqual(game.score(), 150)
        self.clear_bonus()

    def test_score_game1(self):
        game = BowlingGame()
        list(map(game.add_frame, self.game1))
        self.assertEqual(game.score(), 55)
        self.clear_bonus()

    def test_score_almost_perfect_game(self):
        game = BowlingGame()
        list(map(game.add_frame, self.almost_perfect_game))
        self.assertEqual(game.score(), 240)
        self.clear_bonus()


if __name__ == "__main__":
    unittest.main()
