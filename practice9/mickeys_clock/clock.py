import pygame
import time
class MickeyClock:
    def __init__(self):
        self.center_x=300
        self.center_y=300
    def create_hand(self, color, length, width):
        hand = pygame.Surface((width, length), pygame.SRCALPHA) 
        pygame.draw.rect(
            hand, color,
            (width // 2 - 8, length // 2, 16, length // 2 - 5)
        )

        # Draw the glove palm
        pygame.draw.circle(
            hand, color,
            (width // 2, length // 2 - 10), 18
        )

        # Draw fingers
        pygame.draw.circle(hand, color, (width // 2 - 12, length // 2 - 25), 9)
        pygame.draw.circle(hand, color, (width // 2 - 4, length // 2 - 35), 9)
        pygame.draw.circle(hand, color, (width // 2 + 5, length // 2 - 35), 9)
        pygame.draw.circle(hand, color, (width // 2 + 13, length // 2 - 25), 9)

        return hand

    def draw(self, screen):
        # Get current system time
        current_time = time.localtime()

        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Convert time to angles
        minute_angle = minutes * 6
        second_angle = seconds * 6

        # Create hands
        minute_hand = self.create_hand((0, 0, 0), 180, 60)
        second_hand = self.create_hand((220, 0, 0), 140, 50)

        # Rotate hands
        rotated_minute = pygame.transform.rotate(minute_hand, -minute_angle)
        rotated_second = pygame.transform.rotate(second_hand, -second_angle)

        # Draw hands at clock center
        minute_rect = rotated_minute.get_rect(center=(self.center_x, self.center_y))
        second_rect = rotated_second.get_rect(center=(self.center_x, self.center_y))

        screen.blit(rotated_minute, minute_rect)
        screen.blit(rotated_second, second_rect)

        # Display digital time
        font = pygame.font.SysFont("Arial", 40)
        time_text = font.render(
            f"{minutes:02d}:{seconds:02d}", True, (0, 0, 0)
        )

        text_rect = time_text.get_rect(center=(300, 500))
        screen.blit(time_text, text_rect)