import numpy as np
from .. import config

class Boid:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=np.float64)
        self.velocity = np.random.rand(2) * 2 - 1
        self.acceleration = np.zeros(2)
        
        self.max_speed = config.BOID_MAX_SPEED
        self.max_force = config.BOID_MAX_FORCE
        self.perception = config.BOID_PERCEPTION
        self.separation_dist = config.BOID_SEPARATION_DIST
        
        self.trail = []
        self.max_trail_length = 20

    def apply_force(self, force):
        self.acceleration += force

    def update(self, width, height):
        self.velocity += self.acceleration
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity = (self.velocity / speed) * self.max_speed
            
        # Update trail
        self.trail.append(self.position.copy())
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)
            
        self.position += self.velocity
        self.acceleration = np.zeros(2)
        
        # Wrapping
        self.position[0] %= width
        self.position[1] %= height

    def steer_to(self, target):
        """Steers towards a target position."""
        desired = target - self.position
        dist = np.linalg.norm(desired)
        if dist > 0:
            desired = (desired / dist) * self.max_speed
            steer = desired - self.velocity
            steer_mag = np.linalg.norm(steer)
            if steer_mag > self.max_force:
                steer = (steer / steer_mag) * self.max_force
            return steer
        return np.zeros(2)

    def flock(self, neighbors):
        """Standard flocking rules: Separation, Alignment, Cohesion."""
        sep = np.zeros(2)
        ali = np.zeros(2)
        coh = np.zeros(2)
        
        total = len(neighbors)
        if total == 0:
            return sep, ali, coh
            
        sum_pos = np.zeros(2)
        sum_vel = np.zeros(2)
        sep_count = 0
        
        for neighbor in neighbors:
            dist = np.linalg.norm(self.position - neighbor.position)
            
            # Separation
            if 0 < dist < self.separation_dist:
                diff = self.position - neighbor.position
                diff /= (dist * dist) # Inverse square weighting
                sep += diff
                sep_count += 1
                
            sum_pos += neighbor.position
            sum_vel += neighbor.velocity
            
        # Alignment
        avg_vel = sum_vel / total
        mag = np.linalg.norm(avg_vel)
        if mag > 0:
            avg_vel = (avg_vel / mag) * self.max_speed
            ali = avg_vel - self.velocity
            ali_mag = np.linalg.norm(ali)
            if ali_mag > self.max_force:
                ali = (ali / ali_mag) * self.max_force
                
        # Cohesion
        avg_pos = sum_pos / total
        coh = self.steer_to(avg_pos)
        
        # Finish Separation
        if sep_count > 0:
            sep /= sep_count
            sep_mag = np.linalg.norm(sep)
            if sep_mag > 0:
                sep = (sep / sep_mag) * self.max_speed
                sep = sep - self.velocity
                if np.linalg.norm(sep) > self.max_force:
                    sep = (sep / np.linalg.norm(sep)) * self.max_force
                    
        return sep, ali, coh

    def avoid_obstacles(self, obstacles):
        steer = np.zeros(2)
        for obstacle in obstacles:
            dist = np.linalg.norm(self.position - obstacle)
            if dist < 40: # Obstacle radius + buffer
                steer += self.steer_to(2 * self.position - obstacle)
        return steer

    def flee(self, predator_pos):
        dist = np.linalg.norm(self.position - predator_pos)
        if dist < self.perception:
            return self.steer_to(2 * self.position - predator_pos)
        return np.zeros(2)
