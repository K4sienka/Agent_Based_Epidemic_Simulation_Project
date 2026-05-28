from config import (
    QUARANTINE_AFTER,
    INFECTION_RADIUS,
    INFECTION_PROBABILITY,
)


class QuarantineScenario:
    name = "quarantine"

    def before_update(self, model):
        for person in model.people:
            if person.status == "I" and person.infected_time >= QUARANTINE_AFTER:
                person.is_quarantined = True

    def can_move(self, person):
        return not person.is_quarantined

    def can_infect(self, infected_person):
        return not infected_person.is_quarantined

    def get_infection_radius(self, infected_person, susceptible_person):
        return INFECTION_RADIUS

    def get_infection_probability(self, infected_person, susceptible_person):
        return INFECTION_PROBABILITY

    def draw_environment(self, screen):
        pass