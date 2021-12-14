import sys
import pygame
import pygame_gui

class End:
    def __init__(self,game,time):
        pygame.init()

        self.game = game
        self.gamewindow = game.window
        self.gameclock = game.clock
        self.time = f"{time:.2f}"
        self.background = pygame.Surface((self.gamewindow.width, self.gamewindow.height))
        self.manager = pygame_gui.UIManager((self.gamewindow.width, self.gamewindow.height))
        self.save_panel = pygame_gui.elements.UIPanel(pygame.Rect(self.gamewindow.width/2-125,
                                                self.gamewindow.height/2-100,
                                                250, 165),
                                                starting_layer_height=1,
                                                manager=self.manager,)
        self.text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                                (2, 0),
                                                (240, 93)),
                                                html_text= "<b>Well played!</b>"
                                                "<br><b>Your time: {time} sec!</b>"
                                                "<br>Write your name below to SAVE your TIME.".format(time=self.time),
                                                manager=self.manager,
                                                container=self.save_panel)
        self.nick_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
                                                    (32,91),
                                                    (190,50)),
                                                    manager=self.manager,
                                                    container=self.save_panel)
        self.savescore_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        (77,118),
                                                        (100, 40)),
                                                        text="Save",
                                                        manager=self.manager,
                                                        container=self.save_panel)
        self.newgame_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+70,
                                                        200, 40),
                                                        text="New Game",
                                                        manager=self.manager)
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
        #self.save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
        #                                                self.gamewindow.width/2-100,
        #                                                self.gamewindow.height/2+155,
        #                                                200, 40),
        #                                                text="Save",
        #                                                manager=self.manager,
        #                                                container=self.save_panel)

    def run(self):
        is_running = True
        clock = pygame.time.Clock()
        while is_running:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.newgame_button:
                            is_running = False
                            self.game.new_game()
                        if event.ui_element == self.quit_button:
                            is_running = False
                            sys.exit()
                        #if event.ui_element == self.save_button:
                        #    save scores to file

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.gamewindow.display.blit(self.background, (0,0))
            self.manager.draw_ui(self.gamewindow.display)
            self.gameclock.clock_tick(60)
            pygame.display.update()
