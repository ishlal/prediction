from manim import *
import coin
import experts
import light_character
import random 

class scene16(Scene):
    def construct(self):
        line_1 = Line(UP*3 + LEFT*2.5, DOWN*3 + LEFT*2.5)

        line_2 = Line(UP*3 + RIGHT*2.5, DOWN*3 + RIGHT*2.5)

        self.play(Create(line_1), Create(line_2))

        self.wait(2)

        text_modification_1 = Text("Modification 1").scale(0.7).shift(UP*3 + LEFT*4.9)
        self.play(Write(text_modification_1))
        self.wait(1)

        expert_group = VGroup(
            *[experts.experts().get_expert(random.randint(1,4)).scale(0.23)
              for j in range(4)]
        ).arrange_in_grid(2, 2, buff=0.7).shift(LEFT*4.9)

        self.play(FadeIn(expert_group))
        self.wait(2)

        cap_1 = Text("Outcome 1").scale(0.35).next_to(expert_group[0], DOWN)
        cap_2 = Text("Outcome 2").scale(0.35).next_to(expert_group[1], DOWN)
        cap_3 = Text("Outcome 3").scale(0.35).next_to(expert_group[2], DOWN)
        cap_4 = Text("Outcome 4").scale(0.35).next_to(expert_group[3], DOWN)

        self.play(Write(cap_1), Write(cap_2), Write(cap_3), Write(cap_4))
        self.wait(2)

        full_caption_1 = Text("Experts represent the outcomes").scale(0.45).next_to(expert_group, DOWN)
        full_caption_1.shift(DOWN*0.5)
        self.play(Write(full_caption_1))
        self.wait(2)

        text_modification_2 = Text("Modification 2").scale(0.7).shift(UP*3)
        self.play(Write(text_modification_2))
        self.wait(1)

        expert = experts.experts().get_trusted_expert(3).scale(0.5).shift(DOWN)
        self.play(FadeIn(expert))
        self.wait(2)

        overbrace = Brace(expert[1], UP)
        text_overbrace = overbrace.get_text("Probability").scale(0.5)
        self.play(Create(overbrace), Write(text_overbrace))

        self.wait(2)

        text_modification_3 = Text("Modification 3").scale(0.7).shift(UP*3 + RIGHT*4.9)
        self.play(Write(text_modification_3))
        self.wait(1)

        og_penalty = MathTex(r"\text{Original Penalty: }\tfrac12").scale(0.7)
        og_penalty.shift(RIGHT*4.9 + UP)

        new_penalty = MathTex(r"\text{New Penalty: }(1- \epsilon \ell)").scale(0.7)
        new_penalty.shift(RIGHT*4.9)
        self.play(Write(og_penalty))
        self.wait(1)
        self.play(Write(new_penalty))
        self.wait(1)

        blist_explanation = BulletedList(
            r"$\epsilon \in (0, 1)$ is a smoothing parameter",
            r"$\ell \in (0, 1)$ is the loss"
        ).scale(0.5)

        blist_explanation.shift(RIGHT*4.9 + DOWN*1.5)
        self.play(Create(blist_explanation))
        self.wait(2)

        everything_group = VGroup(
            line_1,
            line_2,
            text_modification_1,
            expert_group,
            cap_1,
            cap_2,
            cap_3,
            cap_4,
            full_caption_1,
            text_modification_2,
            expert,
            overbrace,
            text_overbrace,
            text_modification_3,
            og_penalty,
            new_penalty,
            blist_explanation
        )

        main_eq = MathTex(r"\mathbb{E}[\text{our loss}] \leq \mathbb{E}[\text{loss of best expert}] + 2 T\cdot \sqrt{\frac{\ln(N)}{T}}")
        main_eq.scale(1)
        main_eq.shift(UP)
        self.play(Transform(everything_group, main_eq))
        self.wait(2)

        old_eq_1 = MathTex(r"(\text{Our Loss}) \leq ")
        old_eq_2 = MathTex(r"2.4")
        old_eq_3 = MathTex(r"\cdot (\text{Loss of best expert}) + 2.4 \cdot \sqrt{\ln(N)}")
        old_eq_2.next_to(old_eq_1, RIGHT)
        old_eq_3.next_to(old_eq_2, RIGHT)
        old_eq_2.set_color(RED)
        old_eq = VGroup(old_eq_1, old_eq_2, old_eq_3)
        old_eq.move_to(ORIGIN)
        old_eq.scale(1)
        old_eq.shift(DOWN)
        self.play(Write(old_eq))
        self.wait(2)

        self.play(FadeOUt(old_eq), FadeOut(main_eq))
        self.wait(2)

