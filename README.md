# Advanced Modular Boids Simulation

A high-performance flocking simulation built with Python, Pygame, and NumPy.

![Advanced Boids Simulation](https://github.com/TheCodePrism/advanced-boids-algorithm/raw/main/screenshot.png) *(Placeholder for screenshot)*

## Features

- **Modular Architecture**: Clean separation of concerns with `core`, `entities`, and `ui` packages.
- **High Performance**: Uses `scipy.spatial.cKDTree` for $O(N \log N)$ neighbor lookups, allowing hundreds of boids at 60 FPS.
- **Improved UI**: Interactive sliders for Separation, Alignment, and Cohesion weights via `pygame_gui`.
- **Advanced Behaviors**:
  - **Standard Flocking**: Emergent group behavior.
  - **Predator-Prey**: Boids flee from predators; predators hunt the nearest boids.
  - **Obstacle Avoidance**: Dynamic obstacle placement and pathfinding.
- **Smooth Visuals**: Rotated triangle boids with motion trails.

## Getting Started

### Prerequisites

- Python 3.10+
- Dependencies listed in `requirements.txt` (or install manually: `pygame`, `numpy`, `pygame_gui`, `scipy`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TheCodePrism/advanced-boids-algorithm.git
   cd advanced-boids-algorithm
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install pygame numpy pygame_gui scipy
   ```

### Running the Simulation

Execute the main script from the root directory:
```bash
export PYTHONPATH="."
python AdvancedBoids/main.py
```
*On Windows Powershell:*
```powershell
$env:PYTHONPATH="."; python AdvancedBoids/main.py
```

## How to Interact

- **Sliders**: Adjust flocking behavior in real-time.
- **Dropdown**: Switch between "Standard Flocking", "Predator-Prey", and "Obstacle Course" modes.
- **Mouse Click**: In "Obstacle Course" mode, click anywhere to place an obstacle.
- **Buttons**: Toggle "Debug" vectors or "Reset" the simulation.

## License

MIT
