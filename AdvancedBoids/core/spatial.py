import numpy as np
from scipy.spatial import cKDTree

class SpatialManager:
    """Wrapper for scipy.spatial.cKDTree to handle spatial partitioning."""
    def __init__(self):
        self.tree = None
        self.points = None

    def update(self, positions):
        """Build the tree from an array of positions."""
        if len(positions) == 0:
            self.tree = None
            return
            
        self.points = np.array(positions)
        self.tree = cKDTree(self.points)

    def query_radius(self, position, radius):
        """Returns indices of points within radius of position."""
        if self.tree is None:
            return []
        return self.tree.query_ball_point(position, radius)
