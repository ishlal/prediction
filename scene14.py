from manim import *
import coin
import light_character
import experts
import random

class scene14(Scene):
    def construct(self):

        upper_text = Text("Suppose our algorithm makes M mistakes").scale(1).shift(UP*3)
        underline = Underline(upper_text)
        self.play(Write(upper_text), Create(underline))
        self.wait(2)

        phi_t = MathTex(r"\phi^t").scale(1.5).shift(LEFT*1.5)

        self.play(Create(phi_t))
        self.wait(1)

        phi_t_plus_1 = MathTex(r"\phi^{t+1}").scale(1.5).shift(RIGHT*1.5)
        curvy_arrow = CurvedArrow(phi_t.get_bottom() + DOWN*0.2, phi_t_plus_1.get_bottom() + DOWN*0.2 + LEFT*0.2, angle=TAU/6)

        self.play(Create(phi_t_plus_1), Create(curvy_arrow))
        self.wait(1)
        text_mistake = Text("Mistake").scale(0.7).next_to(curvy_arrow, DOWN)
        self.play(Create(text_mistake))
        self.wait(2)

        leq = MathTex(r"\leq \tfrac34 \cdot \phi^t").scale(1.5).next_to(phi_t_plus_1, RIGHT)

        group_for_later = VGroup(leq, phi_t_plus_1)
        self.play(Create(leq))
        self.wait(2)

        group_1 = VGroup(phi_t, phi_t_plus_1, curvy_arrow, text_mistake, leq)
        bounding_box = SurroundingRectangle(group_1, buff=0.2).set_color(WHITE)
        group_1.add(bounding_box)
        self.play(Create(bounding_box))
        group_1_animation = group_1.animate
        self.play(group_1_animation.shift(UP*2 + LEFT*5.5), group_1_animation.scale(0.5))
        self.wait(2)

        text_n_experts = Text("N total experts").scale(1)
        self.play(Write(text_n_experts))
        self.wait(1)
        bbox_2 = SurroundingRectangle(text_n_experts, buff=0.2).set_color(WHITE)
        self.play(Create(bbox_2))
        group_2 = VGroup(text_n_experts, bbox_2)
        group_2_animation = group_2.animate
        self.play(group_2_animation.shift(UP*1.7 + RIGHT*4), group_2_animation.scale(0.7))
        self.wait(2)

        text_phi_1 = MathTex(r"N = \phi^{t=1}").scale(0.8)
        self.play(Write(text_phi_1))
        self.wait(2)
        text_phi_1_anim = text_phi_1.animate
        self.play(text_phi_1_anim.shift(DOWN*0.5 + LEFT*5))
        self.wait(2)
        text_more = MathTex(r"\geq \phi^2 \geq \ldots \geq ").scale(0.8)
        text_more_2 = MathTex(r"\phi^i").scale(0.8)
        text_more_3 = MathTex(r"\geq").scale(0.8)
        text_more_4 = MathTex(r"\phi^{i+1}").scale(0.8)
        text_more_5 = MathTex(r"\geq \ldots \geq ").scale(0.8)
        text_more_6 = MathTex(r"\phi^j").scale(0.8)
        text_more_7 = MathTex(r"\geq").scale(0.8)
        text_more_8 = MathTex(r"\phi^{j+1}").scale(0.8)
        text_more_9 = MathTex(r"\geq \ldots \geq \phi^t").scale(0.8)
        text_more.next_to(text_phi_1, RIGHT)
        text_more_2.next_to(text_more, RIGHT)
        text_more_3.next_to(text_more_2, RIGHT)
        text_more_4.next_to(text_more_3, RIGHT)
        text_more_5.next_to(text_more_4, RIGHT)
        text_more_6.next_to(text_more_5, RIGHT)
        text_more_7.next_to(text_more_6, RIGHT)
        text_more_8.next_to(text_more_7, RIGHT)
        text_more_9.next_to(text_more_8, RIGHT)
        text_more_group = VGroup(text_more, text_more_2, text_more_3, text_more_4, text_more_5, text_more_6, text_more_7, text_more_8, text_more_9)
        text_leftover_group = VGroup(text_more, text_more_3, text_more_5, text_more_7, text_more_9)
        self.play(Write(text_more_group))
        self.wait(2)

        arrow_2 = CurvedArrow(text_more_2.get_top() + UP*0.2, text_more_4.get_top()+UP*0.2, angle=-TAU/6)
        #change stroke width
        arrow_2.set_stroke(width=4)
        #change size of arrow head
        arrow_2.tip.scale(0.3)
        self.play(Create(arrow_2))
        text_mistake = Text("Mistake 1").scale(0.4).next_to(arrow_2, UP)
        self.play(Create(text_mistake))
        self.wait(2)

        group_to_highlight = VGroup(text_more_2, text_more_4, arrow_2, text_mistake)
        bounding_box_highlight = SurroundingRectangle(group_to_highlight, buff=0.2).set_color(PINK)
        self.play(Create(bounding_box_highlight), bounding_box.animate.set_color(PINK))
        self.wait(2)

        group_to_copy = VGroup(text_more_2, text_more_3, text_more_4)
        group_to_copy_copy = group_to_copy.copy()

        self.play(group_to_copy_copy.animate.shift(DOWN*1.5 + LEFT*3))
        group_for_later_copy = group_for_later.copy()
        self.wait(1)
        self.play(group_for_later_copy.animate.next_to(group_to_copy_copy, RIGHT, buff=1.5))    
        self.wait(2)

        text_new = MathTex(r"\phi^{i+1} \leq \phi^i").scale(0.8).move_to(group_to_copy_copy.get_center())
        text_new_2 = MathTex(r"\phi^{i+1} \leq \tfrac34 \cdot \phi^i").scale(0.8).move_to(group_for_later_copy.get_center())

        self.play(Transform(group_to_copy_copy, text_new))
        self.wait(2)
        self.play(Transform(group_for_later_copy, text_new_2))
        self.wait(2)
        text_conc = MathTex(r"\implies \phi^{t+1} \leq \tfrac34 \cdot \phi^t").scale(0.8)
        text_conc.next_to(text_new_2, RIGHT, buff=1)
        self.play(Write(text_conc))
        self.wait(2)
        text_conc_2 = MathTex(r"\leq \tfrac34 \cdot N").scale(0.8).next_to(text_conc, RIGHT)
        self.play(Write(text_conc_2))
        self.wait(2)

        self.play(
            FadeOut(group_to_copy_copy), FadeOut(group_for_later_copy), FadeOut(text_conc)
        )
        self.wait(1)
        conc_2_anim = text_conc_2.animate
        self.play(
            conc_2_anim.scale(0.8), conc_2_anim.next_to(text_more_4, DOWN), conc_2_anim.shift(LEFT*0.1)
        )
        group_to_highlight.add(text_conc_2)
        bounding_box_highlight_2 = SurroundingRectangle(group_to_highlight, buff=0.2).set_color(PINK)
        self.play(Transform(bounding_box_highlight, bounding_box_highlight_2))
        self.wait(2)

        arrow_2 = CurvedArrow(text_more_6.get_top() + UP*0.2, text_more_8.get_top()+UP*0.2, angle=-TAU/6)
        #change stroke width
        arrow_2.set_stroke(width=4)
        #change size of arrow head
        arrow_2.tip.scale(0.3)
        self.play(Create(arrow_2))
        text_mistake = Text("Mistake 2").scale(0.4).next_to(arrow_2, UP)
        self.play(Create(text_mistake))
        self.wait(2)

        group_help_me_please = group_to_highlight
        bounding_box_help_me = bounding_box_highlight

        group_to_highlight = VGroup(text_more_6, text_more_8, arrow_2, text_mistake)


        leq_again = MathTex(r"\leq \tfrac34 \cdot \phi^j").scale(0.7).next_to(text_more_8, DOWN)
        leq_again.shift(LEFT*0.2)
        group_to_highlight = VGroup(text_more_6, text_more_8, arrow_2, text_mistake, leq_again)

        bounding_box_highlight = SurroundingRectangle(group_to_highlight, buff=0.2).set_color(PINK)
        self.play(Create(bounding_box_highlight), bounding_box.animate.set_color(PINK))
        self.wait(2)
        self.play(FadeIn(leq_again))
        self.wait(2)
        leq_transform = MathTex(r"\leq \tfrac34 \cdot \tfrac34 \cdot N").scale(0.7).next_to(text_more_7, DOWN)
        leq_transform.shift(RIGHT*0.3)
        self.play(Transform(leq_again, leq_transform))
        self.wait(2)
        leq_transform_final = MathTex(r"\leq\left(\tfrac34\right)^2 \cdot N").scale(0.7).next_to(text_more_7, DOWN)
        leq_transform_final.shift(RIGHT*0.3)
        self.play(Transform(leq_again, leq_transform_final))
        self.wait(2)

        text_last = MathTex(r"\text{After the } M^{th} \text{ mistake: }").scale(0.8).shift(DOWN*2)
        text_last_p2 = MathTex(r"\phi^{t} \leq \left(\tfrac34\right)^M \cdot N").scale(0.8).next_to(text_last, DOWN)
        self.play(Write(text_last))
        self.wait(1)
        self.play(Write(text_last_p2))
        self.wait(2)

        text_last_group = VGroup(text_last, text_last_p2)

        self.play(
            FadeOut(upper_text),
            FadeOut(text_leftover_group),
            FadeOut(text_phi_1),
            FadeOut(bounding_box_highlight),
            FadeOut(group_help_me_please),
            FadeOut(bounding_box_help_me),
            FadeOut(group_to_highlight),

        )
        self.wait(2)

        box_around_text = SurroundingRectangle(text_last_group, buff=0.2).set_color(WHITE)
        self.play(Create(box_around_text))
        self.wait(1)
        text_last_group.add(box_around_text)
        text_last_group_animation = text_last_group.animate
        self.play(
            text_last_group_animation.next_to(group_1, RIGHT),
            text_last_group_animation.scale(0.8)
        )
        self.wait(2)

        text_up = Text("Suppose Best Expert makes `BEST ` mistakes").scale(0.9).shift(UP*3)
        self.play(Write(text_up))
        self.wait(2)

        best_expert = experts.experts().best_expert().scale(0.4)
        best_expert.shift(DOWN*0.5 + LEFT*5)
        text_best_expert = Text("Best Expert").scale(0.6).next_to(best_expert, DOWN)
        self.play(Create(best_expert))
        self.play(Create(text_best_expert))
        self.wait(2)

        phi_start = MathTex(r"\phi^{t=1}_{BEST} = 1").next_to(best_expert, RIGHT)
        self.play(Write(phi_start))
        self.wait(2)

        phi_2 = MathTex(r"\tfrac12").next_to(phi_start, RIGHT)
        phi_2.shift(RIGHT)
        self.play(Write(phi_2))
        curved_arrow_12 = CurvedArrow(phi_start.get_bottom() + DOWN*0.2, phi_2.get_bottom() + DOWN*0.2, angle=TAU/6)
        curved_arrow_12_text = Text("Mistake #1").scale(0.4).next_to(curved_arrow_12, DOWN)
        self.play(Create(curved_arrow_12), Create(curved_arrow_12_text))
        self.wait(2)

        phi_3 = MathTex(r"\tfrac12 \cdot \tfrac12").next_to(phi_2, RIGHT)
        phi_3.shift(RIGHT)
        self.play(Write(phi_3))
        self.wait(1)
        phi_3_v2 = MathTex(r"\tfrac14").next_to(phi_2, RIGHT)
        phi_3_v2.shift(RIGHT)
        self.play(Transform(phi_3, phi_3_v2))
        curved_arrow_23 = CurvedArrow(phi_2.get_bottom() + DOWN*0.2, phi_3_v2.get_bottom() + DOWN*0.2, angle=TAU/6)
        curved_arrow_23_text = Text("Mistake #2").scale(0.4).next_to(curved_arrow_23, DOWN)
        self.play(Create(curved_arrow_23), Create(curved_arrow_23_text))
        self.wait(2)

        phi_4 = MathTex(r"\tfrac12 \cdot \tfrac14").next_to(phi_3, RIGHT)
        phi_4.shift(RIGHT)
        self.play(Write(phi_4))
        self.wait(1)
        phi_4_v2 = MathTex(r"\tfrac18").next_to(phi_3, RIGHT)
        phi_4_v2.shift(RIGHT)
        self.play(Transform(phi_4, phi_4_v2))
        curved_arrow_34 = CurvedArrow(phi_3.get_bottom() + DOWN*0.2, phi_4_v2.get_bottom() + DOWN*0.2, angle=TAU/6)
        curved_arrow_34_text = Text("Mistake #3").scale(0.4).next_to(curved_arrow_34, DOWN)
        self.play(Create(curved_arrow_34), Create(curved_arrow_34_text))
        self.wait(2)

        cdots = MathTex(r"\cdots").next_to(phi_4, RIGHT)
        cdots.shift(RIGHT*0.5)
        self.play(Write(cdots))
        self.wait(2)

        phi_final = MathTex(r"\left(\tfrac12\right)^{BEST}").next_to(cdots, RIGHT)
        phi_final.shift(RIGHT*0.5)
        self.play(Write(phi_final))
        self.wait(1)
        # curved_arrow_last = CurvedArrow(cdots.get_bottom() + DOWN*0.7 + RIGHT*0.4, phi_final.get_bottom() + DOWN*0.2 + LEFT*0.3, angle=TAU/6)
        curved_arrow_last = CurvedArrow(curved_arrow_34.get_start() + RIGHT*3, phi_final.get_bottom() + DOWN*0.2 + LEFT*0.5, angle=TAU/6)
        curved_arrow_last_text = Text("Mistake #BEST").scale(0.4).next_to(curved_arrow_last, DOWN)
        self.play(Create(curved_arrow_last), Create(curved_arrow_last_text))
        self.wait(2)

        text_conc = MathTex(r"\phi^{t}_{BEST} = \left(\tfrac12\right)^{BEST}")
        text_conc.shift(DOWN*3 + LEFT*2)
        self.play(Write(text_conc))

        text_impl = MathTex(r"\implies \phi^t \geq \left(\tfrac12 \right)^{BEST}")
        text_impl.next_to(text_conc, RIGHT)
        self.play(Write(text_impl))
        self.wait(2)

        bounding_box_conc = SurroundingRectangle(text_impl, buff=0.2).set_color(YELLOW)
        self.play(Create(bounding_box_conc))
        self.wait(2)
