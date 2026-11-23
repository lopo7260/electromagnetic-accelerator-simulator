# Software Architecture

## Overview

The Electromagnetic Accelerator Simulator is organized into several subsystems responsible for configuration, simulation, analysis and visualization.

The general execution flow is:

```text
User
 │
 ▼
ConfigurationTab
 │
 ▼
SimulationConfig
 │
 ▼
SimulationBuilder
 │
 ▼
SimulationEngine
 │
 ▼
BeamHistory
 │
 ├── AnalysisTab
 │
 └── AnimationTab
```
---

## Project Structure
---
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

## GUI Layer
---
```text
MainWindow
│
├── ConfigurationTab
├── AnalysisTab
└── AnimationTab

```
### Configuration Tab
responsible for:
- Creating simulation moduls
- Editing field expressions
- Defining simulation parameters
- Running simualtion

### Analysis Tab
responsible for:
- Trajectory visualization
- Projection plots
- Beam analysis tools

### Animation Tab
responsible for:
- Real-time particle animation
- Playback controls
- Particle selection
- Animation timing controls

---

## Configuration System
---

Simulation parameters are stored in configuration objects.

```text
ModuleConfig
│
▼
SimulationConfig
```
### ModuleConfig
Stores the parameters of a single accelerator section:

- Name
- z_min
- z_max
- Electric field expressions
- Magnetic field expressions

### SimulationConfig
Stores global simulation parameters:

- Number of particles
- Charge-to-mass ratio
- Time step
- Number of simulation steps
- Module list

---

## Simulation Pipeline
---
The simulation process follows the pipeline below:
```text
SimulationConfig
        │
        ▼
SimulationBuilder
        │
        ▼
SimulationEngine
        │
        ▼
BeamHistory
```

### SimulationBuilder
Converts user configurations into simulation objects.

Creates:
- Beam
- Electromagnetic modules
- Field functions
- Simulation engine

### Physics Layer
The physics package contains the mathematical representation of the simulation.

Main classes:
- Beam
- FieldFunction 
- VectorField
- EM_Module
### Beam

Stores:

- Particle positions
- Particle velocities
- Charge-to-mass ratio
### FieldFunction

Represents a user-defined mathematical expression.

### VectorField

Groups three FieldFunctions into a vector field.

### EM_Module

Represents an electromagnetic region active between z_min and z_max

---
### Simulation Engine

The SimulationEngine is responsible for:

- Updating particle positions
- Updating particle velocities
- Evaluating electric fields
- Evaluating magnetic fields
- Recording simulation history
### Data Recording

Simulation results are stored inside BeamHistory.

BeamHistory contains:

- Recorded trajectories
- Simulation snapshots
- Analysis data
---
### Visualization Layer

Simulation results are visualized through two independent systems.
```text
BeamHistory
│── AnalysisTab───> Static visualization tools
│
└── AnimationTab──> Dynamic visualization tools
```
---

## Design Goals
The software was designed with the following goals:

- Modularity
- Extensibility
- Separation between GUI and simulation logic
- Real-time visualization
- Educational value