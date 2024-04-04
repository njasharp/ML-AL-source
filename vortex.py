from manim import *

class VortexAnimation(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=2, color=BLUE, fill_opacity=0.5)

        # Create a vortex effect using rotations and color fading
        vortex = circle.copy()
        num_iterations = 30  # Number of iterations for the vortex effect
        fade_color = YELLOW  # Color to fade into

        # Animation loop for the vortex effect
        for _ in range(num_iterations):
            self.play(
                Rotate(vortex, angle=TAU / num_iterations),
                FadeToColor(vortex, fade_color),
                run_time=0.5
            )

        self.wait(2)  # Wait for 2 seconds at the end of the animation