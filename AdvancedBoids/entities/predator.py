import numpy as np
from .boid import Boid
from .. import config

class Predator(Boid):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.max_speed = config.PREDATOR_MAX_SPEED
        self.max_force = config.PREDATOR_MAX_FORCE
        self.perception = config.PREDATOR_PERCEPTION
        self.max_trail_length = 30 # Longer trails for predators

    def hunt(self, boids):
        if not boids:
            return np.zeros(2)
            
        closest_boid = None
        min_dist = float('inf')
        
        # Simply find the closest boid to hunt
        for boid in boids:
            dist = np.linalg.norm(self.position - boid.position)
            if dist < min_dist:
                min_dist = dist
                closest_boid = boid
                
        if closest_boid:
            return self.steer_to(closest_boid.position)
        return np.zeros(2)
