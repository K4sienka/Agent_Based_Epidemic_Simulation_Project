def draw_stats(screen, model, font):
    susceptible = model.count_status("S")
    infected = model.count_status("I")
    recovered = model.count_status("R")

    text = f"S: {susceptible}   I: {infected}   R: {recovered}"
    surface = font.render(text, True, (0, 0, 0))
    screen.blit(surface, (20, 20))