import pygame
import pygame_gui
from .. import config

class Interface:
    def __init__(self, manager):
        self.manager = manager
        self.width, self.height = manager.window_resolution
        
        # Sidebar state
        self.panel_width = 230
        self.is_open = True
        self.target_x = 10
        self.current_x = 10
        self.animation_speed = 1000 # pixels per second
        
        self.setup_ui()

    def setup_ui(self):
        # The main sliding panel
        self.panel_rect = pygame.Rect((self.current_x, 10), (self.panel_width, 420))
        self.panel = pygame_gui.elements.UIPanel(relative_rect=self.panel_rect, manager=self.manager)

        # Toggle button (stays outside the panel to be clickable when collapsed)
        self.toggle_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.current_x + self.panel_width, 10), (30, 420)),
            text="<",
            manager=self.manager,
            tool_tip_text="Toggle Controls Panel"
        )

        y = 5
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Simulation Mode", manager=self.manager, container=self.panel)
        y += 25
        self.mode_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=['Standard Flocking', 'Predator-Prey', 'Obstacle Course'],
            starting_option='Standard Flocking',
            relative_rect=pygame.Rect((5, y), (self.panel_width - 25, 30)),
            manager=self.manager, container=self.panel
        )

        y += 40
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Separation Weight", manager=self.manager, container=self.panel)
        y += 20
        self.sep_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, y), (self.panel_width - 25, 20)),
            start_value=config.DEFAULT_WEIGHT_SEPARATION,
            value_range=(0, 5),
            manager=self.manager, container=self.panel
        )

        y += 30
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Alignment Weight", manager=self.manager, container=self.panel)
        y += 20
        self.ali_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, y), (self.panel_width - 25, 20)),
            start_value=config.DEFAULT_WEIGHT_ALIGNMENT,
            value_range=(0, 5),
            manager=self.manager, container=self.panel
        )

        y += 30
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect((5, y), (200, 20)), text="Cohesion Weight", manager=self.manager, container=self.panel)
        y += 20
        self.coh_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, y), (self.panel_width - 25, 20)),
            start_value=config.DEFAULT_WEIGHT_COHESION,
            value_range=(0, 5),
            manager=self.manager, container=self.panel
        )

        y += 35
        self.start_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((5, y), (95, 30)),
            text="Start",
            manager=self.manager, container=self.panel,
            tool_tip_text="Resume the simulation physics."
        )
        self.stop_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((105, y), (95, 30)),
            text="Stop",
            manager=self.manager, container=self.panel,
            tool_tip_text="Pause the simulation physics."
        )

        y += 35
        self.debug_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((5, y), (95, 30)),
            text="Debug",
            manager=self.manager, container=self.panel,
            tool_tip_text="Toggle force vector visualization."
        )
        self.trails_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((105, y), (95, 30)),
            text="Trails",
            manager=self.manager, container=self.panel,
            tool_tip_text="Toggle boid motion trails."
        )
        
        y += 35
        self.reset_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((5, y), (95, 30)),
            text="Reset",
            manager=self.manager, container=self.panel,
            tool_tip_text="Reset simulation state."
        )
        self.about_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((105, y), (95, 30)),
            text="About",
            manager=self.manager, container=self.panel,
            tool_tip_text="Show information about the simulation."
        )
        
        y += 40
        self.status_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((5, y), (200, 20)),
            text="Boids: 0",
            manager=self.manager, container=self.panel
        )

    def toggle_sidebar(self):
        self.is_open = not self.is_open
        if self.is_open:
            self.target_x = 10
            self.toggle_btn.set_text("<")
        else:
            self.target_x = -self.panel_width - 5
            self.toggle_btn.set_text(">")

    def update_animation(self, time_delta):
        if self.current_x != self.target_x:
            direction = 1 if self.target_x > self.current_x else -1
            move_amount = self.animation_speed * time_delta * direction
            
            # Don't overshoot
            if abs(self.target_x - self.current_x) < abs(move_amount):
                self.current_x = self.target_x
            else:
                self.current_x += move_amount
            
            # Update panel and toggle button positions
            self.panel.set_relative_position((self.current_x, 10))
            self.toggle_btn.set_relative_position((self.current_x + self.panel_width, 10))

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
