import pygame
import matplotlib.pyplot as plt
import pandas as pd

from simulation.config import WIDTH, HEIGHT, FPS
from simulation.model import SimulationModel


def draw_stats(screen, model, font):
    susceptible = model.count_status("S")
    infected = model.count_status("I")
    recovered = model.count_status("R")

    text = f"S: {susceptible}   I: {infected}   R: {recovered}"
    surface = font.render(text, True, (0, 0, 0))
    screen.blit(surface, (20, 20))


def show_plot(history):
    plt.figure()
    plt.plot(history["S"], label="Podatni (S)")
    plt.plot(history["I"], label="Zakażeni (I)")
    plt.plot(history["R"], label="Ozdrowiali (R)")
    plt.xlabel("Krok symulacji")
    plt.ylabel("Liczba osób")
    plt.title("Przebieg epidemii w modelu SIR")
    plt.legend()
    plt.grid(True)
    plt.show()

    df = pd.DataFrame(history)
    df.to_csv("results/sir_results.csv", index=False)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Symulacja rozprzestrzeniania się choroby - model SIR")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    model = SimulationModel()

    running = True

    while running:
        screen.fill((245, 245, 245))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        model.update()

        for person in model.people:
            person.draw(screen)

        draw_stats(screen, model, font)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    show_plot(model.history)


if __name__ == "__main__":
    main()