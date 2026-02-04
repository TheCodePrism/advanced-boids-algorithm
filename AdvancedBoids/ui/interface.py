import pygame
import pygame_gui
from .. import config

class Interface:
    def __init__(self, manager):
        self.manager = manager
        self.width, self.height = manager.window_resolution
        self.setup_ui()

    def setup_ui(self):
        panel_rect = pygame.Rect((10, 10), (220, 360))
        self.panel = pygame_gui.elements.UIPanel(relative_rect=panel_rect, manager=self.manager)

        y = 5
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Simulation Mode", manager=self.manager, container=self.panel)
        y += 25
        self.mode_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=['Standard Flocking', 'Predator-Prey', 'Obstacle Course'],
            starting_option='Standard Flocking',
            relative_rect=pygame.Rect((5, y), (200, 30)),
            manager=self.manager, container=self.panel
        )

        y += 40
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Separation Weight", manager=self.manager, container=self.panel)
        y += 20
        self.sep_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, y), (200, 20)),
            start_value=config.DEFAULT_WEIGHT_SEPARATION,
            value_range=(0, 5),
            manager=self.manager, container=self.panel
        )

        y += 30
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Alignment Weight", manager=self.manager, container=self.panel)
        y += 20
        self.ali_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, y), (200, 20)),
            start_value=config.DEFAULT_WEIGHT_ALIGNMENT,
            value_range=(0, 5),
            manager=self.manager, container=self.panel
        )

        y += 30
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Cohesion Weight", manager=self.manager, container=self.panel)
        y += 20
        self.coh_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, y), (200, 20)),
            start_value=config.DEFAULT_WEIGHT_COHESION,
            value_range=(0, 5),
            manager=self.manager, container=self.panel
        )

        y += 35
        self.debug_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((5, y), (100, 30)),
            text="Debug",
            manager=self.manager, container=self.panel
        )
        self.reset_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((110, y), (95, 30)),
            text="Reset",
            manager=self.manager, container=self.panel
        )


        y += 35
        self.about_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((5, y), (200, 30)),
            text="About Simulation",
            manager=self.manager, container=self.panel
        )
        
        y += 40
        self.status_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((5, y), (200, 20)),
            text="Boids: 0",
            manager=self.manager, container=self.panel
        )

    def show_about_window(self):
        about_text = (
            "<b>Advanced Boids Research Simulation</b><br><br>"
            "This application is designed for experimentation with emergent collective behavior using Craig Reynolds' Boids algorithm.<br><br>"
            "<b>The Three Core Rules:</b><br>"
            "1. <b>Separation:</b> Steer to avoid crowding local flockmates.<br>"
            "2. <b>Alignment:</b> Steer towards the average heading of local flockmates.<br>"
            "3. <b>Cohesion:</b> Steer to move towards the average position of local flockmates.<br><br>"
            "<b>Advanced Features:</b><br>"
            "- <b>Spatial Partitioning:</b> Uses cKDTree for efficient O(N log N) computation.<br>"
            "- <b>Predator-Prey Logic:</b> Simulates evasion tactics against larger predators.<br>"
            "- <b>Obstacle Navigation:</b> Evaluates pathfinding in complex environments.<br><br>"
            "<b>Uses:</b><br>"
            "- Researching swarm intelligence and decentralized systems.<br>"
            "- Educational tool for understanding vector mathematics and physics simulations."
        )
        pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((self.width // 2 - 250, self.height // 2 - 200), (500, 400)),
            html_message=about_text,
            manager=self.manager,
            window_title="About the Simulation"
        )

    def update_status(self, boid_count):

        self.status_label.set_text(f"Boids: {boid_count}")
