from pygame.locals import K_SPACE
from globals import (
    pygame,
    clock,
    SCREEN,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_SPEED,
    COMIC_SANS,
    BLACK,
    WHITE,
)
from bird    import Bird
from ground  import Ground
from pipe    import Pipe

bird    = Bird(((int)(SCREEN_WIDTH/2), (int)(SCREEN_HEIGHT/2)), (20, 20), GAME_SPEED)
grounds = []
grounds.append( Ground(            0, SCREEN_HEIGHT / 6 ,GAME_SPEED, ( 0, 240, 10 ) ) )
grounds.append( Ground( SCREEN_WIDTH, SCREEN_HEIGHT / 6 ,GAME_SPEED, ( 0, 200, 60 ) ) )

pipes = []
pipes.append ( Pipe(2 * SCREEN_WIDTH, 80, 200, (10,170,20), GAME_SPEED ) )
pipes.append ( Pipe(3 * SCREEN_WIDTH, 80, 200, (10,170,20), GAME_SPEED ) )


def update():
    if not bird.isDead: bird.update()

    for i in grounds:
        if not bird.isDead: i.update()

    for i in pipes:
        bird.pipeCollide(i)
        if not bird.isDead: i.update(bird)

def render():
    bird.render()
    for i in grounds: i.render()
    for i in pipes  : i.render()


def keyboardInput(event):
    if event.key == K_SPACE:
        if not bird.isDead:
            bird.flap()
        else:
            pipes.clear()
            bird.reset()
            pipes.append ( Pipe(2 * SCREEN_WIDTH, 80, 200, (10,170,20), GAME_SPEED ) )
            pipes.append ( Pipe(3 * SCREEN_WIDTH, 80, 200, (10,170,20), GAME_SPEED ) )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keyboardInput(event)

    if not bird.isDead:
        SCREEN.fill((50,200,220))
        scoreText = COMIC_SANS.render("Score: " + str(bird.points), True, BLACK)
    else:
        SCREEN.fill((70,  0, 50))
        scoreText = COMIC_SANS.render("Score: " + str(bird.points), True, WHITE)

    update()
    render()

    SCREEN.blit(scoreText, ((SCREEN_WIDTH/2) - scoreText.get_width()/2, 50))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
