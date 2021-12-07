import unittest
from game.sprites.spriteball import Ball
from game.sprites.platform import Platform
from game.gameloop import GameLoop
#from game.clock import Clock

class TestBall(unittest.TestCase):
    def setUp(self):
        self.pl1 = Platform(0,0,5,200)
        self.testball1 = Ball(20, 200, 200, 10, None, self.pl1)

        self.pl2 = Platform(100,0,5,50) 
        self.testball2 = Ball(20, 200, 200, 10, None, self.pl2)

        self.testgame = GameLoop()
        #self.testball3 = Ball(20, 200, 200, 10, self.testgame, self.pl2)

    def test_move_right(self):
        self.testball1.move_right()
        self.assertEqual(self.testball1.rect.x, 90)

    def test_stop_move_right(self):
        for i in range(1,8):
            self.testball1.move_right()
        move = self.testball1.move_right()
        self.assertEqual(move, False)

    def test_move_left(self):
        self.testball1.move_left()
        self.assertEqual(self.testball1.rect.x, 70)

    def test_stop_move_left(self):
        for i in range(1,8):
            self.testball1.move_left()
        move = self.testball1.move_left()
        self.assertEqual(move, False)

    def test_fall_from_platform_right(self):
        for i in range(1,5):
            self.testball2.move_right()
        self.assertEqual(self.testball2.vertical, -10)

    def test_fall_from_platform_left(self):
        for i in range(1,5):
            self.testball2.move_left()
        self.assertEqual(self.testball2.vertical, -10)

    #def test_can_jump(self):
    #    self.assertEqual(self.testball1.jump(), True)
