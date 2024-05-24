from manim import *
import coin
import light_character
import experts
import random

class scene8(Scene):
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

        self.play(FadeIn(expert_group))
        self.wait(1)

        surrounding_box = SurroundingRectangle(expert_group, buff=0.3)
        self.play(Create(surrounding_box))
        self.wait(2)

        # FLIP COIN
        h_coin = coin.T.copy().scale(1).shift(RIGHT*4 + DOWN*2.3)
        square = Square()
        square.set_fill(color=WHITE, opacity=1)
        square.move_to(h_coin.get_center())
        self.play(FadeIn(square))
        self.wait(1)

        oof = [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1]
        coins = []
        for i in range(27):
            if oof[i] == 0:
                new_h_coin = coin.H.copy().scale(0.4).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                # self.play(FadeIn(new_h_coin), run_time=0.1)
            else:
                new_h_coin = coin.T.copy().scale(0.4).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
                # self.play(FadeIn(new_h_coin), run_time=0.1)
            coins.append(new_h_coin)

        coins_vgroup = VGroup(*coins)
        self.play(FadeIn(coins_vgroup))
        self.wait(2)

        t0 = Table(
            [["HEADS", "TAILS"],
            ["8", "19"]])
        
        t0.scale(0.7)
        t0.shift(DOWN*2.5)
        self.play(Create(t0))
        self.wait(1)

        ent = t0.get_entries_without_labels()

        #change color of t0[0][0] to red
        self.play(ent[0].animate.set_color(RED),
                  ent[1].animate.set_color(GREEN),
                    ent[2].animate.set_color(RED),
                    ent[3].animate.set_color(GREEN))
        self.wait(1)

        coin_t_self = coin.T.copy().scale(0.6).move_to(light_off.get_center() + UP*1 + RIGHT*1.1)
        self.play(FadeIn(coin_t_self))
        self.wait(1)

        self.play(
            square.animate.set_fill(color=WHITE, opacity=0),
            FadeIn(h_coin)
        )
        self.wait(2)
        text_one_dollar = MathTex(r"\$1").move_to(coin_t_self.get_center() + DOWN*1.4)
        self.play(FadeIn(text_one_dollar))
        in_group_experts = []
        in_group_coins = []
        for i in range(27):
            if oof[i] == 0:
                self.play(FadeOut(coins[i]), FadeOut(expert_group[i]), run_time=0.25)
                self.remove(coins[i])
                self.remove(expert_group[i])
            else:
                in_group_experts.append(expert_group[i])
                in_group_coins.append(coins[i])

        self.wait(2)

        in_group_experts_vgroup = VGroup(*in_group_experts)
        in_group_coins_vgroup = VGroup(*in_group_coins)

        massive_group = VGroup(
            # expert_group,
            in_group_experts_vgroup,
            in_group_coins_vgroup,
            surrounding_box,
            square,
            # coins_vgroup,
            t0,
            coin_t_self,
            text_one_dollar,
            light_off,
            h_coin
        )
        self.play(
            massive_group.animate.scale(0.4)
        )
        self.play(massive_group.animate.shift(LEFT*3.5))
        self.wait(2)

        line = Line(start=UP*3, end=DOWN*3)
        self.play(Create(line))

        text_majority_correct = Text("Majority is Correct").scale(0.7).shift(UP*3 + LEFT*3.5)
        self.play(Write(text_majority_correct), run_time=0.5)
        self.wait(1)

        text_majority_is_incorrect = Text("Majority is Incorrect").scale(0.7).shift(UP*3 + RIGHT*3.5)
        self.play(Write(text_majority_is_incorrect), run_time = 0.5)
        self.wait(1)

        rectangle = Rectangle(height=3, width=6).shift(RIGHT*3.5)
        rectangle.set_fill(color=BLACK, opacity=1)
        self.play(Create(rectangle))
        self.wait(2)

        animation = rectangle.animate
        self.play(animation.move_to(ORIGIN), animation.scale(4))
        self.wait(2)