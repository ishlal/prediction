from manim import *

import light_character
import coin
import experts
import random

class scene11(Scene):
    def construct(self):
        light_off = light_character.LightCharacter().light_off_character().scale(0.9).shift(DOWN*2.3 + LEFT*4.5)
        self.play(Create(light_off))
        self.wait(1)

        # squares = VGroup(
        #     *[VGroup(Square(color=Color(hue = j/16, saturation=1, luminance=0.5),
        #              fill_opacity=0.5).scale(0.65),
        #              Text("Person " + str(j+1)+ "\nAge: " + str(ages[j])).scale(0.4)) for j in range(16)]
        # ).arrange_in_grid(4, 4, buff=0.1)


        # generate a random number between 1 and 4 inclusive
        # expert_num = random.randint(1,4)

        designated_expert = experts.experts().designated_expert().scale(0.23)
        expert_group = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.23) if j!= 13 else
              designated_expert
              for j in range(27)]
        ).arrange_in_grid(3, 9, buff=0.3).shift(UP*1.5)

        loc = expert_group[13].get_center()

        # designated_expert = experts.experts().designated_expert().scale(0.23)
        # expert_group[13] = designated_expert

        self.play(Create(expert_group))



        surrounding_box = SurroundingRectangle(expert_group, buff=0.3)
        self.wait(0.3)
        self.play(Create(surrounding_box))

        # FLIP COIN
        h_coin = coin.H.copy().scale(1).shift(RIGHT*3 + DOWN*2.3)
        square = Square()
        square.set_fill(color=WHITE, opacity=0)
        square.move_to(h_coin.get_center())
        self.play(FadeIn(h_coin), FadeIn(square))
        self.wait(0.5)



        #flip coin with animated box
        for a in coin.animate_flip(h_coin,final='H', n_flips=2):
            self.play(a,run_time=0.1)
        idk = coin.animate_flip(h_coin, final='T', n_flips=2)
        counter = 0
        for a in idk:
            self.play(a,run_time=0.1)
            counter += 1
            square.set_fill(color=WHITE, opacity=counter * 1/(len(idk)))
        self.wait(1)


        oof = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1]
        coins = []
        for i in range(27):
            if oof[i] == 0:
                new_h_coin = coin.H.copy().scale(0.4).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                # self.play(FadeIn(new_h_coin), run_time=0.1)
            else:
                new_h_coin = coin.T.copy().scale(0.4).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                # self.play(FadeIn(new_h_coin), run_time=0.1)
            coins.append(new_h_coin)
        v_group_coins = VGroup(
            *[coin for coin in coins]
        )
        self.play(FadeIn(v_group_coins))
        self.wait(0.5)

        self.play(square.animate.set_fill(color=WHITE, opacity=0))


        self.play(
            expert_group[4].animate.move_to(expert_group[8].get_center()),
            coins[4].animate.move_to(coins[8].get_center()),
            expert_group[8].animate.move_to(expert_group[4].get_center()),
            coins[8].animate.move_to(coins[4].get_center())
        )
        self.wait(0.1)

        self.play(
            expert_group[9].animate.move_to(expert_group[16].get_center()),
            coins[9].animate.move_to(coins[16].get_center()),
            expert_group[16].animate.move_to(expert_group[9].get_center()),
            coins[16].animate.move_to(coins[9].get_center())
        )
        self.wait(0.1)

        self.play(
            expert_group[18].animate.move_to(expert_group[23].get_center()),
            coins[18].animate.move_to(coins[23].get_center()),
            expert_group[23].animate.move_to(expert_group[18].get_center()),
            coins[23].animate.move_to(coins[18].get_center())
        )
        self.wait(0.1)

        self.play(
            expert_group[21].animate.move_to(expert_group[26].get_center()),
            coins[21].animate.move_to(coins[26].get_center()),
            expert_group[26].animate.move_to(expert_group[21].get_center()),
            coins[26].animate.move_to(coins[21].get_center())
        )
        self.wait(0.5)

        expert_group_round_2 = VGroup(
            expert_group[0], expert_group[1], expert_group[2], expert_group[3], expert_group[8],
            expert_group[10], expert_group[11], expert_group[12], expert_group[13], expert_group[16],
            expert_group[26], expert_group[19], expert_group[20], expert_group[23], expert_group[22],
        )

        new_bounding_box = SurroundingRectangle(expert_group_round_2, buff=0.3)
        self.play(ReplacementTransform(surrounding_box, new_bounding_box))
        in_group = [0, 1, 2, 3, 8, 10, 11, 12, 13, 16, 26, 19, 20, 23, 22]
        out_group = [4, 5, 6, 7, 9, 14, 15, 17, 18, 21, 24, 25]
        out_vgroup = VGroup(
            *[expert_group[i] for i in out_group]
        )
        # coin_out_vgroup = VGroup(
        #     *[coins[i] for i in out_group]
        # )

        # turn coins into a vgroup
        coins_vgroup = VGroup(
            *[coin for coin in coins]
        )
        self.play(FadeOut(out_vgroup), FadeOut(coins_vgroup), FadeOut(h_coin))
        self.wait(1)

        oof_v2 = [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0]
        # coins = []
        counter = 0
        new_coins = []
        self.play(square.animate.set_fill(color=WHITE, opacity=1))
        for i in range(27):
            if i in in_group:
                coin_to_get = oof_v2[counter]
                counter += 1
                if coin_to_get == 0:
                    new_h_coin = Arrow(expert_group[i].get_corner(UR) +RIGHT*0.04, expert_group[i].get_corner(UR) + UP*0.14 + RIGHT*0.04).set_color(GREEN)
                    #increase stroke of arrow
                    new_h_coin.set_stroke(width=10)
                else:
                    new_h_coin = Arrow(expert_group[i].get_corner(UR) +RIGHT*0.04 + UP*0.14, expert_group[i].get_corner(UR) + RIGHT*0.04).set_color(RED)
                    #increase stroke of arrow
                    new_h_coin.set_stroke(width=10)
                new_coins.append(new_h_coin)

        # make a group out of new_coins
        new_coins_group = VGroup(
            *[coin for coin in new_coins]
        )
        self.play(FadeIn(new_coins_group))
        self.wait(2)

        arrow_ans = Arrow(square.get_center() + DOWN*0.9, square.get_center() + UP*0.8).set_color(GREEN)
        arrow_ans.set_stroke(width=20)

        self.play(square.animate.set_fill(color=WHITE, opacity=0), FadeIn(arrow_ans))

        in_group_round_2 = [3, 8, 12, 13, 22, 26]
        out_group_round_2 = [0, 1, 2, 10, 11, 23, 20, 19, 16]
        out_group_round_2_vgroup = VGroup(
            *[expert_group[i] for i in out_group_round_2]
        )
        in_group_round_2_vgroup = VGroup(
            *[expert_group[i] for i in in_group_round_2]
        )

        new_bounding_box_round_2 = SurroundingRectangle(in_group_round_2_vgroup, buff=0.3)
        self.play(ReplacementTransform(new_bounding_box, new_bounding_box_round_2))
        self.wait(1)

        self.play(FadeOut(out_group_round_2_vgroup), FadeOut(new_coins_group), square.animate.set_fill(color=WHITE, opacity=1), FadeOut(arrow_ans))
        self.wait(1)


        oof_v2 = [1, 1, 1, 0, 0, 1]
        in_group_v3 = [3, 8, 12, 13, 22, 26]
        # coins = []
        counter = 0
        new_coins = []
        for i in range(27):
            if i in in_group_v3:
                coin_to_get = oof_v2[counter]
                counter += 1
                if coin_to_get == 0:
                    # new_h_coin = coin.H.copy().scale(0.4).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                    new_h_coin = ImageMobject("images/mavs.png").scale(0.16).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                else:
                    new_h_coin = ImageMobject("images/celtics.png").scale(0.07).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                self.play(FadeIn(new_h_coin), run_time=0.1)
                new_coins.append(new_h_coin)

        # make a group out of new_coins
        new_coins_group = Group(
            *[coin for coin in new_coins]
        )
        # self.play(FadeIn(new_coins_group))
        self.wait(1)


        team_ans = ImageMobject("images/mavs.png").scale(0.32).move_to(square.get_center())
        self.play(square.animate.set_fill(color=WHITE, opacity=0), FadeIn(team_ans))

        in_group_round_3 = [13, 22]
        out_group_round_3 = [3, 8, 12, 26]

        out_group_round_3_vgroup = VGroup(
            *[expert_group[i] for i in out_group_round_3]
        )
        in_group_round_3_vgroup = VGroup(
            *[expert_group[i] for i in in_group_round_3]
        )

        new_bounding_box_round_3 = SurroundingRectangle(in_group_round_3_vgroup, buff=0.3)
        self.play(ReplacementTransform(new_bounding_box_round_2, new_bounding_box_round_3))
        self.wait(1)

        self.play(FadeOut(out_group_round_3_vgroup), FadeOut(new_coins_group), FadeOut(team_ans))
        self.wait(1)
        self.play(square.animate.set_fill(color=WHITE, opacity=1))

        # raindrop shape
        new_t_coin = ImageMobject("images/raindrop.png").scale(0.08).move_to(expert_group[22].get_corner(UR) + UP*0.04 + RIGHT*0.04)
        new_h_coin = ImageMobject("images/sun.png").scale(0.25).move_to(expert_group[13].get_corner(UR) + UP*0.04 + RIGHT*0.04)
        answer = ImageMobject("images/sun.png").scale(0.5).move_to(square.get_center())

        self.play(FadeIn(new_h_coin), FadeIn(new_t_coin))
        self.wait(1)
        self.play(square.animate.set_fill(color=WHITE, opacity=0), FadeIn(answer))

        new_bounding_box_round_4 = SurroundingRectangle(expert_group[13], buff=0.3)
        self.play(ReplacementTransform(new_bounding_box_round_3, new_bounding_box_round_4))
        self.wait(1)
        self.play(FadeOut(new_t_coin), FadeOut(expert_group[22]))
        self.wait(2)

        self.play(FadeOut(light_off), FadeOut(new_bounding_box_round_4), FadeOut(expert_group[13]), FadeOut(square), FadeOut(designated_expert),
                  FadeOut(answer))
        
        self.wait(1)

