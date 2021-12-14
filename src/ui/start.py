import sys
import pygame
import pygame_gui

from gameloop import GameLoop

class Start:
    def __init__(self,window,clock):
        pygame.init()

        self.gamewindow = window
        self.gameclock = clock
        self.background = pygame.Surface((self.gamewindow.width, self.gamewindow.height))
        self.manager = pygame_gui.UIManager((self.gamewindow.width, self.gamewindow.height))
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2-20,
                                                        200, 40),
                                                        text="Play",
                                                        manager=self.manager)
        self.inst_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+25,
                                                        200, 40),
                                                        text="Instructions",
                                                        manager=self.manager)
        self.score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+70,
                                                        200, 40),
                                                        text="High Score List",
                                                        manager=self.manager)

        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+115,
                                                        200, 40),
                                                        text="Quit",
                                                        manager=self.manager)
        self.inst_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                                    self.gamewindow.width/2-100,
                                                    self.gamewindow.height/2-80,
                                                    200, 240),
                                                    html_text=
                                            "<b>Instructions</b>"
                                            "<br>Move ball with ARROW keys and jump with SPACE bar."
                                            "<br>Collect STARS to get points."
                                            "<br>Get to GOAL as fast as you can.",
                                                    manager=self.manager,
                                                    visible=False)
        self.return_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+155,
                                                        200, 40),
                                                        text="Return",
                                                        manager=self.manager,
                                                        visible=False)

    def run(self):
        is_running = True
        clock = pygame.time.Clock()
        while is_running:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.play_button:
                            is_running = False
                            gameloop = GameLoop(self.gamewindow, self.gameclock)
                            gameloop.loop()
                        if event.ui_element == self.quit_button:
                            is_running = False
                            sys.exit()
                        if event.ui_element == self.inst_button:
                            self.inst_text.visible = True
                            self.return_button.visible = True
                        if event.ui_element == self.return_button:
                            self.inst_text.visible = False
                            self.return_button.visible = False

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.gamewindow.display.blit(self.background, (0,0))
            self.manager.draw_ui(self.gamewindow.display)
            self.gameclock.clock_tick(60)
            pygame.display.update()
        