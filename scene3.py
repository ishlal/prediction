
from manim import *
import coin
import light_character
import experts
import random

class scene3(Scene):
    def construct(self):
        main_text = Text("What should you do to earn the most money?")
        self.play(Write(main_text))
        self.wait(1)

        text_random_guessing = Text("Random Guessing")
        text_random_guessing.shift(UP*3)
        underline = Underline(text_random_guessing)
        random_group = VGroup(text_random_guessing, underline)
        self.play(Transform(main_text, random_group))
        self.wait(1)

        
        vgroup_rectangles = VGroup(
            *[Rectangle(width=6, height=2.5, color=WHITE, fill_opacity=0) for _ in range(4)]
        ).arrange_in_grid(2, 2, buff=0.5)
        vgroup_rectangles.shift(DOWN*0.75)
        self.play(Create(vgroup_rectangles))
        self.wait(1)

        lighty_1 = light_character.LightCharacter().light_off_character().scale(0.6).shift(vgroup_rectangles[0].get_center())
        lighty_1.shift(LEFT*2)
        lighty_1_coin = coin.H.copy().scale(0.4).move_to(lighty_1.get_center() + RIGHT*0.8 + UP*0.8)
        square_1 = Square().scale(0.6)
        square_1.set_fill(color=WHITE, opacity=0)
        square_1.move_to(vgroup_rectangles[0].get_center() + RIGHT*1.5)
        square_coin = coin.H.copy().scale(0.6).move_to(square_1.get_center())
        self.play(Create(lighty_1), Create(lighty_1_coin), Create(square_1), Create(square_coin))

        lighty_2 = light_character.LightCharacter().light_off_character().scale(0.6).shift(vgroup_rectangles[1].get_center())
        lighty_2.shift(LEFT*2)
        lighty_2_coin = coin.H.copy().scale(0.4).move_to(lighty_2.get_center() + RIGHT*0.8 + UP*0.8)
        square_2 = Square().scale(0.6)
        square_2.set_fill(color=WHITE, opacity=0)
        square_2.move_to(vgroup_rectangles[1].get_center() + RIGHT*1.5)
        square_coin_2 = coin.T.copy().scale(0.6).move_to(square_2.get_center())
        self.play(Create(lighty_2), Create(lighty_2_coin), Create(square_2), Create(square_coin_2))

        lighty_3 = light_character.LightCharacter().light_off_character().scale(0.6).shift(vgroup_rectangles[2].get_center())
        lighty_3.shift(LEFT*2)
        lighty_3_coin = coin.T.copy().scale(0.4).move_to(lighty_3.get_center() + RIGHT*0.8 + UP*0.8)
        square_3 = Square().scale(0.6)
        square_3.set_fill(color=WHITE, opacity=0)
        square_3.move_to(vgroup_rectangles[2].get_center() + RIGHT*1.5)
        square_coin_3 = coin.H.copy().scale(0.6).move_to(square_3.get_center())
        self.play(Create(lighty_3), Create(lighty_3_coin), Create(square_3), Create(square_coin_3))

        lighty_4 = light_character.LightCharacter().light_off_character().scale(0.6).shift(vgroup_rectangles[3].get_center())
        lighty_4.shift(LEFT*2)
        lighty_4_coin = coin.T.copy().scale(0.4).move_to(lighty_4.get_center() + RIGHT*0.8 + UP*0.8)
        square_4 = Square().scale(0.6)
        square_4.set_fill(color=WHITE, opacity=0)
        square_4.move_to(vgroup_rectangles[3].get_center() + RIGHT*1.5)
        square_coin_4 = coin.T.copy().scale(0.6).move_to(square_4.get_center())
        self.play(Create(lighty_4), Create(lighty_4_coin), Create(square_4), Create(square_coin_4))

        one_fourth_1 = Text("1/4").scale(0.5).move_to(vgroup_rectangles[0].get_center() + UP*0.9)
        one_fourth_2 = Text("1/4").scale(0.5).move_to(vgroup_rectangles[1].get_center() + UP*0.9)
        one_fourth_3 = Text("1/4").scale(0.5).move_to(vgroup_rectangles[2].get_center() + UP*0.9)
        one_fourth_4 = Text("1/4").scale(0.5).move_to(vgroup_rectangles[3].get_center() + UP*0.9)

        self.play(Create(one_fourth_1), Create(one_fourth_2), Create(one_fourth_3), Create(one_fourth_4))
        self.wait(1)

        dollar_1 = Text("$1").scale(0.5).move_to(vgroup_rectangles[0].get_center() + DOWN*0.9)
        dollar_2 = Text("$0").scale(0.5).move_to(vgroup_rectangles[1].get_center() + DOWN*0.9)
        dollar_3 = Text("$0").scale(0.5).move_to(vgroup_rectangles[2].get_center() + DOWN*0.9)
        dollar_4 = Text("$1").scale(0.5).move_to(vgroup_rectangles[3].get_center() + DOWN*0.9)
        self.play(Create(dollar_1), Create(dollar_2), Create(dollar_3), Create(dollar_4))
        self.wait(1)
        
        self.play(vgroup_rectangles[0].animate.set_color(GREEN), vgroup_rectangles[3].animate.set_color(GREEN))
        self.wait(1)

        self.play(vgroup_rectangles[1].animate.set_color(RED), vgroup_rectangles[2].animate.set_color(RED))
        self.wait(1)

        self.play(main_text.animate.shift(LEFT*4))
        self.wait(2)

        math = MathTex(r"\implies")
        math.next_to(main_text, RIGHT)
        more_text = Text("Expected Earnings:").scale(0.5)
        more_text.next_to(math, RIGHT)
        expr = MathTex(r"\mathbb{E}[E]=\tfrac12 \cdot \$1 + \tfrac12 \cdot \$0 = \tfrac12").scale(0.7)
        expr.next_to(more_text, RIGHT)
        self.play(Write(math), Write(more_text), Write(expr))
        self.wait(2)
        group_ee = VGroup(math, more_text, expr)
        self.play(group_ee.animate.shift(UP*0.5))
        self.wait(1)

        last_stuff = Text("After M rounds:").scale(0.5)
        math_last = MathTex(r"\mathbb{E}[E]=\tfrac12 \cdot M").scale(0.7)
        math_last.next_to(last_stuff, RIGHT)
        group_last = VGroup(last_stuff, math_last)
        group_last.next_to(group_ee, DOWN)
        self.play(Write(group_last))
        self.wait(2)