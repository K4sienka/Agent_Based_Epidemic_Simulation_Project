import random
import math

from simulation.config import (
    POPULATION_SIZE,
    INITIAL_INFECTED,
    INFECTION_RADIUS,
    INFECTION_PROBABILITY,
    RECOVERY_TIME,
)

from simulation.person import Person


class SimulationModel:
    def __init__(self):
        self.people = []

        for i in range(POPULATION_SIZE):
            if i < INITIAL_INFECTED:
                self.people.append(Person(status="I"))
            else:
                self.people.append(Person(status="S"))

        self.history = {
            "S": [],
            "I": [],
            "R": [],
        }

    def update(self):
        for person in self.people:
            person.move()

        self.spread_infection()
        self.recover_people()
        self.save_history()

    def spread_infection(self):
        infected_people = [p for p in self.people if p.status == "I"]
        susceptible_people = [p for p in self.people if p.status == "S"]

        for infected in infected_people:
            for susceptible in susceptible_people:
                distance = math.sqrt(
                    (infected.x - susceptible.x) ** 2
                    + (infected.y - susceptible.y) ** 2
                )

                if distance <= INFECTION_RADIUS:
                    if random.random() < INFECTION_PROBABILITY:
                        susceptible.status = "I"

    def recover_people(self):
        for person in self.people:
            if person.status == "I":
                person.infected_time += 1

                if person.infected_time >= RECOVERY_TIME:
                    person.status = "R"

    def save_history(self):
        self.history["S"].append(self.count_status("S"))
        self.history["I"].append(self.count_status("I"))
        self.history["R"].append(self.count_status("R"))

    def count_status(self, status):
        return sum(1 for person in self.people if person.status == status)