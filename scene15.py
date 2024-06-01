from manim import *
import coin 
import light_character
import experts
import random

class scene15(Scene):
    def construct(self):
        # reminder_1 = Text("Reminder").scale(1.2).shift(UP*3)
        # eq_1 = MathTex(r"\phi^t \leq \left(\tfrac34\right)^M")
        bulleted_list_1 = BulletedList(
            r"Algorithm makes M mistakes",
            r"Best expert makes BEST mistakes",
            r"There are N total experts"
        ).scale(0.8)


        bulleted_list_2 = BulletedList(
            r"$\phi^t \leq N \cdot \left(\tfrac34\right)^M$",
            r"$\phi^t \geq \left(\tfrac12\right)^{BEST}$"
        ).scale(1)

        bulleted_list_1.arrange(DOWN, aligned_edge = LEFT)
        bulleted_list_2.arrange(DOWN, aligned_edge = LEFT)

        vgroup = VGroup(bulleted_list_1, bulleted_list_2).arrange(RIGHT, buff=1)
        vgroup.shift(UP*2)
        
        for item in bulleted_list_1:
            self.play(Write(item))
            self.wait(1)

        for item in bulleted_list_2:
            self.play(Write(item))
            self.wait(1)

        self.wait(2)

        transformed_bullet = MathTex(r"\left(\tfrac12\right)^{BEST} \leq \phi^t")

        transformed_bullet.shift(LEFT*2)
        bullet_2_2 = bulleted_list_2[1].copy()
        # bullet_2_2_animation = bullet_2_2.animate
        self.play(ReplacementTransform(bullet_2_2, transformed_bullet))
        self.wait(2)

        transformed_bullet_2 = MathTex(r" \leq N \cdot \left(\tfrac34\right)^M")
        transformed_bullet_2.next_to(transformed_bullet, RIGHT)
        bullet_2_1 = bulleted_list_2[0].copy()
        self.play(ReplacementTransform(bullet_2_1, transformed_bullet_2))
        self.wait(2)

        impl = MathTex(r"\implies \left(\tfrac43\right)^M \leq N \cdot 2^{BEST}")
        impl.next_to(bullet_2_1, DOWN)
        impl.shift(LEFT*2.1 + DOWN*0.5)
        self.play(Write(impl))

        self.wait(2)

        conclusion_1 = MathTex(r"M \leq")
        conclusion_2 = MathTex(r"2.4 \cdot BEST")
        conclusion_3 = MathTex(r"+")
        conclusion_4 = MathTex(r"2.4 \log N")
        conclusion_2.next_to(conclusion_1, RIGHT)
        conclusion_3.next_to(conclusion_2, RIGHT)
        conclusion_4.next_to(conclusion_3, RIGHT)
        conclusion = VGroup(conclusion_1, conclusion_2, conclusion_3, conclusion_4)
        conclusion.next_to(impl, DOWN)
        conclusion.shift(DOWN*0.5)
        box = SurroundingRectangle(conclusion, buff=0.1)
        self.play(Write(conclusion), Create(box))
        self.wait(2)

        self.play(FadeOut(vgroup), FadeOut(impl), FadeOut(transformed_bullet), FadeOut(transformed_bullet_2))
        self.wait(0.5)
        conclusion_group = VGroup(conclusion, box)
        self.play(conclusion_group.animate.move_to(ORIGIN + UP*3))
        self.wait(2)

        blist_questions = BulletedList(
            r"Can we reduce the 2.4 factor?",
            r"What do we do if there are multiple outcomes?"
        ).scale(0.8)
        self.play(Write(blist_questions[0]), run_time=3)
        self.wait(1)
        self.play(Write(blist_questions[1]), run_time=3)
        self.wait(2)
        self.play(FadeOut(blist_questions), FadeOut(conclusion_group))
        self.wait(2)
