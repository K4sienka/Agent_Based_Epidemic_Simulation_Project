from config import INFECTION_RADIUS, INFECTION_PROBABILITY


class BasicScenario:
    name = "basic"

    def before_update(self, model):
        pass

    def can_move(self, person):
        return True

    def can_infect(self, infected_person):
        return True

    def get_infection_radius(self, infected_person, susceptible_person):
        return INFECTION_RADIUS

    def get_infection_probability(self, infected_person, susceptible_person):
        return INFECTION_PROBABILITY

    def draw_environment(self, screen):
        pass