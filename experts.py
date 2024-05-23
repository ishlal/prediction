from manim import *

class experts(Scene):
    def get_expert(self, x):
        expert = None
        if x == 1:
            expert = SVGMobject("images/expert_1 (2).svg").scale(2.5)
        elif x == 2:
            expert = SVGMobject("images/expert_2 (2).svg").scale(2.5)
        elif x == 3:
            expert = SVGMobject("images/expert_3 (2).svg").scale(2.5)
        elif x == 4:
            expert = SVGMobject("images/expert_4 (2).svg").scale(2.5)
        return expert
    
    def designated_expert(self):
        expert = SVGMobject("images/designated_expert.svg").scale(2.5)
        return expert

    def construct(self):
        expert = self.get_expert(1)
        expert.shift(LEFT*5)
        expert_2 = self.get_expert(2)
        expert_2.shift(LEFT*2)
        expert_3 = self.get_expert(3)
        expert_3.shift(RIGHT*1)
        expert_4 = self.get_expert(4)
        expert_4.shift(RIGHT*4)
        self.play(Create(expert), Create(expert_2), Create(expert_3), Create(expert_4))
        self.wait(1)