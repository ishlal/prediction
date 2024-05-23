from manim import *

class Person(Scene):

    def rounded_rect(self):
        rounded_rectangle = RoundedRectangle(
            width=2.0,        # Width of the rectangle
            height=3.0,       # Height of the rectangle
            corner_radius=0.5, # Radius of the corners
            color=WHITE        # Color of the rectangle
        )
        
        # Add the RoundedRectangle to the scene
        return rounded_rectangle
    
    def get_person(self):
        # Head
        head = Circle(radius=0.5, color=WHITE)
        head.shift(UP * 2)

        # Body
        body = Line(start=head.get_bottom(), end=head.get_bottom() + DOWN * 2, color=WHITE)

        # Arms
        left_arm = Line(start=body.get_center(), end=body.get_center() + LEFT * 1 + UP * 0.5, color=WHITE)
        right_arm = Line(start=body.get_center(), end=body.get_center() + RIGHT * 1 + UP * 0.5, color=WHITE)

        # Legs
        left_leg = Line(start=body.get_end(), end=body.get_end() + LEFT * 0.7 + DOWN * 1, color=WHITE)
        right_leg = Line(start=body.get_end(), end=body.get_end() + RIGHT * 0.7 + DOWN * 1, color=WHITE)

        # Grouping all parts
        person = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)

        # Animation
        return person

    
    def construct(self):
        # person = self.get_person()
        # self.play(Create(person))
        # self.wait(1)
        
        person = self.wider_person()
        self.play(Create(person))
        self.wait(1)

