import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

BG_COLOR = (0, 25, 40)

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"
    THIRD_COLOR = "black"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
            
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
        
        return self.size > 0  # Return False if target should be removed
            
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)
        pygame.draw.circle(win, self.THIRD_COLOR, (self.x, self.y), self.size * 0.2)
        
    def collide(self, x, y):
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis <= self.size 

def draw(win, targets, misses):
    win.fill(BG_COLOR)
    
    new_targets = []
    for target in targets:
        if target.update():  # Keep targets with size > 0
            new_targets.append(target)
        else:
            misses += 1  # Increment misses for each removed target
        target.draw(win)
    
    targets[:] = new_targets  # Update targets list
    pygame.display.update()
    return misses

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
    
    targets_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    
    while run:
        clock.tick(60)
        click = False  # Initialize click
        mouse_pos = pygame.mouse.get_pos()  # Update mouse position
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
        
        if click:  # Process clicks after events
            mouse_x, mouse_y = mouse_pos
            for target in targets[:]:
                if target.collide(mouse_x, mouse_y):
                    targets.remove(target)
                    targets_pressed += 1  # Fixed typo
        
        misses = draw(WIN, targets, misses)
    
    print(f"Targets Hit: {targets_pressed}, Clicks: {clicks}, Misses: {misses}")
    pygame.quit()

if __name__ == "__main__":
    main()
