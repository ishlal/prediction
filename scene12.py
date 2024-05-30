from manim import *
import coin
import light_character
import experts
import random

class scene12(Scene):
    def construct(self):
        line = Line(UP*3, DOWN*3)
        self.play(Create(line))

        text_best_case = Text("Old Scenario").scale(1).shift(UP*3 + LEFT*3.5)
        self.play(Create(text_best_case), run_time = 1)
        self.wait(1)

        text_round_1 = Text("Exists an Always Correct Expert").scale(0.5).next_to(text_best_case, DOWN)
        self.play(Create(text_round_1), run_time = 1)
        self.wait(2)

        designated_expert = experts.experts().designated_expert().scale(0.2)
        expert_group = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.2) if j!= 10 else
              designated_expert
              for j in range(16)]
        ).arrange_in_grid(4, 4, buff=0.16).next_to(text_round_1, DOWN)
        expert_group.shift(DOWN*0.5)

        self.play(Create(expert_group))
        self.wait(2)

        # ================

        text_worst_case = Text("New Scenario").scale(1).shift(UP*3 + RIGHT*3.5)
        self.play(Create(text_worst_case), run_time = 1)
        self.wait(1)

        text_round_1_r = Text("No Guarantee of an Always Correct Expert").scale(0.5).next_to(text_worst_case, DOWN)
        self.play(Create(text_round_1_r), run_time = 1)
        self.wait(2)
        expert_group_r = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.2)
              for j in range(16)]
        ).arrange_in_grid(4, 4, buff=0.16).next_to(text_round_1_r, DOWN)
        expert_group_r.shift(DOWN*0.5)
        self.play(Create(expert_group_r))

        self.wait(2)

        self.play(
            FadeOut(text_best_case),
            FadeOut(text_round_1),
            FadeOut(expert_group),
            FadeOut(line),
            FadeOut(text_worst_case),
            FadeOut(text_round_1_r),
        )

        anim = expert_group_r.animate
        self.play(anim.scale(1.2), anim.shift(LEFT*7 + UP*0.5))
        self.wait(1)

        lighty = light_character.LightCharacter().light_off_character().scale(0.9).shift(DOWN*2.1 +RIGHT*1.5)
        self.play(Create(lighty))
        self.wait(1)

        square = Square()
        square.set_fill(color=WHITE, opacity=1)
        square.move_to(expert_group_r.get_center() + RIGHT*9)
        self.play(FadeIn(square))
        self.wait(1)

        bounding_box = SurroundingRectangle(expert_group_r, buff=0.3)
        self.play(Create(bounding_box))
        self.wait(2)

        coins = []
        for i in range(16):
            new_h_coin = coin.H.copy().scale(0.4).move_to(expert_group_r[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
            coins.append(new_h_coin)
        v_group_coins = VGroup(
            *[coin for coin in coins]
        )
        self.play(FadeIn(v_group_coins))
        self.wait(2)

        h_coin_lighty = coin.H.copy().scale(0.8).move_to(lighty.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(FadeIn(h_coin_lighty))
        self.wait(1)

        t_coin_square = coin.T.copy().scale(1).move_to(square.get_center())
        self.play(square.animate.set_fill(color=WHITE, opacity=0), FadeIn(t_coin_square))
        self.wait(2)

        self.play(FadeOut(v_group_coins), FadeOut(h_coin_lighty))
        crosses = []
        for i in range(16):
            red_cross = Cross(expert_group_r[i])
            red_cross.set_color(RED)
            crosses.append(red_cross)
        v_group_crosses = VGroup(
            *[cross for cross in crosses]
        )
        self.play(Create(v_group_crosses))
        self.wait(1)
        self.play(FadeOut(bounding_box))
        self.wait(2)

        question_mark = Text("?").scale(2).move_to(h_coin_lighty)
        self.play(Create(question_mark))
        self.wait(2)

        expert_group_r_7_copy = expert_group_r[7].copy()
        expert_group_r_7_copy.move_to(expert_group_r[7].get_center())
        self.add(expert_group_r_7_copy)
        self.play(FadeOut(expert_group_r), FadeOut(lighty), FadeOut(square), FadeOut(t_coin_square), FadeOut(question_mark), FadeOut(v_group_crosses))
        self.wait(1)
        self.play(expert_group_r_7_copy.animate.move_to(ORIGIN))
        self.play(expert_group_r_7_copy.animate.scale(3.5))
        self.wait(2)

        overline = Line(expert_group_r_7_copy.get_corner(UL) + UP*0.2, expert_group_r_7_copy.get_corner(UR) + UP*0.2).set_color(DARK_BLUE)
        overline.set_stroke(width=15)
        self.play(Create(overline))
        self.wait(2)

        # move right endpoint to the left, but keep left endpoint fixed
        self.play(
            overline.animate.put_start_and_end_on(
                expert_group_r_7_copy.get_corner(UL) + UP*0.2,
                (expert_group_r_7_copy.get_corner(UL) + UP*0.2 + expert_group_r_7_copy.get_corner(UR) + UP*0.2) / 2
            )
        )
        self.wait(0.5)
        self.play(
            overline.animate.put_start_and_end_on(
                expert_group_r_7_copy.get_corner(UL) + UP*0.2,
                (expert_group_r_7_copy.get_corner(UL) + UP*0.2 + expert_group_r_7_copy.get_corner(UR) + UP*0.2) / 2 + LEFT*0.5
            )
        )
        self.wait(0.5)

        self.play(
            overline.animate.put_start_and_end_on(
                expert_group_r_7_copy.get_corner(UL) + UP*0.2,
                expert_group_r_7_copy.get_corner(UR) + UP*0.2
            )
        )
        self.wait(1)

        grouper = VGroup(expert_group_r_7_copy, overline)
        anim_grouper = grouper.animate
        self.play(anim_grouper.shift(LEFT*5), anim_grouper.scale(0.65))
        self.wait(1)

        phi_eq_1 = MathTex(r"\phi = 1").scale(0.85).next_to(overline, UP)
        loc = phi_eq_1.get_center()
        self.play(Create(phi_eq_1))
        self.wait(1)

        square_v2 = Square()
        square_v2.set_fill(color=WHITE, opacity=1)
        square_v2.shift(RIGHT*5)
        self.play(FadeIn(square_v2))
        self.wait(1)

        h_coin_lighty = coin.H.copy().scale(0.7).move_to(expert_group_r_7_copy.get_center() + RIGHT*1.2 + UP*1)
        self.play(FadeIn(h_coin_lighty))
        self.wait(1)

        h_coin_again = coin.H.copy().scale(0.8).move_to(square_v2.get_center())
        self.play(square_v2.animate.set_fill(color=WHITE, opacity=0), FadeIn(h_coin_again))
        self.wait(1)

        lighty_group = VGroup(
            expert_group_r_7_copy, overline, phi_eq_1, h_coin_lighty
        )
        lighty_group_copy = lighty_group.copy()
        lighty_group_copy_animation = lighty_group_copy.animate
        self.play(lighty_group_copy_animation.move_to(ORIGIN + UP*2), lighty_group_copy_animation.scale(0.6))
        arrow = Arrow(lighty_group.get_corner(UR) + DOWN*1.9, lighty_group_copy.get_corner(DL) + UP, buff=0.2)
        self.play(Create(arrow))
        self.wait(2)

        t_coin_lighty = coin.T.copy().scale(0.7).move_to(expert_group_r_7_copy.get_center() + RIGHT*1.2 + UP*1)
        self.play(Transform(h_coin_lighty, t_coin_lighty))
        self.wait(1)

        self.play(
            overline.animate.put_start_and_end_on(
                expert_group_r_7_copy.get_corner(UL) + UP*0.2,
                (expert_group_r_7_copy.get_corner(UL) + UP*0.2 + expert_group_r_7_copy.get_corner(UR) + UP*0.2) / 2
            )
        )

        phi_eq_half = MathTex(r"\phi = \tfrac12").scale(0.85).move_to(loc)
        self.play(Transform(phi_eq_1, phi_eq_half))
        self.wait(1)

        lighty_group_new = VGroup(
            expert_group_r_7_copy, overline, phi_eq_1, h_coin_lighty
        )
        lighty_group_new_copy = lighty_group_new.copy()
        lighty_group_new_copy_animation = lighty_group_new_copy.animate
        self.play(lighty_group_new_copy_animation.move_to(ORIGIN + DOWN*2), lighty_group_new_copy_animation.scale(0.6))
        arrow = Arrow(lighty_group.get_corner(UR) + DOWN*1.9, lighty_group_new_copy.get_corner(UL) + DOWN, buff=0.2)
        self.play(Create(arrow))
        self.wait(2)






        
