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
                                                self.gamewindow.height/2-60,
                                                250, 165),
                                                starting_layer_height=1,
                                                manager=self.manager,)
        self.save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        (77,118),
                                                        (100, 40)),
                                                        text="Save",
                                                        visible=False,
                                                        manager=self.manager,
                                                        container=self.save_panel)
        self.nick_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
                                                    (32,91),
                                                    (190,50)),
                                                    manager=self.manager,
                                                    visible=False,
                                                    container=self.save_panel)
        self.nick_entry.set_text_length_limit(9)
        self.text = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                                (2, 0),
                                                (240, 93)),
                                                html_text=self.get_text(self.time),
                                                manager=self.manager,
                                                container=self.save_panel)
        self.newgame_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+115,
                                                        200, 40),
                                                        text="New Game",
                                                        manager=self.manager)
        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
                                                        self.gamewindow.width/2-100,
                                                        self.gamewindow.height/2+160,
                                                        200, 40),
                                                        text="Quit",
                                                        manager=self.manager)
        self.score_list = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                                    self.gamewindow.width/2-100,
                                                    self.gamewindow.height/2-115,
                                                    200, 225),
                                                    html_text= "<b>Text</b>",
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
                        if event.ui_element == self.newgame_button:
                            is_running = False
                            self.game.new_game()
                        if event.ui_element == self.quit_button:
                            is_running = False
                            sys.exit()
                        if event.ui_element == self.save_button:
                            nick = self.nick_entry.get_text().strip()
                            if  nick != "":
                                self.save(nick, self.time)

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.gamewindow.display.blit(self.background, (0,0))
            self.manager.draw_ui(self.gamewindow.display)
            self.gameclock.clock_tick(60)
            pygame.display.update()

    def save(self, name, gametime):
        scores = []
        with open("high_score.txt","r") as file:
            for line in file:
                if "\n" in line or line == "":
                    continue
                parts = line.split(";")
                nick = str(parts[0])
                time = float(parts[1])
                scores.append((nick,time))
        if float(gametime) < float(scores[-1][1]):
            scores.remove(scores[-1])
            scores.append((name,float(gametime)))
            scores.sort(key=lambda x:x[1])
            with open("high_score.txt","w") as file:
                for i in range(0,len(scores)):
                    file.write(f"{str(scores[i][0])};{float(scores[i][1])}\n")
        self.save_panel.kill()
        scorelist = "<b>Best Times</b>"
        i = 1

        for score in scores:
            scorelist = scorelist + f"<br><b>{i}: </b>{score[0]}: {score[1]}"
            i += 1
        score_list = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect(
                                            self.gamewindow.width/2-100,
                                            self.gamewindow.height/2-115,
                                            200, 225),
                                            html_text= scorelist,
                                            manager=self.manager,)

    def get_text(self,playtime):
        scores = []
        with open("high_score.txt","r") as file:
            for line in file:
                if line == "\n" or line == "":
                    continue
                parts = line.split(";")
                nick = str(parts[0])
                time = parts[1]
                scores.append((nick,time))

        if playtime < scores[-1][1]:
            self.save_button.visible = True
            self.nick_entry.visible = True
            txt = f"<b>Well played!</b><br><b>Your time: {playtime} sec!</b><br>Write your name below to SAVE your TIME."
            return txt
        self.save_button.disable()
        self.nick_entry.disable()
        txt = f"<b>Well played!</b><br><b>Your time: {playtime} sec!</b>"
        return txt
