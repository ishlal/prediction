from manim import *
import coin
import light_character
import experts
import random

class Scene6(Scene):
    def construct(self):
        
        line = Line(UP*3, DOWN*3)
        self.play(Create(line))

        text_best_case = Text("Best Case").scale(1).shift(UP*3 + LEFT*3.5)
        self.play(Create(text_best_case), run_time = 0.2)
        self.wait(1)

        text_round_1 = Text("Round 1").scale(0.7).next_to(text_best_case, DOWN)
        self.play(Create(text_round_1), run_time = 0.2)

        designated_expert = experts.experts().designated_expert().scale(0.2)
        expert_group = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.2) if j!= 10 else
              designated_expert
              for j in range(16)]
        ).arrange_in_grid(4, 4, buff=0.16).next_to(text_round_1, DOWN)
        expert_group.shift(DOWN*0.5)

        loc = expert_group[11].get_center()
        

        h_coin = coin.T.copy().scale(1).next_to(text_best_case, RIGHT).scale(0.6)
        h_coin.shift(RIGHT*0.3 + DOWN*0.3)
        square = Square().scale(0.6)
        square.set_fill(color=WHITE, opacity=1)
        square.move_to(h_coin.get_center())
        # self.bring_to_back(h_coin)
        self.play(FadeIn(square), Create(expert_group))
        self.bring_to_front(square)
        # self.add(h_coin)
        self.wait(2)


        coins = []
        for i in range(16):
            if i != 10:
                new_h_coin = coin.H.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                self.play(FadeIn(new_h_coin), run_time=0.1)
            else:
                new_h_coin = coin.T.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                self.play(FadeIn(new_h_coin), run_time=0.1)
            coins.append(new_h_coin)

        self.play(square.animate.set_fill(color=WHITE, opacity=0), FadeIn(h_coin))
        self.wait(1)

        surrounding_box = SurroundingRectangle(expert_group[10], buff=0.3)
        self.play(Create(surrounding_box))
        self.wait(1)

        # ================

        text_worst_case = Text("Worst Case").scale(1).shift(UP*3 + RIGHT*3.5)
        self.play(Create(text_worst_case), run_time = 0.2)
        self.wait(1)

        text_round_1_r = Text("Round 1").scale(0.7).next_to(text_worst_case, DOWN)
        self.play(Create(text_round_1_r), run_time = 0.2)
        self.wait(2)

        designated_expert_r = experts.experts().designated_expert().scale(0.2)
        expert_group_r = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.2) if j!= 10 else
              designated_expert_r
              for j in range(16)]
        ).arrange_in_grid(4, 4, buff=0.16).next_to(text_round_1_r, DOWN)
        expert_group_r.shift(DOWN*0.5)

        h_coin_r = coin.T.copy().scale(1).next_to(text_worst_case, RIGHT).scale(0.6)
        h_coin_r.shift(RIGHT*0.3 + DOWN*0.3)
        square_r = Square().scale(0.6)
        square_r.set_fill(color=WHITE, opacity=1)
        square_r.move_to(h_coin_r.get_center())
        # self.bring_to_back(h_coin)
        self.play(FadeIn(square_r), Create(expert_group_r))
        self.bring_to_front(square_r)
        # self.add(h_coin)
        self.wait(2)


        coins = []
        for i in range(16):
            new_h_coin_r = coin.T.copy().scale(0.3).move_to(expert_group_r[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
            self.play(FadeIn(new_h_coin_r), run_time=0.1)
            coins.append(new_h_coin_r)

        self.play(square_r.animate.set_fill(color=WHITE, opacity=0), FadeIn(h_coin_r))
        self.wait(1)

        text_round_2_r = Text("Round 2").scale(0.7).move_to(text_round_1_r.get_center())
        
        # self.play(square.animate.set_fill(color=WHITE, opacity=1), FadeOut(h_coin))
        coins_vgroup = VGroup(*coins)
        self.play(FadeOut(coins_vgroup))
        self.wait(1)
        self.play(Transform(text_round_1_r, text_round_2_r), run_time=0.2)
        self.play(square_r.animate.set_fill(color=WHITE, opacity=1), FadeOut(h_coin_r))
        self.wait(1)


        t_coin_r = coin.T.copy().scale(1).next_to(text_round_1_r, RIGHT).scale(0.6)
        # t_coin_r.shift(RIGHT*0.3 + DOWN*0.3)
        t_coin_r.move_to(square_r.get_center())

        coins = []
        for i in range(16):
            new_t_coin_r = coin.T.copy().scale(0.3).move_to(expert_group_r[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
            # self.play(FadeIn(new_t_coin_r), run_time=0.1)
            coins.append(new_t_coin_r)
        
        coins_vgroup = VGroup(*coins)
        self.play(FadeIn(coins_vgroup))
        self.play(square_r.animate.set_fill(color=WHITE, opacity=0), FadeIn(t_coin_r))
        self.wait(1)

        self.play(FadeOut(coins_vgroup))

        text_round_m_r = Text("Round M").scale(0.7).move_to(text_round_1_r.get_center())
        self.play(Transform(text_round_1_r, text_round_m_r), run_time=0.2)
        self.play(square_r.animate.set_fill(color=WHITE,opacity = 1), FadeOut(t_coin_r))
        self.wait(1)

        h_coin_r = coin.H.copy().scale(1).move_to(square_r.get_center()).scale(0.6)
        # h_coin_r.shift(RIGHT*0.3 + DOWN*0.3)

        coins = []
        for i in range(16):
            new_h_coin_r = coin.H.copy().scale(0.3).move_to(expert_group_r[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
            # self.play(FadeIn(new_h_coin_r), run_time=0.1)
            coins.append(new_h_coin_r)
        coins_vgroup = VGroup(*coins)
        self.play(FadeIn(coins_vgroup))
        self.play(square_r.animate.set_fill(color=WHITE, opacity=0), FadeIn(h_coin_r))
        self.wait(1)




        
