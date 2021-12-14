from ui.start import Start
from gamewindow import GameWindow
from clock import Clock

def main():
    gamewindow = GameWindow()
    gameclock = Clock()
    game = Start(gamewindow, gameclock)
    game.run()

if __name__ == '__main__':
    main()
