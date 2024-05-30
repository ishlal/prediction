from manim import *
import coin
import light_character
import experts
import random

class scene10(Scene):
    def construct(self):
        text_counting_mistakes = Text("Counting Mistakes").scale(1.2).shift(UP*3)
        self.wait(1)
        # underline under text_counting_mistakes
        underline = Underline(text_counting_mistakes)
        self.play(Create(text_counting_mistakes), Create(underline))
        self.wait(1)

        # Initial parameters
        initial_percentage = 1.00
        final_percentage = 0.45
        angle3_percentage = 0.2
        angle4_percentage = 0.02

        v2_angle2_percentage = 0.5
        v2_angle3_percentage = 0.25
        v2_angle4_percentage = 0.125
        radius = 1.7

        # Calculate angles for the sectors
        initial_angle = initial_percentage * TAU
        final_angle = final_percentage * TAU
        angle3 = angle3_percentage * TAU
        angle4 = angle4_percentage * TAU

        v2_angle2 = v2_angle2_percentage * TAU
        v2_angle3 = v2_angle3_percentage * TAU
        v2_angle4 = v2_angle4_percentage * TAU

        # Create the initial sector (90% filled)
        sector = Sector(
            outer_radius=radius,
            angle=initial_angle,
            start_angle=0,
            color=BLUE,
            fill_opacity=0.5
        )

        # Add the initial sector to the scene
        # self.add(sector)
        sector.shift(LEFT*5)
        sector.scale(0.7)
        text_N = MathTex(r"N").scale(0.8).move_to(sector.get_center() + DOWN*1.6)
        self.play(Create(sector), Create(text_N))
        self.wait(1)

        # Create an updater function to animate the angle change
        # def update_sector(sector, alpha):
        #     new_angle = interpolate(initial_angle, final_angle, alpha)
        #     sector.become(Sector(
        #         outer_radius=radius,
        #         angle=new_angle,
        #         start_angle=0,
        #         color=BLUE,
        #         fill_opacity=0.5
        #     ).scale(0.5).move_to(sector.get_center()))

        # Animate the transition to the final sector
        # self.play(UpdateFromAlphaFunc(sector, update_sector), run_time=3)

        # Create the final sector (55% filled)
        final_sector = Sector(
            outer_radius=radius,
            angle=final_angle,
            start_angle=0,
            color=BLUE,
            fill_opacity=0.5
        ).scale(0.7)
        final_sector.move_to(sector.get_center() + RIGHT*4.2)
        text_N_minus_1 = MathTex(r"\leq \tfrac12 \cdot N").scale(0.8)
        #move text to point where radii meet
        text_N_minus_1.move_to(final_sector.get_center() + DOWN*1.2)
        

        self.wait(1)

        # draw an arrow between sector and final_sector
        arrow = Arrow(sector.get_center() + RIGHT*1.5, final_sector.get_center() + LEFT*1.5, buff=0.2)
        self.play(Create(final_sector), Create(text_N_minus_1), Create(arrow))

        # Keep the final state on screen for a while
        self.wait(1)

        sector_3 = Sector(
            outer_radius = radius,
            angle = angle3,
            start_angle = 0,
            color = BLUE,
            fill_opacity=0.5
        ).scale(0.7)
        sector_3.move_to(final_sector.get_center() + RIGHT*4.2)
        text_N_minus_2 = MathTex(r"\leq \tfrac12 \cdot \tfrac12 \cdot N").scale(0.8)
        text_N_minus_2.move_to(sector_3.get_center() + DOWN*1.2)

        arrow_2 = Arrow(final_sector.get_center() + RIGHT*1.5, sector_3.get_center() + LEFT*1.5, buff=0.2)
        self.play(Create(sector_3), Create(text_N_minus_2), Create(arrow_2))
        self.wait(2)

        # creage group of sectors, text and arrows
        sectors_group = VGroup(sector, final_sector, sector_3, text_N, text_N_minus_1, text_N_minus_2, arrow, arrow_2)
        animation = sectors_group.animate
        self.play(animation.shift(LEFT*1.8), animation.scale(0.7))
        self.wait(2)

        arrow_3 = Arrow(sector_3.get_center() + RIGHT*0.5, sector_3.get_center() + RIGHT*1.5, buff=0.2).scale(0.7)
        cdots = MathTex(r"\cdots").scale(1.5).move_to(arrow_3.get_center() + RIGHT)
        self.play(Create(arrow_3))
        self.play(Create(cdots))
        self.wait(2)

        sector_4 = Sector(
            outer_radius = radius,
            angle = angle4,
            start_angle = 0,
            color = BLUE,
            fill_opacity=0.5
        ).scale(0.7)
        sector_4.move_to(cdots.get_center() + RIGHT*3.2)
        text_N_minus_3 = MathTex(r"\geq 1 <<< N").scale(0.5)
        text_N_minus_3.move_to(sector_4.get_center() + DOWN*0.7)

        arrow_4 = Arrow(cdots.get_center() + RIGHT*1, sector_4.get_center() + LEFT*1, buff=0.2)
        self.play(Create(sector_4), Create(text_N_minus_3), Create(arrow_4))
        self.wait(2)

        # create group out of everything
        sectors_group.add(sector_4, text_N_minus_3, arrow_4, cdots, arrow_3)
        self.play(sectors_group.animate.shift(UP*1.5))
        self.wait(2)

        text_worst_case = Text("Worst Case Scenario").scale(0.6).shift(DOWN*0.5 + LEFT*4.6).set_color(RED)
        underline_worst_case = Underline(text_worst_case).set_color(RED)
        self.play(Create(text_worst_case), Create(underline_worst_case))
        self.wait(2)

        sector_copy = sector.copy().set_color(GREEN)
        sector_copy.move_to(sector.get_center() + DOWN*3.5)
        text_N_2 = MathTex(r"N").scale(0.6).move_to(sector_copy.get_center() + DOWN*1.2)
        self.play(Create(sector_copy), Create(text_N_2))
        self.wait(1)

        v2_sector2 = Sector(
            outer_radius = radius,
            angle = v2_angle2,
            start_angle = 0,
            color = GREEN,
            fill_opacity=0.5
        ).scale(0.5)

        v2_sector2.move_to(sector_copy.get_center() + RIGHT*2.5)
        text_N_minus_1_2 = MathTex(r"= \tfrac12 \cdot N").scale(0.6)
        text_N_minus_1_2.move_to(v2_sector2.get_center() + DOWN*1.2)

        arrow_v2 = Arrow(sector_copy.get_center() + RIGHT*0.75, v2_sector2.get_center() + LEFT*0.75, buff=0.2)
        self.play(Create(v2_sector2), Create(text_N_minus_1_2), Create(arrow_v2))
        self.wait(2)

        v3_sector = Sector(
            outer_radius = radius,
            angle = v2_angle3,
            start_angle = 0,
            color = GREEN,
            fill_opacity=0.5
        ).scale(0.5)

        v3_sector.move_to(v2_sector2.get_center() + RIGHT*2.5)
        text_N_minus_2_2 = MathTex(r"= \tfrac14 \cdot N").scale(0.6)
        text_N_minus_2_2.move_to(text_N_minus_1_2.get_center() + RIGHT*2.5)

        arrow_v3 = Arrow(v2_sector2.get_center() + RIGHT*0.75, v3_sector.get_center() + LEFT*0.75, buff=0.2)
        self.play(Create(v3_sector), Create(text_N_minus_2_2), Create(arrow_v3))
        self.wait(2)

        v4_sector = Sector(
            outer_radius = radius,
            angle = v2_angle4,
            start_angle = 0,
            color = GREEN,
            fill_opacity=0.5
        ).scale(0.5)

        v4_sector.move_to(v3_sector.get_center() + RIGHT*2.5)
        text_N_minus_3_2 = MathTex(r"= \tfrac18 \cdot N").scale(0.5)
        text_N_minus_3_2.move_to(text_N_minus_2_2.get_center() + RIGHT*2.5)

        arrow_v4 = Arrow(v3_sector.get_center() + RIGHT*0.75, v4_sector.get_center() + LEFT*0.75, buff=0.2)
        self.play(Create(v4_sector), Create(text_N_minus_3_2), Create(arrow_v4))
        self.wait(2)

        cdots2 = MathTex(r"\cdots").scale(1.5).move_to(v4_sector.get_center() + RIGHT*1.7)
        self.play(Create(cdots2))
        self.wait(2)

        sector_4_copy = sector_4.copy().set_color(GREEN)
        sector_4_copy.move_to(cdots2.get_center() + RIGHT*1.7)
        text_N_minus_4 = MathTex(r"=\left(\frac12\right)^M \cdot N").scale(0.5)
        text_N_minus_4.move_to(sector_4_copy.get_center() + DOWN*1.2)
        self.play(Create(sector_4_copy), Create(text_N_minus_4))
        self.wait(2)

        group_v2 = VGroup(text_worst_case, underline_worst_case, v2_sector2, v3_sector, v4_sector, sector_copy, sector_4_copy, text_N_2, text_N_minus_1_2, text_N_minus_2_2, text_N_minus_3_2, text_N_minus_4, arrow_v2, arrow_v3, arrow_v4, cdots2)

        self.play(FadeOut(text_counting_mistakes), FadeOut(underline), FadeOut(sectors_group), 
                  FadeOut(arrow), FadeOut(arrow_2), FadeOut(arrow_3), FadeOut(arrow_4), FadeOut(cdots),
                  FadeOut(sector_4), FadeOut(text_N_minus_3))

        self.wait(0.5)

        self.play(group_v2.animate.shift(UP*3.5))

        text_N_minus_4_copy = text_N_minus_4.copy()
        animation2 = text_N_minus_4_copy.animate
        self.play(animation2.shift(DOWN*1.5 + LEFT*10), animation2.scale(2))
        self.wait(2)

        geq_1 = MathTex(r"\geq 1").scale(1.2).move_to(text_N_minus_4_copy.get_center() + RIGHT*2.5)
        self.play(Create(geq_1))
        self.wait(2)

        imp = MathTex(r"\implies N \geq 2^M").scale(1.2).move_to(text_N_minus_4_copy.get_center() + RIGHT*6.5)
        self.play(Create(imp))
        self.wait(2)

        conc = MathTex(r"\implies M \leq \log_2 N").scale(1.2).move_to(text_N_minus_4_copy.get_center() + RIGHT*6.5 + DOWN*1.5)
        self.play(Create(conc))
        self.wait(2)
