def get_scenario(name):
    if name == "basic":
        from simulation.scenarios.basic import BasicScenario
        return BasicScenario()

    if name == "quarantine":
        from simulation.scenarios.quarantine import QuarantineScenario
        return QuarantineScenario()

    if name == "shop":
        from simulation.scenarios.shop import ShopScenario
        return ShopScenario()

    available = "basic, quarantine, shop"
    raise ValueError(f"Nieznany scenariusz: {name}. Dostępne scenariusze: {available}")