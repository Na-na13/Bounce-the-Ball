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
                                                        text="Best times",
                                                        manager=self.manager)
        self.return_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+160,
                                                        200, 40),
                                                        text="Return",
                                                        manager=self.manager,
                                                        visible=False)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+115,
                                                        200, 40),
                                                        text="Quit",
                                                        manager=self.manager)
        self.inst_text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                                    self.gamewindow.width/2-100,
                                                    self.gamewindow.height/2-40,
                                                    200, 195),
                                                    html_text=
                                            "<b>Instructions</b>"
                                            "<br>Move ball with ARROW keys and jump with SPACE bar."
                                            "<br>Collect 10 STARS as fast as you can."
                                            "<br>Press ESC to start new game."
                                            "<br>Press Q to exit game.",
                                                    manager=self.manager,
                                                    visible=False)
        self.score_list = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                                    self.gamewindow.width/2-100,
                                                    self.gamewindow.height/2-70,
                                                    200, 225),
                                                    html_text= self.get_scorelist(),
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
                            self.show_textbox(self.inst_text)
                        if event.ui_element == self.return_button:
                            if self.inst_text.visible is True:
                                self.hide_textbox(self.inst_text)
                            if self.score_list.visible is True:
                                self.hide_textbox(self.score_list)
                        if event.ui_element == self.score_button:
                            self.show_textbox(self.score_list)

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.gamewindow.display.blit(self.background, (0,0))
            self.manager.draw_ui(self.gamewindow.display)
            self.gameclock.clock_tick(60)
            pygame.display.update()

    def show_textbox(self, textbox):
        textbox.visible = True
        self.return_button.visible = True
        self.play_button.disable()
        self.score_button.disable()
        self.inst_button.disable()
        self.quit_button.disable()

    def hide_textbox(self, textbox):
        textbox.visible = False
        self.return_button.visible = False
        self.play_button.enable()
        self.score_button.enable()
        self.inst_button.enable()
        self.quit_button.enable()

    def get_scorelist(self):
        with open("high_score.txt","r") as file:
            scores = []
            for line in file:
                if line == "\n" or line == "":
                    continue
                parts = line.split(";")
                nick = parts[0]
                time = parts[1].strip()
                scores.append((nick,time))

        scorelist = "<b>Best Times</b>"
        i = 1

        for score in scores:
            scorelist = scorelist + f"<br><b>{i}: </b>{score[0]}: {score[1]}"
            i += 1
        return scorelist
