# Particle Simulator

A simple 2D particle simulator built with Python and Pygame. Particles move within a defined window, bouncing off the walls to create interesting and dynamic animations.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)

## Introduction

The Particle Simulator is a fun and educational project that demonstrates basic physics principles and the use of the Pygame library for visualizing particle movement. Each particle moves with a specified speed and angle, bouncing off the walls of the window when they collide.

## Features

- Particle movement with speed and direction
- Wall collision detection and response
- Randomized particle properties (position, size, color, speed, and direction)
- Smooth animation using Pygame

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JusufS12/particleSimulator.git
    cd particleSimulator
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install pygame
    ```

## Usage

1. **Run the simulation**:
    ```bash
    python app.py
    ```

2. **Watch the particles bounce around the screen**. Close the window to exit the simulation.

## Customization

You can customize various aspects of the simulation by modifying the `app.py` file:

- **Number of particles**: Change the number of particles created in the `for` loop.
- **Particle properties**: Adjust properties like `radius`, `color`, `speed`, and `angle` in the particle initialization section.
- **Screen dimensions**: Modify `SCREEN_WIDTH` and `SCREEN_HEIGHT` to change the size of the window.