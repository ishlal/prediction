from manim import *
import coin
import light_character
import experts
import random

class scene14(Scene):
    def construct(self):

        upper_text = Text("Suppose our algorithm makes M mistakes").scale(1).shift(UP*3)
        underline = Underline(upper_text)
        self.play(Write(upper_text), Create(underline))
        self.wait(2)