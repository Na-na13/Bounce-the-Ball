import sys
import pygame
import pygame_gui


from gamewindow import GameWindow
from clock import Clock
#from gameloop import GameLoop

class End:
    def __init__(self):
        pygame.init()

        self.gamewindow = GameWindow()
        self.gameclock = Clock()
        self.background = pygame.Surface((self.gamewindow.width, self.gamewindow.height))
        self.manager = pygame_gui.UIManager((self.gamewindow.width, self.gamewindow.height))

        self.save_panel = pygame_gui.elements.UIPanel(pygame.Rect(self.gamewindow.width/2-100,
                                                self.gamewindow.height/2-80,
                                                200, 145),
                                                starting_layer_height=1,
                                                manager=self.manager,)

        self.newgame_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+70,
                                                        200, 40),
                                                        text="New Game",
                                                        manager=self.manager)
        self.savescore_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        (50,105),
                                                        (100, 40)),
                                                        text="Save Score",
                                                        manager=self.manager,
                                                        container=self.save_panel)
        #self.score_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        #                                                self.gamewindow.width/2-100,
        #                                                self.gamewindow.height/2+70,
        #                                                200, 40),
        #                                                text="High Score List",
        #                                                manager=self.manager)

        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+115,
                                                        200, 40),
                                                        text="Quit",
                                                        manager=self.manager)

        self.nick_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
                                                            (2,75),
                                                            (190,50)),
                                                            manager=self.manager,
                                                            container=self.save_panel)

        self.save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+155,
                                                        200, 40),
                                                        text="Save",
                                                        manager=self.manager,
                                                        container=self.save_panel)

        self.text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                                (2, 0),
                                                (190, 75)),
                                                html_text= "<b>Save Scores</b>"
                                                "<br>Write your name below to save your SCORES.",
                                                manager=self.manager,
                                                container=self.save_panel)

    def run(self):
        is_running = True
        clock = pygame.time.Clock()

        while is_running:
            time_delta = clock.tick(60)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        #if event.ui_element == self.newgame_button:
                        #    is_running = False
                        #    gameloop = GameLoop(self.gamewindow, self.gameclock)
                        #    gameloop.loop()
                        if event.ui_element == self.quit_button:
                            is_running = False
                            sys.exit()
                        #if event.ui_element == self.save_button:
                        #    self.inst_text.visible = True
                        #    self.return_button.visible = True
                        #if event.ui_element == self.return_button:
                        #    self.inst_text.visible = False
                        #    self.return_button.visible = False

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.gamewindow.display.blit(self.background, (0,0))
            self.manager.draw_ui(self.gamewindow.display)
            self.gameclock.clock_tick(60)
            pygame.display.update()

#if __name__ == "__main__":
#    end = End()
#    end.run()
