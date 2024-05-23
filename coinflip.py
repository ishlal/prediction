from manim import *
import coin

class CoinFlip(Scene):
    def construct(self):
        h_coin = coin.H.copy().scale(1).shift(LEFT*3)
        t_coin = coin.T.copy().scale(1).shift(RIGHT*3)

        self.play(Write(h_coin))
        self.play(Write(t_coin))
        self.wait(1)
        # animate_flip(h_coin,final=my_string[i],n_flips=10,side_H = H.copy().scale(2), side_T = T.copy().scale(2))
        # self.play(*coin.animate_flip(h_coin,final='H',n_flips=10,side_H = coin.H, side_T = coin.T,my_scale=1))
        for a in coin.animate_flip(h_coin,final='H', n_flips=1):
               self.play(a,run_time=0.2)
        self.wait(1)