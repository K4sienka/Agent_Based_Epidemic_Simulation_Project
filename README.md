# Agent-Based Epidemic Simulation

Project developed for the **Modeling and Simulation of Systems** course.

The project implements an agent-based simulation of an infectious disease spreading through a population. It is inspired by the classical SIR model, but represents each person as an independent agent moving in a two-dimensional environment.

The simulation is used to compare how different contact patterns and intervention strategies affect the number of infections, the epidemic peak, and the total duration of the outbreak.

## Model

Each agent belongs to one of three epidemiological states:

- **S — Susceptible:** can become infected,
- **I — Infected:** can transmit the disease,
- **R — Recovered:** no longer participates in transmission.

Infection may occur when a susceptible agent is within the infection radius of an infected agent. Transmission is probabilistic, which reflects the random nature of interpersonal contact.

After a defined infection period, an infected agent moves to the recovered state.

## Implemented Scenarios

The project includes six simulation variants:

### Basic SIR

Agents move freely across the entire simulation area without additional restrictions. This scenario is used as the reference model.

### Quarantine

Infected agents are isolated after a specified delay. Quarantined agents stop moving and can no longer infect other people.

### Shared Contact Point

A selected group of agents may visit a shared public location, such as a shop. The location has its own capacity, contact radius, visit cooldown, and increased infection probability.

### Communities

The population is divided into eight communities. Agents mainly move inside their home community but may occasionally travel to another one.

This scenario produces separate epidemic waves as the disease gradually reaches new groups.

### Mobility Restrictions

When the proportion of infected agents exceeds a defined threshold, movement speed is reduced. Restrictions are removed when the infection level falls below a lower threshold.

### Social Distancing

Agents actively repel each other when they are too close. The mechanism is activated after a short delay and reduces the number of close-range contacts.

## Main Results

The experiments show that different interventions affect the epidemic in different ways:

- the basic scenario leads to a rapid outbreak affecting almost the entire population,
- quarantine lowers and delays the epidemic peak while reducing the final number of infections,
- the shared contact point changes the timing of transmission but does not strongly reduce the epidemic's total reach,
- community structure creates several separate infection waves and slows transmission between groups,
- mobility restrictions significantly extend the epidemic and reduce the peak but do not prevent most infections,
- social distancing is the most effective tested intervention and keeps the number of active cases very low.

The results also show behaviors that are difficult to reproduce with a basic compartmental SIR model, including multiple epidemic waves, step-like transmission between communities, and repeated peaks caused by dynamic restrictions.

## Project Structure

```text
project/
├── main.py
├── config.py
├── config.yaml
├── requirements.txt
├── config/
│   ├── base.yaml
│   └── scenarios/
│       ├── basic.yaml
│       ├── quarantine.yaml
│       ├── shop.yaml
│       ├── communities.yaml
│       ├── mobility_restrictions.yaml
│       └── social_distancing.yaml
├── simulation/
│   ├── app.py
│   ├── model.py
│   ├── person.py
│   ├── utils.py
│   └── scenarios/
│       ├── base_scenario.py
│       ├── basic.py
│       ├── quarantine.py
│       ├── shop.py
│       ├── communities.py
│       ├── mobility_restrictions.py
│       ├── social_distancing.py
│       └── registry.py
└── results/
```

## Configuration

Simulation parameters and the active scenario are defined in YAML configuration files. This allows experiments to be modified without changing the source code.

The configuration controls values such as:

- population size,
- initial number of infected agents,
- infection radius,
- infection probability,
- recovery time,
- agent movement speed,
- quarantine delay,
- community travel probability,
- mobility restriction thresholds,
- social-distancing strength.

## Outputs

For each scenario, the program can generate:

- a real-time Pygame visualization,
- an epidemic curve showing the number of susceptible, infected, and recovered agents,
- a GIF animation of the simulation,
- saved results for later comparison.

## Technologies

- Python
- Pygame
- Matplotlib
- Pillow
- PyYAML

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux or macOS:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Simulation

```bash
python main.py
```

Select the scenario and its parameters in the configuration files before starting the program.
