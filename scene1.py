from manim import *
import person
import coin
import light_character

class opening(Scene):
    def construct(self):
        # person1 = person.Person().get_person().scale(0.9).set_color(GREEN).shift(LEFT*4 + DOWN)
        light_off = light_character.LightCharacter().light_off_character().scale(0.9).shift(LEFT*4 + DOWN)
        self.play(Create(light_off))
        self.wait(1)

        h_coin = coin.H.copy().scale(1).shift(RIGHT*3)
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

        light_on = light_character.LightCharacter().light_on_character().scale(0.9).shift(LEFT*4 + DOWN)
        self.play(FadeOut(light_off), FadeIn(light_on))

        # speech bubble
        bubble = SVGMobject("images/bubble.svg")
        bubble.scale(3.5)
        bubble.move_to(light_off.get_center() + UP*2.2 + RIGHT*2.2)

        coin_t = coin.T.copy().scale(0.8).move_to(bubble.get_center()+UP*0.6+LEFT*0.1)
        self.play(FadeIn(bubble), FadeIn(coin_t))
        self.wait(2)
        self.play(square.animate.set_fill(color=WHITE, opacity=0))
        self.wait(2)
        money_won = MathTex(r"\text{Money Won: } \$1")
        money_won.move_to(light_on.get_center() + DOWN*2+RIGHT*0.76)
        self.play(Write(money_won))
        self.wait(2)
        # Group everything together
        group = VGroup(light_on, bubble, coin_t, money_won, square, h_coin)
        self.play(group.animate.scale(0.6))
        self.play(group.animate.shift(LEFT*2))
        self.wait(0.5)

        self.play(group[3].animate.shift(DOWN + RIGHT))
        self.play(group[3].animate.scale(2.5))
        self.wait(2)


        # vertical line
        line = Line(UP*2.5, DOWN*3)
        line.shift(RIGHT*0.1)
        self.play(Create(line))
        self.wait(2)
        # copy of group
        group_copy = group.copy()
        # group_copy.animate.shift(RIGHT*4)
        self.play(group_copy.animate.shift(RIGHT*7))
        coin_h_2 = coin.H.copy().scale(0.48).move_to(group_copy[2])
        # self.play(FadeIn(coin_h_2))
        self.remove(group_copy[2])
        # self.play(FadeOut(group_copy[2]))
        
        money_won_2 = MathTex(r"\text{Money Won: } \$0")
        money_won_2.move_to(group_copy[3].get_center())
        self.remove(group_copy[3])
        self.play(FadeIn(coin_h_2))
        self.wait(2)
        # money_won_2.shift(DOWN + RIGHT)
        money_won_2.scale(1.5)
        self.play(Write(money_won_2))

        self.wait(2)
        # self.play(FadeOut(group), FadeOut(group_copy), FadeOut(line), FadeOut(money_won_2), FadeOut(coin_h_2))

        text_round = Text("Round 1")
        text_round.move_to(UP*3.2)
        text_correct = Text("Correct Prediction").set_color(GREEN)
        text_correct.next_to(money_won, DOWN)
        text_incorrect = Text("Incorrect Prediction").set_color(RED)
        text_incorrect.next_to(money_won_2, DOWN)
        self.play(Write(text_round), Write(text_correct), Write(text_incorrect))
        self.wait(1)

        text_round_2 = Text("Round 2")
        text_round_2.move_to(UP*3.2)
        self.play(ReplacementTransform(text_round, text_round_2))
        self.wait(1)
        self.play(FadeOut(group[2]), FadeOut(coin_h_2))
        self.wait(1)

        new_flip = coin.animate_flip(group[5],final='H', n_flips=5)
        new_flip_2 = coin.animate_flip(group_copy[5],final='H', n_flips=5)
        for a, b in zip(new_flip, new_flip_2):
            self.play(a, b, run_time=0.1)
        self.play(group[5].animate.scale(0.6), group_copy[5].animate.scale(0.6), run_time=0.3)
        self.wait(2)

        coin_left_round_2 = coin.H.copy().scale(0.48).move_to(group[2])
        coin_right_round_2 = coin.T.copy().scale(0.48).move_to(group_copy[2])
        self.play(FadeIn(coin_left_round_2), FadeIn(coin_right_round_2))
        self.wait(2)

        money_won_round_2 = MathTex(r"\text{Money Won: } \$2").scale(1.5)
        money_won_round_2.move_to(group[3].get_center())
        self.play(ReplacementTransform(money_won, money_won_round_2))
        self.wait(2)

        text_round_3 = Text("Round 3")
        text_round_3.move_to(UP*3.2)
        self.play(ReplacementTransform(text_round_2, text_round_3))
        self.wait(1)
        self.play(FadeOut(coin_left_round_2), FadeOut(coin_right_round_2))
        self.wait(1)

        new_flip_round_3 = coin.animate_flip(group[5],final='H', n_flips=5)
        new_flip_2_round_3 = coin.animate_flip(group_copy[5],final='H', n_flips=5)
        for a, b in zip(new_flip_round_3, new_flip_2_round_3):
            self.play(a, b, run_time=0.1)
        self.play(group[5].animate.scale(0.6), group_copy[5].animate.scale(0.6), run_time=0.3)
        self.wait(2)

        self.play(FadeIn(coin_left_round_2), FadeIn(coin_right_round_2))
        self.wait(2)

        money_won_round_3 = MathTex(r"\text{Money Won: } \$3").scale(1.5)
        money_won_round_3.move_to(group[3].get_center())
        self.play(ReplacementTransform(money_won_round_2, money_won_round_3))
        self.wait(2)

        text_round_M = Text("Round M")
        text_round_M.move_to(UP*3.2)
        self.play(ReplacementTransform(text_round_3, text_round_M))
        self.wait(1)
        self.play(FadeOut(coin_left_round_2), FadeOut(coin_right_round_2))
        self.wait(1)

        new_flip_round_M = coin.animate_flip(group[5],final='T', n_flips=5)
        new_flip_2_round_M = coin.animate_flip(group_copy[5],final='T', n_flips=5)
        for a, b in zip(new_flip_round_M, new_flip_2_round_M):
            self.play(a, b, run_time=0.1)

        self.play(group[5].animate.scale(0.6), group_copy[5].animate.scale(0.6), run_time=0.3)
        self.wait(2)

        coin_left_round_M = coin.T.copy().scale(0.48).move_to(group[2])
        coin_right_round_M = coin.H.copy().scale(0.48).move_to(group_copy[2])
        self.play(FadeIn(coin_left_round_M), FadeIn(coin_right_round_M))

        money_won_round_M = MathTex(r"\text{Money Won: } \$M").scale(1.5)
        money_won_round_M.move_to(group[3].get_center())
        self.play(ReplacementTransform(money_won_round_3, money_won_round_M))
        self.wait(2)


