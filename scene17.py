

from manim import *
import coin 
import light_character
import experts
import random 

class scene17(Scene):
    def construct(self):

        light_off = light_character.LightCharacter().light_off_character().scale(0.9).shift(DOWN*2.3 + LEFT*4.5)
        self.play(Create(light_off))
        self.wait(1)
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

        my_coin = coin.T.copy().scale(0.8).move_to(light_off.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(FadeIn(my_coin))
        self.wait(1)
        self.play(square.animate.set_fill(color=WHITE, opacity=0))
        self.wait(2)
        self.play(FadeOut(my_coin))
        self.wait(2)

        my_coin = coin.H.copy().scale(0.8).move_to(light_off.get_center() + RIGHT*1.2 + UP*1.2)
        for a in coin.animate_flip(h_coin,final='H', n_flips=3):
            self.play(a,run_time=0.1)
        idk = coin.animate_flip(h_coin, final='H', n_flips=3)
        counter = 0
        for a in idk:
            self.play(a,run_time=0.1)
            counter += 1
            square.set_fill(color=WHITE, opacity=counter * 1/(len(idk)))
        self.wait(2)

        self.play(FadeIn(my_coin))
        self.wait(1)
        # h_coin = coin.H.copy().scale(1).shift(RIGHT*3 + DOWN*2.3)
        self.play(FadeIn(h_coin), square.animate.set_fill(color=WHITE, opacity=0))
        self.wait(1)
        self.play(FadeOut(my_coin), FadeOut(h_coin), square.animate.set_fill(color=WHITE, opacity=1))
        self.wait(2)

        chuck = ImageMobject("images/chuck.png").scale(1).shift(UP*1.5)
        chuck_pred = ImageMobject("images/mavs.png").scale(0.2).next_to(chuck, RIGHT)
        chuck_pred.shift(UP)
        my_pred = ImageMobject("images/mavs.png").scale(0.2).move_to(light_off.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(FadeIn(chuck), FadeIn(chuck_pred), FadeIn(my_pred))

        self.wait(2)

        mavs_answer = ImageMobject("images/mavs.png").scale(0.35).move_to(square.get_center())
        self.play(FadeIn(mavs_answer), square.animate.set_fill(color=WHITE, opacity=0))
        self.wait(2)


        expert_group = VGroup(
            *[experts.experts().get_trusted_expert(random.randint(1,4)).scale(0.22)
              for _ in range(27)]
        ).arrange_in_grid(3, 9, buff=0.35).shift(UP*1.7)
        self.play(FadeOut(chuck), FadeOut(chuck_pred), FadeOut(mavs_answer), FadeOut(my_pred), square.animate.set_fill(color=WHITE, opacity=1),
                  FadeIn(expert_group))
        self.wait(2)

        choices = ['H', 'T', 'H', 'T', 'T', 'T', 'H', 'H', 'T', 'T', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'H',
                   'H', 'T', 'T', 'H', 'H', 'H', 'T', 'H', 'H']
        # choices = []
        coins = []
        for i in range(27):
            # h_or_t = random.choice(['H','T'])
            # choices.append(h_or_t)
            h_or_t = choices[i]
            if h_or_t == 'H':
                new_h_coin = coin.H.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            else:
                new_h_coin = coin.T.copy().scale(0.3).move_to(expert_group[i].get_corner(UR) - UP*0.14 + RIGHT*0.04)
            coins.append(new_h_coin)
            self.play(FadeIn(new_h_coin), run_time=0.1)

        h_coin = coin.H.copy().scale(1).shift(RIGHT*3 + DOWN*2.3)
        my_pred_coin = coin.H.copy().scale(0.8).move_to(light_off.get_center() + RIGHT*1.2 + UP*1.2)
        self.wait(1)
        self.play(FadeIn(my_pred_coin))
        self.wait(1)
        self.play(square.animate.set_fill(color=WHITE, opacity=0), FadeIn(h_coin))
        self.wait(2)
        for i in range(27):
            if choices[i] == 'T':
                self.play(
                    expert_group[i][1].animate.put_start_and_end_on(
                        expert_group[i][1].get_edge_center(UL),
                        (expert_group[i][1].get_edge_center(UL) + expert_group[i][1].get_edge_center(UR)) / 2
                    ), run_time=0.2
                )
        self.wait(1)
        vgroup_coins = VGroup(*coins)
        self.play(FadeOut(vgroup_coins), FadeOut(my_pred_coin))
        self.bring_to_front(square)

        for a in coin.animate_flip(h_coin,final='H', n_flips=3):
            self.play(a,run_time=0.1)
        idk = coin.animate_flip(h_coin, final='T', n_flips=3)
        counter = 0
        for a in idk:
            self.play(a,run_time=0.1)
            counter += 1
            square.set_fill(color=WHITE, opacity=counter * 1/(len(idk)))
        self.wait(2)


        choices = ['T', 'H', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'T', 'T', 'T', 'H', 'H', 'T', 'H',
                     'H', 'T', 'T', 'T', 'H', 'T', 'T', 'H', 'T']
        # choices = []
        coins = []
        for i in range(27):
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
        my_coin_pred = coin.T.copy().scale(0.8).move_to(light_off.get_center() + RIGHT*1.2 + UP*1.2)
        self.play(FadeIn(my_coin_pred))
        self.wait(1)
        self.play(square.animate.set_fill(color=WHITE, opacity=0), FadeIn(h_coin))
        self.wait(2)

