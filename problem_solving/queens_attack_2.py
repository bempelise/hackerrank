"""
HackerRank - Queen's Attack II
https://www.hackerrank.com/challenges/queens-attack-2/problem

You will be given a square chess board with one queen and a number of obstacles placed on it.
Determine how many squares the queen can attack.
"""

class Limits():
    """ Holds the limits on queen's movement on a line """
    def __init__(self, minimum, maximum):
        self._minimum = minimum
        self._maximum = maximum

    @property
    def minimum(self):
        """ lowerst position in line """
        return self._minimum

    @minimum.setter
    def minimum(self, value):
        self._minimum = value

    @property
    def maximum(self):
        """ highest position in line """
        return self._maximum

    @maximum.setter
    def maximum(self, value):
        self._maximum = value

    @property
    def positions(self):
        """ The number of possible positions"""
        return self._maximum - self._minimum

    def update(self, obstacle_pos, queen_pos):
        """ Update the limits based on obstacle"""
        if obstacle_pos > queen_pos:
            self.maximum = min([obstacle_pos - 1, self.maximum])
        else:
            self.minimum = max([obstacle_pos + 1, self.minimum])

    def __str__(self):
        return "[" + str(self.minimum) + " - " + str(self.maximum) + "]"


def queensAttack(size, k, r_q, c_q, obstacles):
    """ Queen Attack """
    attacks = 0

    row_limits = Limits(1, size)
    for obs in obstacles:
        if obs[0] == r_q:
            row_limits.update(obs[1], c_q)
    attacks += row_limits.positions

    column_limits = Limits(1, size)
    for obs in obstacles:
        if obs[1] == c_q:
            column_limits.update(obs[0], r_q)
    attacks += column_limits.positions

    diff = r_q - c_q
    diag_limits = Limits(max(1, diff + 1), min(size, size + diff))
    for obs in obstacles:
        if obs[0] - obs[1] == diff:
            diag_limits.update(obs[0], r_q)
    attacks += diag_limits.positions

    total = r_q + c_q
    reverse_diag_limits = Limits(max([1, total - size]), min(size, total - 1))
    for obs in obstacles:
        if obs[0] + obs[1] == total:
            reverse_diag_limits.update(obs[0], r_q)
    attacks += reverse_diag_limits.positions

    print(row_limits)
    print(column_limits)
    print(diag_limits)
    print(reverse_diag_limits)
    return attacks


def main():
    """ main """
    # size = 5
    # r_q = 4
    # c_q = 3
    # obstacles = [[5, 5], [4, 2], [2, 3]]

    # size = 8
    # r_q = 5
    # c_q = 4
    # obstacles = []

    size = 100000
    r_q = 4187
    c_q = 5068
    obstacles = []
    k = len(obstacles)
    print(queensAttack(size, k, r_q, c_q, obstacles))


if __name__ == '__main__':
    main()
