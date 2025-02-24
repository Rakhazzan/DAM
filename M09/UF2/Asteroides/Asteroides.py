import pygame
import sys
import threading
import time
import random
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set working directory
os.chdir("C:/Users/Mohamed/Documents/DAM/M09/UF2/Asteroides")

# Basic configurations
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ASTEROIDES")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Global variables
run = True
game_over = False
background_stars = []

# Initialize screen elements
ball1 = pygame.image.load("asteroide.png")
ball2 = pygame.image.load("asteroide.png")
nave = pygame.image.load("halcon.png")

# Rects for positioning and movement
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()
naverect = nave.get_rect(midbottom=(width//2, height-50))

# Randomly position asteroids
ballrect1.topleft = (random.randint(0, width-ballrect1.width), 0)
ballrect2.topleft = (random.randint(0, width-ballrect2.width), 0)

# Movement speeds
speed1 = [2, 2]
speed2 = [3, 2]

# Generate background stars
for _ in range(100):
    background_stars.append([pygame.Vector2(random.randint(0, width), random.randint(0, height)), random.randint(1, 3)])

def move_stars():
    """Move background stars continuously."""
    global background_stars
    while run:
        for star in background_stars:
            star[0].y += star[1]
            if star[0].y > height:
                star[0].y = 0
                star[0].x = random.randint(0, width)
        time.sleep(0.05)

def move_asteroid(asteroid_rect, speed_list):
    """Move an asteroid with given speed."""
    global run, naverect, game_over
    while run:
        asteroid_rect.x += speed_list[0]
        asteroid_rect.y += speed_list[1]

        # Detect collision with the spaceship
        if asteroid_rect.colliderect(naverect):
            # Reverse the asteroid's direction
            speed_list[0] = -speed_list[0]
            speed_list[1] = -speed_list[1]

        if asteroid_rect.left < 0 or asteroid_rect.right > width:
            speed_list[0] = -speed_list[0]
        if asteroid_rect.top < 0:
            speed_list[1] = -speed_list[1]
        # If any asteroid touches the bottom of the screen, end the game
        if asteroid_rect.bottom >= height:
            print("Game Over")
            game_over = True
            pygame.quit()
            sys.exit()
            return
        
        time.sleep(0.01)

def play_music():
    """Play music in a loop."""
    global run
    music_files = ["music1.mp3", "music2.mp3"]
    current_track = 0
    
    try:
        pygame.mixer.music.load(music_files[current_track])
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Music file not found. Music will be disabled.")
        pass

    while run:
        if not pygame.mixer.music.get_busy():
            current_track = (current_track + 1) % len(music_files)
            try:
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play(-1)
            except pygame.error:
                print(f"Could not load {music_files[current_track]}")
                break

def main():
    global run, naverect, ballrect1, ballrect2, game_over

    # Start threads
    threading.Thread(target=move_stars, daemon=True).start()
    threading.Thread(target=move_asteroid, args=(ballrect1, speed1), daemon=True).start()
    threading.Thread(target=move_asteroid, args=(ballrect2, speed2), daemon=True).start()
    threading.Thread(target=play_music, daemon=True).start()

    clock = pygame.time.Clock()

    # Main game loop
    while run and not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Detect keys for spaceship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and naverect.left > 0:
            naverect.x -= 5
        if keys[pygame.K_RIGHT] and naverect.right < width:
            naverect.x += 5

        # Drawing
        screen.fill(black)
        
        # Draw stars
        for star in background_stars:
            pygame.draw.circle(screen, white, (int(star[0].x), int(star[0].y)), 2)
        
        # Draw game objects
        screen.blit(ball1, ballrect1)
        screen.blit(ball2, ballrect2)
        screen.blit(nave, naverect)
        
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()