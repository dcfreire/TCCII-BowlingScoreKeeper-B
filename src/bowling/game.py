from typing import List

from bowling.frame import Frame


class BowlingGame:
    def __init__(self) -> None:
        self.frames: List[Frame] = []
        self.strike_flag = False

    def add_frame(self, frame: Frame):
        if len(self.frames) == 10:
            raise ValueError("Maximum ammount of frames reached")

        if self.frames:
            if self.strike_flag:
                self.frames[-2].bonus(frame.first_throw)
                self.strike_flag = False
            if self.frames[-1].is_spare():
                self.frames[-1].bonus(frame.first_throw)
            if self.frames[-1].is_strike():
                if frame.is_strike():
                    self.strike_flag = True
                self.frames[-1].bonus(frame.score())

        self.frames.append(frame)

    def set_bonus(self, first_throw: int, second_throw: int):
        if len(self.frames) < 10:
            raise ValueError("Bonus throws are only allowed on the last frame")
        if self.frames[-1].is_spare() and second_throw > 0:
            raise ValueError("Spares only get one bonus throw")
        if not (self.frames[-1].is_strike() or self.frames[-1].is_spare()):
            raise ValueError("Only last frames with either a spare or a strike get a bonus throw")
        if first_throw < 0 or second_throw < 0 or first_throw > 10 or second_throw > 10:
            raise ValueError("Invalid bonus throw")

        if self.strike_flag:
            self.frames[-2].bonus(first_throw)
            self.strike_flag = False

        self.frames[-1].bonus(first_throw + second_throw, is_last=True)

    def score(self) -> int:
        """ Get the score from the game """
        return sum(map(lambda frame: frame.score(), self.frames))
