import unittest
import pygame
from gamewindow import GameWindow
from sprites.spriteball import Ball
from sprites.platform import Platform
from gameloop import GameLoop
#from game.clock import Clock

class StubClock:
    def clock_tick(self,fps):
        pass
    def clock_get_ticks(self):
        return 0

class StubGameLoop:
    def __init__(self,pl, pl2):
        self.platforms = pygame.sprite.Group()
        self.platforms.add(pl, pl2)


class TestBall(unittest.TestCase):
    def setUp(self):
        self.pl1 = Platform(0,0,5,200)
        self.testball1 = Ball(20, 200, 200, 10, None, self.pl1)

        self.pl2 = Platform(100,0,5,50) 
        self.testball2 = Ball(20, 200, 200, 10, None, self.pl2)

        self.pl3 = Platform(100,50,5,50)

        self.testgame = StubGameLoop(self.pl1,self.pl1)
        self.testball3 = Ball(20, 200, 200, 10, self.testgame, self.pl1)

        self.testgame2 = StubGameLoop(self.pl3, self.pl2)
        self.testball4 = Ball(20, 200, 200, 10, self.testgame2, self.pl3)

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

    def test_can_jump(self):
        self.assertEqual(self.testball3.jump(), True)

    def test_cannot_jump(self):
        self.testball3.jump()
        self.testball3.update()
        self.assertEqual(self.testball3.jump(), False)

    def test_hit_platform_from_down(self):
        self.testball4.jump()
        self.assertEqual(self.testball4.vertical, 10)
        self.testball4.update()
        self.testball4.update()
        self.assertEqual(self.testball4.vertical, -10)

    def test_reach_maxjumpheight(self):
        self.testball3.jump()
        for i in range(1,18):
            self.testball3.update()
        self.assertEqual(self.testball3.vertical, -10)
        for j in range(1,18):
            self.testball3.update()
        self.assertEqual(self.testball3.vertical, 0)
        
