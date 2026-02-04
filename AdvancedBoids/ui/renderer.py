import pygame
import numpy as np
from .. import config

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_boid(self, boid, color, show_trails=True, debug=False):
        # Draw trail
        if show_trails and len(boid.trail) > 1:
            trail_color = config.COLOR_TRAIL_BOID if color == config.COLOR_BOID else config.COLOR_TRAIL_PREDATOR
            
            # Draw trail segments, breaking them if they jump across the screen (wrapping)
            segment = [boid.trail[0].astype(int)]
            for i in range(1, len(boid.trail)):
                prev = boid.trail[i-1]
                curr = boid.trail[i]
                
                # If distance is too large, it's a wrap-around
                if np.linalg.norm(curr - prev) > 100:
                    if len(segment) > 1:
                        pygame.draw.lines(self.screen, trail_color, False, segment, 1)
                    segment = [curr.astype(int)]
                else:
                    segment.append(curr.astype(int))
            
            if len(segment) > 1:
                pygame.draw.lines(self.screen, trail_color, False, segment, 1)


        # Calculate triangle points based on velocity
        pos = boid.position.astype(int)
        vel = boid.velocity
        speed = np.linalg.norm(vel)
        
        if speed > 0:
            angle = np.arctan2(vel[1], vel[0])
        else:
            angle = 0
            
        radius = config.BOID_RADIUS if color == config.COLOR_BOID else config.PREDATOR_RADIUS
        
        # Triangle vertices
        p1 = pos + np.array([np.cos(angle) * radius * 2, np.sin(angle) * radius * 2])
        p2 = pos + np.array([np.cos(angle + 2.5) * radius, np.sin(angle + 2.5) * radius])
        p3 = pos + np.array([np.cos(angle - 2.5) * radius, np.sin(angle - 2.5) * radius])
        
        pygame.draw.polygon(self.screen, color, [p1, p2, p3])

    def draw_obstacles(self, obstacles):
        for obs in obstacles:
            pygame.draw.circle(self.screen, config.COLOR_OBSTACLE, obs.astype(int), 20)
            pygame.draw.circle(self.screen, (50, 100, 50), obs.astype(int), 22, 2)

    def draw_debug_vectors(self, boid, sep, ali, coh):
        pos = boid.position.astype(int)
        scale = 30
        if np.linalg.norm(sep) > 0:
            pygame.draw.line(self.screen, (255, 0, 0), pos, (pos + sep * scale).astype(int), 2)
        if np.linalg.norm(ali) > 0:
            pygame.draw.line(self.screen, (0, 255, 0), pos, (pos + ali * scale).astype(int), 2)
        if np.linalg.norm(coh) > 0:
            pygame.draw.line(self.screen, (0, 0, 255), pos, (pos + coh * scale).astype(int), 2)
