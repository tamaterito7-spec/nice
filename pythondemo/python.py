import sys
import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

# Tetromino shapes
SHAPES = [
    [
        ['.....',
         '.....',
         'OOOO.',
         '.....',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '..OO.',
         '.OO..',
         '.....'],
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O..',
         '..OO.',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....']
    ],
]


class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)
        self.rotation = 0


class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        return Tetromino(self.width // 2 - 2, 0, shape)

    def valid_move(self, piece, x, y, rotation):
        new_rotation = (piece.rotation + rotation) % len(piece.shape)
        shape_matrix = piece.shape[new_rotation]
        for i, row in enumerate(shape_matrix):
            for j, cell in enumerate(row):
                if cell == 'O':
                    new_x = piece.x + j + x
                    new_y = piece.y + i + y
                    if new_x < 0 or new_x >= self.width or new_y >= self.height:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x] != 0:
                        return False
        return True

    def clear_lines(self):
        lines_cleared = 0
        for i, row in enumerate(self.grid[:]):
            if all(cell != 0 for cell in row):
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)])
                lines_cleared += 1
        return lines_cleared

    def lock_piece(self, piece):
        for i, row in enumerate(piece.shape[piece.rotation % len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    if piece.y + i < self.height and piece.x + j < self.width:
                        self.grid[piece.y + i][piece.x + j] = piece.color
        lines = self.clear_lines()
        self.score += lines * 100
        self.current_piece = self.new_piece()
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True

    def update(self):
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1, 0):
                self.current_piece.y += 1
            else:
                self.lock_piece(self.current_piece)

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

        if self.current_piece:
            shape = self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]
            for i, row in enumerate(shape):
                for j, cell in enumerate(row):
                    if cell == 'O':
                        pygame.draw.rect(
                            screen,
                            self.current_piece.color,
                            ((self.current_piece.x + j) * GRID_SIZE,
                             (self.current_piece.y + i) * GRID_SIZE,
                             GRID_SIZE - 1,
                             GRID_SIZE - 1)
                        )


def draw_score(screen, score, x, y):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (x, y))


def draw_game_over(screen, x, y):
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (x, y))


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
    fall_time = 0
    fall_speed = 500  # milliseconds per fall

    while True:
        delta_time = clock.tick(60)
        fall_time += delta_time
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game.game_over:
                if event.key == pygame.K_LEFT:
                    if game.valid_move(game.current_piece, -1, 0, 0):
                        game.current_piece.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0, 0):
                        game.current_piece.x += 1
                elif event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1
                elif event.key == pygame.K_UP:
                    if game.valid_move(game.current_piece, 0, 0, 1):
                        game.current_piece.rotation = (game.current_piece.rotation + 1) % len(game.current_piece.shape)
                elif event.key == pygame.K_SPACE:
                    while game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1
                    game.lock_piece(game.current_piece)

            if game.game_over and event.type == pygame.KEYDOWN:
                game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)

        if fall_time >= fall_speed:
            game.update()
            fall_time = 0

        draw_score(screen, game.score, 10, 10)
        game.draw(screen)

        if game.game_over:
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)

        pygame.display.flip()


if __name__ == "__main__":
    main()
