from manim import *

class RotatingCube(ThreeDScene):
    def construct(self):
        # Create a cube
        cube = Cube(side_length=2, color=BLUE)

        # Set initial position and add to the scene
        cube.shift(IN * 3)  # Shift the cube 3 units towards the camera
        self.add(cube)

        # Rotate the cube continuously
        self.play(
            Rotate(cube, angle=TAU, axis=OUT, run_time=4, rate_func=linear)
        )

        self.wait(2)  # Wait for 2 seconds at the end of the animation