class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        if first_throw + second_throw > 10:
            raise ValueError("Invalid Frame")
        if first_throw < 0 or second_throw < 0:
            raise ValueError("Invalid Frame")

        self.first_throw = first_throw
        self.second_throw = second_throw
        self._bonus_score = 0

    def score(self) -> int:
        """The score of a single frame"""
        return self.first_throw + self.second_throw + self._bonus_score

    def is_strike(self) -> bool:
        """Return whether the frame is a strike or not"""
        return self.first_throw == 10

    def is_spare(self) -> bool:
        """Return whether the frame is a spare or not"""
        return (self.first_throw + self.second_throw == 10) and (not self.is_strike())

    def bonus(self, bonus_score: int, is_last=False):
        if not is_last and bonus_score > 10:
            raise ValueError("Invalid Bonus")
        if is_last and bonus_score > 20:
            raise ValueError("Invalid Bonus")
        self._bonus_score += bonus_score
