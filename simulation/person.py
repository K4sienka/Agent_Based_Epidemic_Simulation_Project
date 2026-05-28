import random
import pygame

from config import WIDTH, HEIGHT, PERSON_RADIUS, SPEED


class Person:
    def __init__(self, status="S"):
        self.x = random.randint(PERSON_RADIUS, WIDTH - PERSON_RADIUS)
        self.y = random.randint(PERSON_RADIUS, HEIGHT - PERSON_RADIUS)

        self.vx = random.uniform(-SPEED, SPEED)
        self.vy = random.uniform(-SPEED, SPEED)

        self.status = status
        self.infected_time = 0

        self.is_quarantined = False
        
        self.target_x = None
        self.target_y = None
        self.shop_timer = 0
        self.can_visit_shop = False
        self.shop_cooldown = 0  

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= PERSON_RADIUS or self.x >= WIDTH - PERSON_RADIUS:
            self.vx *= -1

        if self.y <= PERSON_RADIUS or self.y >= HEIGHT - PERSON_RADIUS:
            self.vy *= -1

    def draw(self, screen):
        colors = {
            "S": (40, 120, 255),
            "I": (220, 50, 50),
            "R": (40, 180, 90),
        }

        pygame.draw.circle(
            screen,
            colors[self.status],
            (int(self.x), int(self.y)),
            PERSON_RADIUS,
        )

        if self.is_quarantined:
            pygame.draw.circle(
                screen,
                (0, 0, 0),
                (int(self.x), int(self.y)),
                PERSON_RADIUS + 3,
                2,
            )