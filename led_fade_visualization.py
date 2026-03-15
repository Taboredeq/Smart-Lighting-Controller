import pygame
import sys

#Configuration
WINDOW_WIDTH = 2400
WINDOW_HEIGHT = 512
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("LED Fade & Gradient Visualization")
clock = pygame.time.Clock()


def draw_marker_line(x_position, base_y):
    """
    Draws small vertical white marker lines every 100 pixels.
    """
    if x_position % 100 == 0:
        for y_offset in range(10):
            screen.set_at((x_position, base_y + y_offset), WHITE)


def draw_color_gradient(offset_x=0, offset_y=10):
    """
    Draws a 256x256 RGB gradient block.
    """
    for y in range(256):
        for x in range(256):
            screen.set_at((x + offset_x, y + offset_y), (x, y, 0))


def draw_led_path(offset_x=0, offset_y=10):
    """
    Draws a simple LED path simulating red fade-in, orange transition, and red fade-out.
    """
    # Red fade-in
    for red in range(256):
        screen.set_at((red + offset_x, offset_y), WHITE)
    # Orange transition (small green addition)
    for green in range(11):
        screen.set_at((255 + offset_x, green + offset_y), WHITE)
    # Red fade-out with proportional green
    for red in range(255, -1, -1):
        screen.set_at((red + offset_x, red // 16 + offset_y), WHITE)


def draw_fade_in(start_y, marker_y):
    """
    Simulates LED fade-in effect (red increasing, subtle green for orange).
    """
    for y in range(start_y, start_y + 50):
        x_position = 0

        # Red fade-in
        for red in range(256):
            for _ in range(5):
                screen.set_at((x_position, y), (red, 0, 0))
                x_position += 1
                draw_marker_line(x_position, marker_y)

        # Orange transition
        for green in range(11):
            for _ in range(100):
                screen.set_at((x_position, y), (255, green, 0))
                x_position += 1
                draw_marker_line(x_position, marker_y)


def draw_fade_out(start_y, marker_y):
    """
    Simulates LED fade-out effect (red decreasing with proportional green).
    """
    for y in range(start_y, start_y + 50):
        x_position = 0
        for red in range(255, -1, -1):
            for _ in range(5):
                green = red // 16
                screen.set_at((x_position, y), (red, green, 0))
                x_position += 1
                draw_marker_line(x_position, marker_y)


def main():
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Draw gradients and simulated LED paths
        draw_color_gradient()
        draw_color_gradient(offset_x=300)
        draw_led_path(offset_x=300)
        draw_fade_in(start_y=300, marker_y=350)
        draw_fade_out(start_y=400, marker_y=450)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()