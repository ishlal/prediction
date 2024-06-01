

from manim import *
import coin
import light_character
import experts
import random

class Scene7(Scene):
    def construct(self):

        text_how_to_predict = Text("How do we predict?").scale(1.5).set_color(BLUE)
        self.play(Write(text_how_to_predict))

        self.wait(2)

        text_how_to_predict_anim = text_how_to_predict.animate
        self.play(text_how_to_predict_anim.shift(UP*3.1), text_how_to_predict_anim.scale(0.666))

        self.wait(1)

        line = Line(UP*2.5, DOWN*3)
        self.play(Create(line))

        text_random_guessing = Text("Random Guessing")
        text_random_guessing.shift(UP*2 + LEFT*3.9)
        underline = Underline(text_random_guessing)
        random_group = VGroup(text_random_guessing, underline)
        self.play(Write(random_group))
        self.wait(1)

        lighty = light_character.LightCharacter().light_off_character().scale(0.9).shift(LEFT*3.9 + DOWN*0.3)
        lighty_q_mark = Text("?").scale(1.5).move_to(lighty.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(Create(lighty), Create(lighty_q_mark))
        self.wait(1)

        bullet1 = Text("• 50% accuracy").scale(0.7)
        bullet2 = Text("• May take time to find \n  designated expert").scale(0.7)

        # Position the bullet points vertically in a VGroup
        bullet_list = VGroup(bullet1, bullet2).arrange(DOWN, aligned_edge=LEFT).scale(0.7)

        bullet_list.next_to(lighty, DOWN)
        bullet_list.shift(UP*0.5)
        self.play(Write(bullet_list))
        self.wait(2)

        text_experts = Text("Experts")
        text_experts.shift(UP*2 + RIGHT*3.9)
        underline2 = Underline(text_experts)
        random_group_right = VGroup(underline2, text_experts)
        self.play(Write(random_group_right))
        self.wait(1)

        expert_group = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.33)
              for _ in range(4)]
        ).arrange_in_grid(2,2, buff=0.3).shift(RIGHT*3.9 + DOWN*0.5)
        self.play(Create(expert_group))
        self.wait(1)

        bullet3 = Text("• Use the experts to influence \n prediction").scale(0.7)
        blist_group = VGroup(bullet3).arrange(DOWN, aligned_edge=LEFT).scale(0.7)

        blist_group.next_to(expert_group, DOWN)
        # blist_group.shift(UP*0.5)
        self.play(Write(blist_group))
        self.wait(2)