# Eletromagnetic Accelerator Simulator

A scientific simulation and visualization tool developed to model and display the trajectories of charged particles in electromagnetic fields.

This project allows users to:
- Create custom electromagnetic modules.
- Define electric and magnetic field components using mathematical expressions.
- Simulate charged particle beam dynamics.
- Analyze trajectories through different visualization tools.
- Replay particle motion through an interactive animation interface.
---
## Features

### Simulation

- Random Gaussian charged particle beam generation
- Configurable electromagnetic modules
- Custom electric and magnetic fields
- Multiple sequential accelerator sections
- Beam trajectory recording

### Analysis

- 3D trajectory visualization
- XY, XZ and YZ projections
- Beam profile inspection

### Animation

- Real-time particle animation
- Play / Pause / Reset controls
- Adjustable number of displayed particles
- Uniform frame sampling for long simulations

## Installation

Clone the repository:

```bash
git clone https://github.com/lopo7260/electromagnetic-accelerator-simulator.git
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the application

Start the simulator with:

```bash
python src/main.py
```

---

## Project Structure

```text
src/

├── analysis/
├── components/
├── config/
├── graphics/
├── gui/
├── physics/
├── simulation/

└── main.py
```

---

## Documentation

Additional documentation is available in the `docs` directory:

- Architecture documentation
- Physics documentation
- User guide

---

Current Version: **Beta 1.0**

Implemented:

- Simulation engine
- Configuration GUI
- Analysis GUI
- Animation GUI
- Electric field support
- Magnetic field support
- Beam history recording

---

## License

This project is released under the MIT License.