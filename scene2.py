from manim import *
import coin
import light_character
import experts
import random

class scene2(Scene):
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
        expert_group = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.23)
              for _ in range(27)]
        ).arrange_in_grid(3, 9, buff=0.3).shift(UP*1.5)
        self.play(Create(expert_group))

        surrounding_box = SurroundingRectangle(expert_group, buff=0.3)
        self.wait(0.3)
        self.play(Create(surrounding_box))
        self.wait(2)

        # FLIP COIN
        h_coin = coin.H.copy().scale(1).shift(RIGHT*3 + DOWN*2.3)
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
        self.wait(2)

        for i in range(27):
            h_or_t = random.choice(['H','T'])
            if h_or_t == 'H':
                new_h_coin = coin.H.copy().scale(0.4).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
            else:
                new_h_coin = coin.T.copy().scale(0.4).move_to(expert_group[i].get_corner(UR) + UP*0.04 + RIGHT*0.04)
            self.play(FadeIn(new_h_coin), run_time=0.1)

        self.wait(2)

        dim_character = light_character.LightCharacter().dim_on_character().scale(0.9).shift(DOWN*2.3 + LEFT*4.5)
        self.play(FadeOut(light_off), FadeIn(dim_character))

        my_coin = coin.T.copy().scale(0.8).move_to(dim_character.get_center() + RIGHT*2.5)
        self.play(FadeIn(my_coin))
        self.wait(2)



        