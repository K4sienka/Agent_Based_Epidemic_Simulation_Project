import math
import random

import pygame

from config import (
    SPEED,
    SHOP_X,
    SHOP_Y,
    SHOP_RADIUS,
    SHOP_VISITOR_SHARE,
    SHOP_VISIT_PROBABILITY,
    SHOP_STAY_TIME,
    SHOP_COOLDOWN,
    SHOP_CAPACITY,
    SHOP_INFECTION_RADIUS,
    SHOP_INFECTION_PROBABILITY,
    INFECTION_RADIUS,
    INFECTION_PROBABILITY,
)


class ShopScenario:
    name = "shop"

    def __init__(self):
        self.initialized = False

    def initialize_people(self, model):
        for person in model.people:
            person.can_visit_shop = random.random() < SHOP_VISITOR_SHARE
            person.shop_cooldown = random.randint(0, SHOP_COOLDOWN)

        self.initialized = True

    def before_update(self, model):
        if not self.initialized:
            self.initialize_people(model)

        active_shop_people = sum(
            1
            for person in model.people
            if person.target_x is not None or self.is_in_shop(person)
        )

        for person in model.people:
            if not person.can_visit_shop:
                continue

            if person.shop_cooldown > 0:
                person.shop_cooldown -= 1

            if person.shop_timer > 0:
                person.shop_timer -= 1
                person.vx = random.uniform(-0.4, 0.4)
                person.vy = random.uniform(-0.4, 0.4)

                if person.shop_timer == 0:
                    person.shop_cooldown = SHOP_COOLDOWN
                    person.vx = random.uniform(-SPEED, SPEED)
                    person.vy = random.uniform(-SPEED, SPEED)

                continue

            if (
                person.target_x is None
                and person.shop_cooldown == 0
                and active_shop_people < SHOP_CAPACITY
                and random.random() < SHOP_VISIT_PROBABILITY
            ):
                person.target_x = SHOP_X
                person.target_y = SHOP_Y
                active_shop_people += 1

            if person.target_x is not None:
                dx = SHOP_X - person.x
                dy = SHOP_Y - person.y
                distance = math.sqrt(dx**2 + dy**2)

                if distance <= SHOP_RADIUS:
                    person.target_x = None
                    person.target_y = None
                    person.shop_timer = SHOP_STAY_TIME

                elif distance > 0:
                    person.vx = SPEED * dx / distance
                    person.vy = SPEED * dy / distance

    def can_move(self, person):
        return True

    def can_infect(self, infected_person):
        return True

    def is_in_shop(self, person):
        distance = math.sqrt((person.x - SHOP_X) ** 2 + (person.y - SHOP_Y) ** 2)
        return distance <= SHOP_RADIUS

    def get_infection_radius(self, infected_person, susceptible_person):
        if self.is_in_shop(infected_person) and self.is_in_shop(susceptible_person):
            return SHOP_INFECTION_RADIUS

        return INFECTION_RADIUS

    def get_infection_probability(self, infected_person, susceptible_person):
        if self.is_in_shop(infected_person) and self.is_in_shop(susceptible_person):
            return SHOP_INFECTION_PROBABILITY

        return INFECTION_PROBABILITY

    def draw_environment(self, screen):
        pygame.draw.circle(screen, (230, 225, 170), (SHOP_X, SHOP_Y), SHOP_RADIUS)
        pygame.draw.circle(screen, (120, 110, 60), (SHOP_X, SHOP_Y), SHOP_RADIUS, 3)