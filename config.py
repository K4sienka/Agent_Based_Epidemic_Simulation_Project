from pathlib import Path

import yaml


CONFIG_PATH = Path(__file__).with_name("config.yaml")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    selected_scenario = data["selected_scenario"]
    base_config = data["base"]
    scenario_config = data["scenarios"].get(selected_scenario)

    if scenario_config is None:
        available = ", ".join(data["scenarios"].keys())
        raise ValueError(
            f"Nieznany scenariusz: {selected_scenario}. "
            f"Dostępne scenariusze: {available}"
        )

    config = {}
    config.update(base_config)
    config.update(scenario_config)

    config["SCENARIO_NAME"] = selected_scenario
    config["GIF_PATH"] = f'{config["RESULTS_DIR"]}/epidemia_{selected_scenario}.gif'
    config["PLOT_PATH"] = f'{config["RESULTS_DIR"]}/wykres_{selected_scenario}.png'

    return config


_config = load_config()

globals().update(_config)