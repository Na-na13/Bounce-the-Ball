import unittest
from game.ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.testball = Ball(20, 200, 200, 10)

    def test_move_right(self):
        self.testball.move_right()
        self.assertEqual(self.testball.ball_x, 110)

    def test_stop_move_right(self):
        for i in range(1,8):
            self.testball.move_right()
        move = self.testball.move_right()
        self.assertEqual(move, False)

    def test_move_left(self):
        self.testball.move_left()
        self.assertEqual(self.testball.ball_x, 90)

    def test_stop_move_left(self):
        for i in range(1,8):
            self.testball.move_left()
        move = self.testball.move_left()
        self.assertEqual(move, False)

    def test_move_up(self):
        self.testball.move_up()
        self.assertEqual(self.testball.ball_y,158)

    def test_move_down(self):
        self.testball.move_up()
        self.testball.move_up()
        self.testball.move_down()
        self.assertEqual(self.testball.ball_y, 158)