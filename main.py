import pygame as pg
from constants import *
from bird import Bird
from pipe import Pipe
import time
import random




class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption("Flappy bird")
        self.font = pg.font.Font(None, 72)

        background = pg.image.load("Flappy Bird Assets/Background/Background1.png")
        self.background = pg.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


        self.setup()

        #Создание экземпляров класса
    def setup(self):
        self.bird = Bird()
        self.pipes = pg.sprite.Group()
        self.mode = "game"
        self.interval = 1.5
        self.timer = time.time()
        self.score = 0



    def run(self):
        self.is_running = True
        while self.is_running:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()
        quit()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.bird.jump()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.bird.jump()
            if self.mode == "game over":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        self.setup()




    def update(self):
        if self.bird.rect.top <= 0 or self.bird.rect.bottom >= SCREEN_HEIGHT: #pg.sprite.spritecollide(self.bird,self.pipes,False)
            self.mode = "game over"
            return
        if pg.sprite.spritecollide(self.bird,self.pipes, False):
            self.mode = "game over"
            return

        self.bird.update()
        if time.time() - self.interval >= self.timer:
            random_w = random.randint(-150,0)
            self.pipes.add(Pipe(y=random_w))
            self.pipes.add(Pipe(y=SCREEN_HEIGHT - 200 + random_w))
            self.score += 1
            self.timer = time.time()
        self.pipes.update()




    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.bird.image,self.bird.rect)
        self.pipes.draw(self.screen)
        score_text = self.font.render(f"Score:{self.score}",True,pg.Color("Black"))
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH//2,100))
        self.screen.blit(score_text,score_text_rect)
        if self.mode == "game over":
            text = self.font .render("Game over press Q", True, pg.Color("Red"))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
        pg.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()

