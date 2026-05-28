from pathlib import Path

import matplotlib.pyplot as plt

import config as _cfg


def show_plot(history):
    Path(_cfg.RESULTS_DIR).mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))

    plt.plot(history["S"], label="Podatni (S)")
    plt.plot(history["I"], label="Zakażeni (I)")
    plt.plot(history["R"], label="Ozdrowiali (R)")

    plt.xlabel("Krok symulacji")
    plt.ylabel("Liczba osób")
    plt.title(f"Przebieg epidemii w modelu SIR - {_cfg.SCENARIO_NAME}")
    plt.legend()
    plt.grid(True)

    plt.savefig(_cfg.PLOT_PATH, dpi=300, bbox_inches="tight")
    plt.close()
