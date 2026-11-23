# User Guide


## Introduction

This guide explains how to configure, run and analyze simulations using the Electromagnetic Accelerator Simulator.

---

## Creating a Simulation

The workflow consists of:

1. Creating one or more electromagnetic modules.
2. Defining electric and magnetic field expressions.
3. Choosing simulation parameters.
4. Running the simulation.
5. Inspecting the results through the Analysis and Animation tabs.

### Adding Modules

Press **Add Module** to create a new accelerator section.

Each module contains:

```text
┌───────────────────────┐
│      ModuleConfig     │
├───────────────────────┤
│ name                  │
│ z_min                 │
│ z_max                 │
│ Ex                    │
│ Ey                    │
│ Ez                    │
│ Bx                    │
│ By                    │
│ Bz                    │
└───────────────────────┘
```

### Editing Module Parameters

- name: Module identifier.
- z_min: Beginning of the active region.
- z_max: End of the active region.
- Ex, Ey, Ez: Electric field components.
- Bx, By, Bz: Magnetic field components.

### Simulation Parameters

```text
Particles ─>  number of simulated particles.
q/m ───────> charge-to-mass ratio.
dt ────────> integration time step.
Steps ─────> number of simulation iterations.
```

## Writing Field Expressions

Field components are defined through mathematical expressions.

### Variables

```text
x
y
z
t
```

### Constants

```text
pi = 3.1415925358
E = 2.7182818284
```

### Functions

```text
sin()
cos()
tan()
exp()
sqrt()
```

### Operators

```text
+
-
*
/
**
```

### Examples

Constant field

```text
100
```

Sinusoidal field

```text
100*sin(pi*z)
```

Time-dependent field

```text
100*cos(t)
```

Gaussian profile

```text
exp(-z**2)
```

## Analysis Tab
The Analysis Tab provides visualization tools for simulation results. 

Available plots:

```text
- 3D Trajectories
- projection
- xy scatter
```

## Animation Tab

The Animation Tab provides a real-time animation of the simulated particles.

Available controls:

- Play / Pause / Reset
- Particle Selector

