import pygame

from config import WIDTH, HEIGHT, FPS, SAVE_GIF, SCENARIO_NAME

from simulation.model import SimulationModel
from simulation.visualization import draw_stats
from simulation.plots import show_plot
from simulation.recorder import GifRecorder
from simulation.scenarios.registry import get_scenario


def run_simulation():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Symulacja epidemii - scenariusz: {SCENARIO_NAME}")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    scenario = get_scenario(SCENARIO_NAME)
    model = SimulationModel(scenario)

    recorder = GifRecorder() if SAVE_GIF else None

    running = True

    while running:
        screen.fill((245, 245, 245))
        scenario.draw_environment(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        model.update()

        for person in model.people:
            person.draw(screen)

        draw_stats(screen, model, font)

        if recorder:
            recorder.capture(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

    if recorder:
        recorder.save()

    show_plot(model.history)