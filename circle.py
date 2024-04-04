from manim import *

class Test(Scene):
    def construct(self):
        c = Circle(radius=2, color=RED, fill_opacity=0.1)

        self.play(Create(c), run_time=0.5)

        title = Text("Manim", font_size=72, slant="ITALIC").shift(UP * 0.3)
        subtitle = Text("Basics", slant="ITALIC").shift(DOWN * 0.5)
        self.play(Write(title), Write(subtitle))

        a = Arc(radius=2.2, start_angle=TAU * 1 / 4, angle=-TAU * 2.6 / 4, color=BLUE, stroke_width=15)
        self.play(Create(a))

        self.wait(6)
