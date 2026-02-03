import pygame
import numpy as np
from .spatial import SpatialManager
from ..entities.boid import Boid
from ..entities.predator import Predator
from .. import config

class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boids = []
        self.predators = []
        self.obstacles = []
        
        self.spatial_manager = SpatialManager()
        self.mode = "Standard Flocking"
        self.debug_mode = False
        
        self.weights = {
            "separation": config.DEFAULT_WEIGHT_SEPARATION,
            "alignment": config.DEFAULT_WEIGHT_ALIGNMENT,
            "cohesion": config.DEFAULT_WEIGHT_COHESION
        }
        
    def reset(self):
        self.boids = [Boid(np.random.rand() * self.width, np.random.rand() * self.height) for _ in range(config.BOID_COUNT)]
        self.predators = [Predator(np.random.rand() * self.width, np.random.rand() * self.height) for _ in range(config.PREDATOR_COUNT)]
        self.obstacles = []

    def handle_click(self, pos):
        if self.mode == "Obstacle Course":
            self.obstacles.append(np.array(pos, dtype=np.float64))

    def update(self):
        # Update spatial partitioning with current boid positions
        positions = [boid.position for boid in self.boids]
        self.spatial_manager.update(positions)
        
        for i, boid in enumerate(self.boids):
            # Query neighbors
            neighbor_indices = self.spatial_manager.query_radius(boid.position, boid.perception)
            neighbors = [self.boids[idx] for idx in neighbor_indices if idx != i]
            
            # Calculate forces
            sep, ali, coh = boid.flock(neighbors)
            
            boid.apply_force(sep * self.weights["separation"])
            boid.apply_force(ali * self.weights["alignment"])
            boid.apply_force(coh * self.weights["cohesion"])
            
            # Mode specific logic
            if self.mode == "Predator-Prey":
                for predator in self.predators:
                    boid.apply_force(boid.flee(predator.position) * config.DEFAULT_WEIGHT_PREDATOR_FLEE)
            
            if self.mode == "Obstacle Course":
                boid.apply_force(boid.avoid_obstacles(self.obstacles) * config.DEFAULT_WEIGHT_AVOIDANCE)
            
            boid.update(self.width, self.height)
            
        # Update predators
        if self.mode == "Predator-Prey":
            for predator in self.predators:
                hunt_force = predator.hunt(self.boids)
                predator.apply_force(hunt_force * config.DEFAULT_WEIGHT_HUNT)
                predator.update(self.width, self.height)
