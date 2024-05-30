from manim import *
import coin
import light_character
import experts
import random

class scene13(Scene):
    def construct(self):
        light_off = light_character.LightCharacter().light_off_character().scale(0.7).shift(DOWN*2.3 + LEFT*5)
        self.play(Create(light_off))
        loc_lighty = light_off.get_center()
        self.wait(1)

        # squares = VGroup(
        #     *[VGroup(Square(color=Color(hue = j/16, saturation=1, luminance=0.5),
        #              fill_opacity=0.5).scale(0.65),
        #              Text("Person " + str(j+1)+ "\nAge: " + str(ages[j])).scale(0.4)) for j in range(16)]
        # ).arrange_in_grid(4, 4, buff=0.1)


        # generate a random number between 1 and 4 inclusive
        # expert_num = random.randint(1,4)
        expert_group = VGroup(
            *[experts.experts().get_trusted_expert(random.randint(1,4)).scale(0.22)
              for _ in range(9)]
        ).arrange_in_grid(1, 9, buff=0.35).shift(UP*2.5)
        self.play(Create(expert_group))

        loc_exp = expert_group[0].get_center()

        surrounding_box = SurroundingRectangle(expert_group, buff=0.3)
        self.wait(0.3)
        self.play(Create(surrounding_box))
        self.wait(2)

        # FLIP COIN
        h_coin = coin.H.copy().scale(1).shift(RIGHT*4.9 + DOWN*2.3)
        square = Square()
        square.set_fill(color=WHITE, opacity=0)
        square.move_to(h_coin.get_center())
        self.play(FadeIn(h_coin), FadeIn(square))
        self.wait(1)
        #flip coin with animated box
        for a in coin.animate_flip(h_coin,final='H', n_flips=5):
            self.play(a,run_time=0.1)
        idk = coin.animate_flip(h_coin, final='T', n_flips=3)
        counter = 0
        for a in idk:
            self.play(a,run_time=0.1)
            counter += 1
            square.set_fill(color=WHITE, opacity=counter * 1/(len(idk)))
        self.play(FadeOut(h_coin), run_time=0.1)
        self.wait(2)




        choices = ['H', 'T', 'H', 'T', 'T', 'T', 'H', 'H', 'T']
        # choices = []
        coins = []
        for i in range(9):
            # h_or_t = random.choice(['H','T'])
            # choices.append(h_or_t)
            h_or_t = choices[i]
            if h_or_t == 'H':
                new_h_coin = coin.H.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            else:
                new_h_coin = coin.T.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            coins.append(new_h_coin)
            self.play(FadeIn(new_h_coin), run_time=0.1)

        self.wait(2)
        h_coin_copy = coin.H.copy().scale(0.6)
        t_coin_copy = coin.T.copy().scale(0.6)

        loc_of_h = loc_exp + DOWN*1.5
        loc_of_t = loc_of_h + DOWN*1.2

        h_coin_copy.move_to(loc_of_h)
        t_coin_copy.move_to(loc_of_t)

        self.play(FadeIn(h_coin_copy), FadeIn(t_coin_copy))

        loc_of_h += RIGHT
        loc_of_t += RIGHT

        fixed_h_loc = loc_of_h
        fixed_t_loc = loc_of_t

        to_remove = []

        for i in range(9):
            obj = expert_group[i][1].copy()
            if choices[i] == 'H':
                # move overline to loc_of_h
                # self.play(expert_group[i][1].get_edge_center(UL).animate.move_to(loc_of_h))
                # self.play(expert_group[i][1].animate.align_to(loc_of_h, LEFT))
                # obj = expert_group[i][1].copy()
                crit_anim = obj.animate
                self.play(crit_anim.next_to(loc_of_h, RIGHT, buff=0))
                loc_of_h = obj.get_edge_center(UR)
            else:
                # self.play(expert_group[i][1].get_edge_center(UL).animate.move_to(loc_of_t))
                # self.play(expert_group[i][1].animate.align_to(loc_of_t, LEFT))
                # obj = expert_group[i][1].copy()
                crit_anim = obj.animate
                self.play(crit_anim.next_to(loc_of_t, RIGHT, buff=0))
                loc_of_t = obj.get_edge_center(UR)
            # to_remove.append(expert_group[i][1])
            to_remove.append(obj)

        self.wait(2)
        vgroup_to_remove = VGroup(*to_remove)



        dim_character = light_character.LightCharacter().dim_on_character().scale(0.7).shift(DOWN*2.3 + LEFT*5)
        self.play(FadeOut(light_off), FadeIn(dim_character))

        my_coin = coin.T.copy().scale(0.6).move_to(dim_character.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(FadeIn(my_coin))
        self.wait(1)

        answer_coin = coin.T.copy().scale(0.8).move_to(square.get_center())
        self.play(square.animate.set_fill(color=WHITE, opacity=0.0), FadeIn(answer_coin))

        self.play(
            FadeOut(vgroup_to_remove)
        )


        for i in range(9):
            if choices[i] == 'H':
                self.play(
                    expert_group[i][1].animate.put_start_and_end_on(
                        expert_group[i][1].get_edge_center(UL),
                        (expert_group[i][1].get_edge_center(UL) + expert_group[i][1].get_edge_center(UR)) / 2
                    )
                )

        # new_ovs = []
        # for i in range(9):
        #     if choices[i] == 'H':
        #         overline = Line(expert_group[i].get_corner(UL) + UP*0.2, (expert_group[i].get_corner(UL) + UP*0.2 + expert_group[i].get_corner(UR) + UP*0.2) / 2 + LEFT*0.8).set_color(DARK_BLUE)
        #         overline.set_stroke(width=15)
        #         new_ovs.append(overline)
        #     else:
        #         overline = Line(expert_group[i].get_corner(UL) + UP*0.2 + RIGHT*0.2, expert_group[i].get_corner(UR) + UP*0.2 + LEFT*0.2).set_color(DARK_BLUE)
        #         overline.set_stroke(width=15)
        #         new_ovs.append(overline)
        # new_ov_group = VGroup(*new_ovs)
        # self.play(FadeIn(new_ov_group))
        self.wait(2)

        vgroup_coins = VGroup(*coins)

        self.play(FadeOut(my_coin), FadeOut(vgroup_coins), square.animate.set_fill(color=WHITE, opacity=1), FadeOut(answer_coin),
                  FadeOut(dim_character), FadeIn(light_off))


        choices = ['T', 'T', 'H', 'H', 'T', 'H', 'T', 'T', 'T']
        coins = []
        # choices = []
        for i in range(9):
            # h_or_t = random.choice(['H','T'])
            # choices.append(h_or_t)
            h_or_t = choices[i]
            if h_or_t == 'H':
                new_h_coin = coin.H.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            else:
                new_h_coin = coin.T.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            coins.append(new_h_coin)
            self.play(FadeIn(new_h_coin), run_time=0.1)


        self.wait(2)

        to_remove = []

        loc_of_h = fixed_h_loc
        loc_of_t = fixed_t_loc


        for i in range(9):
            obj = expert_group[i][1].copy()
            if choices[i] == 'H':
                # move overline to loc_of_h
                # self.play(expert_group[i][1].get_edge_center(UL).animate.move_to(loc_of_h))
                # self.play(expert_group[i][1].animate.align_to(loc_of_h, LEFT))
                # obj = expert_group[i][1].copy()
                crit_anim = obj.animate
                self.play(crit_anim.next_to(loc_of_h, RIGHT, buff=0))
                loc_of_h = obj.get_edge_center(UR)
                # coins.append(obj)
            else:
                # self.play(expert_group[i][1].get_edge_center(UL).animate.move_to(loc_of_t))
                # self.play(expert_group[i][1].animate.align_to(loc_of_t, LEFT))
                # obj = expert_group[i][1].copy()
                crit_anim = obj.animate
                self.play(crit_anim.next_to(loc_of_t, RIGHT, buff=0))
                loc_of_t = obj.get_edge_center(UR)
                # coins.append(obj)
            # to_remove.append(expert_group[i][1])
            to_remove.append(obj)

        self.wait(2)
        vgroup_to_remove = VGroup(*to_remove)

        self.play(FadeOut(light_off), FadeIn(dim_character))

        my_coin = coin.T.copy().scale(0.6).move_to(dim_character.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(FadeIn(my_coin))
        self.wait(1)

        answer_coin = coin.T.copy().scale(0.8).move_to(square.get_center())
        self.play(square.animate.set_fill(color=WHITE, opacity=0.0), FadeIn(answer_coin))

        self.play(
            FadeOut(vgroup_to_remove)
        )


        for i in range(9):
            if i == 2:
                self.play(
                    expert_group[i][1].animate.put_start_and_end_on(
                        expert_group[i][1].get_edge_center(UL),
                        (expert_group[i][1].get_edge_center(UL) + expert_group[i][1].get_edge_center(UR)) / 2 + LEFT*0.08
                    )
                )
            elif choices[i] == 'H':
                self.play(
                    expert_group[i][1].animate.put_start_and_end_on(
                        expert_group[i][1].get_edge_center(UL),
                        (expert_group[i][1].get_edge_center(UL) + expert_group[i][1].get_edge_center(UR)) / 2
                    )
                )
        self.wait(2)

        vgroup_coins = VGroup(*coins)
        self.play(FadeOut(my_coin), FadeOut(vgroup_coins), square.animate.set_fill(color=WHITE, opacity=1), FadeOut(answer_coin),
                  FadeOut(dim_character), FadeIn(light_off))
        

        choices = ['T', 'H', 'T', 'T', 'H', 'H', 'T', 'T', 'H']
        # choices = []
        for i in range(9):
            # h_or_t = random.choice(['H','T'])
            # choices.append(h_or_t)
            h_or_t = choices[i]
            if h_or_t == 'H':
                new_h_coin = coin.H.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            else:
                new_h_coin = coin.T.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            self.play(FadeIn(new_h_coin), run_time=0.1)


        self.wait(2)

        to_remove = []

        loc_of_h = fixed_h_loc
        loc_of_t = fixed_t_loc

        vgroup_heads = VGroup()
        vgroup_tails = VGroup()
        for i in range(9):
            obj = expert_group[i][1].copy()
            if choices[i] == 'H':
                # move overline to loc_of_h
                # self.play(expert_group[i][1].get_edge_center(UL).animate.move_to(loc_of_h))
                # self.play(expert_group[i][1].animate.align_to(loc_of_h, LEFT))
                # obj = expert_group[i][1].copy()
                crit_anim = obj.animate
                self.play(crit_anim.next_to(loc_of_h, RIGHT, buff=0))
                loc_of_h = obj.get_edge_center(UR)
                vgroup_heads.add(obj)
            else:
                # self.play(expert_group[i][1].get_edge_center(UL).animate.move_to(loc_of_t))
                # self.play(expert_group[i][1].animate.align_to(loc_of_t, LEFT))
                # obj = expert_group[i][1].copy()
                crit_anim = obj.animate
                self.play(crit_anim.next_to(loc_of_t, RIGHT, buff=0))
                loc_of_t = obj.get_edge_center(UR)
                vgroup_tails.add(obj)

            # to_remove.append(expert_group[i][1])
            to_remove.append(obj)

        self.wait(2)
        vgroup_to_remove = VGroup(*to_remove)

        self.play(FadeOut(light_off), FadeIn(dim_character))

        my_coin = coin.H.copy().scale(0.6).move_to(dim_character.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(FadeIn(my_coin))
        self.wait(1)

        answer_coin = coin.T.copy().scale(0.8).move_to(square.get_center())
        self.play(square.animate.set_fill(color=WHITE, opacity=0.0), FadeIn(answer_coin))

        self.wait(2)


        self.play(FadeOut(dim_character), FadeOut(my_coin))

        # self.play(
        #     FadeOut(vgroup_to_remove)
        # )
        # for i in range(9):
        #     if i == 5:
        #         self.play(
        #             expert_group[i][1].animate.put_start_and_end_on(
        #                 expert_group[i][1].get_edge_center(UL),
        #                 (expert_group[i][1].get_edge_center(UL) + expert_group[i][1].get_edge_center(UR)) / 2 + LEFT*0.08
        #             )
        #         )
        #     elif choices[i] == 'H':
        #         self.play(
        #             expert_group[i][1].animate.put_start_and_end_on(
        #                 expert_group[i][1].get_edge_center(UL),
        #                 (expert_group[i][1].get_edge_center(UL) + expert_group[i][1].get_edge_center(UR)) / 2
        #             )
        #         )
        self.wait(2)

        self.play(vgroup_heads.animate.set_color(BLUE), vgroup_tails.animate.set_color(YELLOW))
        self.wait(1)
        # self.play(vgroup_tails.animate.next_to(loc_of_h, RIGHT, buff=0), FadeOut(h_coin_copy), FadeOut(t_coin_copy))
        vgroup_heads_copy = vgroup_heads.copy()
        vgroup_tails_copy = vgroup_tails.copy()

        self.play(vgroup_heads_copy.animate.next_to(fixed_h_loc + DOWN*2.4, RIGHT, buff=0))
        self.play(vgroup_tails_copy.animate.next_to(vgroup_heads_copy.get_edge_center(UR), RIGHT, buff=0))
        self.wait(2)

        big_mobject = VGroup(vgroup_heads_copy, vgroup_tails_copy)
        brace = Brace(big_mobject, DOWN)
        text = MathTex(r"\phi^T = \sum_i \phi_i^T").scale(0.8).next_to(brace, DOWN)
        self.play(Create(brace), Create(text))
        self.wait(2)

        text_geq_phi_over_2 = MathTex(r"\geq \tfrac12 \cdot \phi^T").scale(0.8).next_to(vgroup_heads, RIGHT)
        text_leq_phi_over_2 = MathTex(r"\leq \tfrac12 \cdot \phi^T").scale(0.8).next_to(vgroup_tails, RIGHT)

        self.play(Create(text_geq_phi_over_2), Create(text_leq_phi_over_2))

        self.wait(2)

        math_implies = MathTex(r"\implies").scale(0.8).next_to(text_geq_phi_over_2, RIGHT)
        # special_line = vgroup_heads.copy()
        # special_line.put_start_and_end_on(
        #     vgroup_heads.get_edge_center(UL), (vgroup_heads.get_edge_center(UL) + vgroup_heads.get_edge_center(UR))/2
        # )
        special_line = Line(
            vgroup_heads.get_edge_center(UL), (vgroup_heads.get_edge_center(UL) + vgroup_heads.get_edge_center(UR))/2
        ).set_color(BLUE)
        special_line.set_stroke(width=15)
        # special_line_2 = vgroup_heads.copy()
        # special_line_2.put_start_and_end_on(
        #     (vgroup_tails.get_edge_center(UL) + vgroup_tails.get_edge_center(UR))/2, vgroup_tails.get_edge_center(UR)
        # )
        special_line_2 = Line(
            (vgroup_heads.get_edge_center(UL) + vgroup_heads.get_edge_center(UR))/2, vgroup_heads.get_edge_center(UR)
        ).set_color(BLUE)
        special_line_2.set_stroke(width=15)
        special_line_group = VGroup(special_line, special_line_2)
        self.play(Create(math_implies), special_line_group.animate.next_to(math_implies, RIGHT))
        self.wait(1)

        b1 = Brace(special_line, DOWN)
        b2 = Brace(special_line_2, DOWN)
        t1 = MathTex(r"\geq \tfrac14 \cdot \phi^T").scale(0.8).next_to(b1, DOWN)
        t2 = MathTex(r"\geq \tfrac14 \cdot \phi^T").scale(0.8).next_to(b2, DOWN)

        self.play(Create(b1), Create(t1))

        self.wait(2)

        self.play(special_line_2.animate.set_color(RED))
        self.wait(1)
        self.play(Create(b2), Create(t2))

        # self.play(
        #     special_line.animate.put_start_and_end_on(
        #         special_line.get_edge_center(UL),
        #         (special_line.get_edge_center(UL) + special_line.get_edge_center(UR)) / 2
        #     )
        # )
        self.wait(1)

        # text_geq_phi_over_4 = MathTex(r"\geq \tfrac14 \cdot \phi^T").scale(0.8).next_to(special_line, RIGHT)
        # self.play(Create(text_geq_phi_over_4))
        # self.wait(1)

        # text_another_one = MathTex(r"\leq \tfrac12 \cdot \phi^T").scale(0.8).next_to(text_geq_phi_over_4, DOWN)
        # self.play(Create(text_another_one))
        # self.wait(1)

        text_phi_t = MathTex(r"\phi^T").scale(0.8).next_to(big_mobject, LEFT)
        self.play(Transform(text, text_phi_t), FadeOut(brace))

        self.wait(1)

        text_phi_tone = MathTex(r"\phi^{T+1}").scale(0.8).move_to(text_phi_t.get_center() + DOWN*1.2 + LEFT*0.2)
        self.play(FadeIn(text_phi_tone))
        self.wait(0.5)
        special_line_copy = special_line.copy()
        self.play(special_line_copy.animate.next_to(text_phi_tone, RIGHT))
        self.wait(0.5)
        vgroup_tails_copy_again = vgroup_tails.copy()
        self.play(vgroup_tails_copy_again.animate.next_to(special_line_copy, RIGHT, buff=0))
        self.wait(2)

        # brace_2 = Brace(special_line_copy, DOWN)
        # text_2 = MathTex(r"\geq \tfrac14 \cdot \phi^{T}").scale(0.8).next_to(brace_2, DOWN)

        # brace_3 = Brace(vgroup_tails_copy_again, DOWN)
        # text_3 = MathTex(r"\leq \tfrac12 \cdot \phi^{T}").scale(0.8).next_to(brace_3, DOWN)

        # self.play(Create(brace_2), Create(text_2), Create(brace_3), Create(text_3))

        # self.wait(2)

        good_group = VGroup(special_line_copy, vgroup_tails_copy_again)
        good_group_brace = Brace(good_group, DOWN).set_color(GREEN)
        good_group_text = MathTex(r"\phi^{T+1}").scale(0.8).next_to(good_group_brace, DOWN)
        good_group_text.shift(UP*0.2)

        self.play(Create(good_group_brace), Create(good_group_text))
        self.wait(2)

        special_line_2_copy = special_line_2.copy()
        brace_2_copy = b2.copy()
        text_2_copy = t2.copy()
        # bad_group = VGroup(special_line_2_copy, brace_2_copy, text_2_copy)
        self.play(special_line_2_copy.animate.next_to(good_group, RIGHT, buff=0))
        brace_stuff = VGroup(brace_2_copy, text_2_copy)

        self.play(brace_stuff.animate.next_to(special_line_2_copy, DOWN))
        self.wait(2)

        larger_group = VGroup(good_group, special_line_2_copy)
        larger_group_brace = Brace(larger_group, UP).set_color(WHITE)
        larger_group_text = MathTex(r"\phi^{T}").scale(0.8).next_to(larger_group_brace, UP)
        larger_group_text.shift(DOWN*0.2)

        self.play(Create(larger_group_brace), Create(larger_group_text))
        self.wait(2)

        phi_34 = MathTex(r"\geq \tfrac34 \cdot \phi^T").scale(0.8).move_to(good_group_text.get_center())
        self.play(Transform(good_group_text, phi_34))
        self.wait(2)








        