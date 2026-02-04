## About the Research Simulation

This project serves as a platform for **Collective Intelligence Research** and **Emergent Behavior Analysis**. By decoupling environmental factors from agent logic, we can analyze how simple local rules result in complex global patterns.

### Core Research Areas
- **Swarm Intelligence**: Analyzing how decentralized systems achieve high-level coordination without global control.
- **Predatory Dynamics**: Studying evasion strategies and the evolution of "selfish herd" behaviors.
- **Pathfinding Optimization**: Evaluating swarm efficiency in navigating constrained spatial environments (Obstacle Navigation).

### Technical Functionalities
- **Spatial Grid Optimization**: High-performance neighbor lookup using $k$-d trees.
- **Real-time Parametric Tuning**: Dynamic manipulation of flocking weights to observe phase transitions in behavior.
- **Vector Debugging**: Visual overlay of internal force vectors for behavioral auditing.

## How it Affects the Boids (The Physics)

Understanding the sliders is key to the experimentation:

- **Separation**: The "Push" force. Higher values prevent collisions and create a sparse, cloud-like flock. Low values lead to overlapping and denser groups.
- **Alignment**: The "Direction" force. High alignment makes the flock move as a single rigid unit. Low alignment results in chaotic, swirling motion.
- **Cohesion**: The "Pull" force. High cohesion keeps the flock tightly knit. Low cohesion allows boids to wander off individually.

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
