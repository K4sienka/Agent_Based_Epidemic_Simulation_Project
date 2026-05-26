import random
import math

from config import (
    POPULATION_SIZE,
    INITIAL_INFECTED,
    RECOVERY_TIME,
)

from simulation.person import Person


class SimulationModel:
    def __init__(self, scenario):
        self.scenario = scenario
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
        self.scenario.before_update(self)

        for person in self.people:
            if self.scenario.can_move(person):
                person.move()

        self.spread_infection()
        self.recover_people()
        self.save_history()

    def spread_infection(self):
        infected_people = [p for p in self.people if p.status == "I"]
        susceptible_people = [p for p in self.people if p.status == "S"]

        for infected in infected_people:
            if not self.scenario.can_infect(infected):
                continue

            for susceptible in susceptible_people:
                distance = math.sqrt(
                    (infected.x - susceptible.x) ** 2
                    + (infected.y - susceptible.y) ** 2
                )

                infection_radius = self.scenario.get_infection_radius(infected, susceptible)
                infection_probability = self.scenario.get_infection_probability(infected, susceptible)

                if distance <= infection_radius:
                    if random.random() < infection_probability:
                        susceptible.status = "I"
                        susceptible.infected_time = 0

    def recover_people(self):
        for person in self.people:
            if person.status == "I":
                person.infected_time += 1

                if person.infected_time >= RECOVERY_TIME:
                    person.status = "R"
                    person.is_quarantined = False

    def save_history(self):
        self.history["S"].append(self.count_status("S"))
        self.history["I"].append(self.count_status("I"))
        self.history["R"].append(self.count_status("R"))

    def count_status(self, status):
        return sum(1 for person in self.people if person.status == status)