import pygame as pg
from field import Field
from snake import Snake
from food import Food
import sys


def main():
    # pg.init()
    unity = pg.Surface((20, 20))
    unity.fill((0, 0, 0))
    screen = pg.display.set_mode((700, 500))
    screen.fill((0, 0, 0))

    field1 = Field(screen, unity)
    snake1 = Snake((255, 255, 255), field1)
    snake2 = Snake((255, 255, 255), field1)
    apple = Food((255, 0, 0), field1)

    clock = pg.time.Clock()

    while True:
        clock.tick(20)
        snake1.update()
        snake2.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    snake1.set_direction_top()
                elif event.key == pg.K_s:
                    snake1.set_direction_down()
                elif event.key == pg.K_d:
                    snake1.set_direction_right()
                elif event.key == pg.K_a:
                    snake1.set_direction_left()
                elif event.key == pg.K_UP:
                    snake2.set_direction_top()
                elif event.key == pg.K_DOWN:
                    snake2.set_direction_down()
                elif event.key == pg.K_RIGHT:
                    snake2.set_direction_right()
                elif event.key == pg.K_LEFT:
                    snake2.set_direction_left()
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_p:
                    snake1.set_direction(0, 0)
                    snake2.set_direction(0, 0)


if __name__ == '__main__':
    main()
