import pygame
import pygame_gui
from AdvancedBoids import config
from AdvancedBoids.core.engine import Engine
from AdvancedBoids.ui.renderer import Renderer
from AdvancedBoids.ui.interface import Interface

def main():
    pygame.init()
    pygame.display.set_caption("Advanced Modular BOIDS Simulation")
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    clock = pygame.time.Clock()
    
    manager = pygame_gui.UIManager((config.WIDTH, config.HEIGHT))
    engine = Engine(config.WIDTH, config.HEIGHT)
    renderer = Renderer(screen)
    interface = Interface(manager)
    
    engine.reset()
    
    running = True
    while running:
        time_delta = clock.tick(config.FPS) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not manager.get_focus_set(): # Only if not clicking UI
                    engine.handle_click(event.pos)
            
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == interface.mode_dropdown:
                    engine.mode = event.text
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == interface.start_btn:
                    engine.is_running = True
                if event.ui_element == interface.stop_btn:
                    engine.is_running = False
                if event.ui_element == interface.debug_btn:
                    engine.debug_mode = not engine.debug_mode
                if event.ui_element == interface.trails_btn:
                    engine.show_trails = not engine.show_trails
                if event.ui_element == interface.reset_btn:
                    engine.reset()
                if event.ui_element == interface.about_btn:
                    interface.show_about_window()
            
            manager.process_events(event)
            
        # Sync UI settings to engine
        engine.weights["separation"] = interface.sep_slider.get_current_value()
        engine.weights["alignment"] = interface.ali_slider.get_current_value()
        engine.weights["cohesion"] = interface.coh_slider.get_current_value()
        
        if engine.is_running:
            engine.update()
            
        interface.update_status(len(engine.boids))

        
        # Render
        screen.fill(config.COLOR_BACKGROUND)
        
        if engine.mode == "Obstacle Course":
            renderer.draw_obstacles(engine.obstacles)
            
        for boid in engine.boids:
            if engine.debug_mode:
                # Re-calculate forces for debug drawing (simplified)
                neighbor_indices = engine.spatial_manager.query_radius(boid.position, boid.perception)
                neighbors = [engine.boids[idx] for idx in neighbor_indices if engine.boids[idx] != boid]
                sep, ali, coh = boid.flock(neighbors)
                renderer.draw_debug_vectors(boid, sep, ali, coh)
            
            renderer.draw_boid(boid, config.COLOR_BOID, show_trails=engine.show_trails)

            
        if engine.mode == "Predator-Prey":
            for predator in engine.predators:
                renderer.draw_boid(predator, config.COLOR_PREDATOR, show_trails=engine.show_trails)

                
        manager.update(time_delta)
        manager.draw_ui(screen)
        
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()
