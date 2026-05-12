# Symulacja rozprzestrzeniania się chorób w populacji

Projekt realizowany w ramach przedmiotu **Modelowanie i symulacja systemów**.

Celem projektu jest przygotowanie symulacji rozprzestrzeniania się choroby zakaźnej w populacji z wykorzystaniem modelu SIR oraz jego późniejszych wariantów. Symulacja ma charakter agentowy - każda osoba jest reprezentowana jako niezależny obiekt poruszający się po planszy.

## Założenia modelu

Populacja dzieli się na trzy podstawowe grupy:

- **S** — osoby podatne na zakażenie,
- **I** — osoby zakażone,
- **R** — osoby ozdrowiałe/odporne.

Zakażenie może nastąpić, gdy osoba podatna znajdzie się w określonym promieniu od osoby zakażonej. Po upływie określonego czasu osoba zakażona przechodzi do stanu ozdrowienia.

## Planowane rozszerzenia

W kolejnych etapach projektu planowane jest dodanie:

- podziału populacji na społeczności,
- wspólnych miejsc kontaktu, np. sklepów,
- kwarantanny,
- ograniczenia przemieszczania się między społecznościami,
- porównania różnych scenariuszy epidemii.

## Technologie

Projekt wykorzystuje:

- Python,
- pygame,
- numpy,
- matplotlib.

## Instalacja

Utworzenie środowiska wirtualnego:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Uruchomienie

```bash
python main.py
```

## Status projektu

Na obecnym etapie przygotowywana jest podstawowa wersja symulacji agentowej SIR z prostym GUI i zapisem wyników liczby osób w poszczególnych stanach.