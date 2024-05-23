from manim import *

class LightCharacter(Scene):
    def light_off_character(self):
        light_off_character = SVGMobject("images/light_out.svg")
        light_off_character.scale(2.5)
        return light_off_character
    
    def light_on_character(self):
        light_on_character = SVGMobject("images/light_on.svg")
        light_on_character.scale(2.5)
        return light_on_character
    
    def dim_on_character(self):
        dim_on_character = SVGMobject("images/light_on (2).svg")
        dim_on_character.scale(2.5)
        return dim_on_character
    
    def construct(self):
        light_off_character = self.light_off_character()
        self.play(Create(light_off_character))
        self.wait(2)

        light_on_character = self.light_on_character()
        self.play(FadeOut(light_off_character), FadeIn(light_on_character))
        self.wait(2)