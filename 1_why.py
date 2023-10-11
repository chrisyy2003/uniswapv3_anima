from manim import *

class Scene1(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):

        eq1 = MathTex(
            "X", "\\times", "Y", "= K"
        )
        self.play(Write(eq1))
        self.play(eq1.animate.move_to([3,2,0]))


        ax_value = ValueTracker(10)

        def get_axex():
            return Axes(
                x_range=[0, ax_value.get_value()],
                y_range=[0, ax_value.get_value()],
                x_length=6,
                y_length=6,
                axis_config={"include_tip": False},
            )
        ax = always_redraw(get_axex)

        t = ValueTracker(4)
        k = ValueTracker(25)

        def get_graph():
            return ax.plot(
                lambda x: k.get_value() / x,
                color=YELLOW_D,
                x_range=[k.get_value() / 10, 10.0, 0.01],
                use_smoothing=False,
            )

        graph = always_redraw(get_graph)

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (t.get_value(), k.get_value() / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon
        
        
        
        polygon1 = get_rectangle()

        x_det = Line()
        x_det.add_updater(lambda x: x.become(Line(ax.c2p(4, k.get_value() / t.get_value()),  ax.c2p(t.get_value(), k.get_value() / t.get_value()))))

        y_det = Line()
        y_det.add_updater(lambda x: x.become(Line(ax.c2p(4, k.get_value() / 4),  ax.c2p(4, k.get_value() / t.get_value()))))


        fix_dot = Dot(point=[ax.c2p(4, k.get_value() / 4)])
        fix_dot.add_updater(lambda x: x.move_to(ax.c2p(4, k.get_value() / 4)))
        fix_dot_with_label = VGroup(fix_dot, Tex("A").add_updater(lambda x: x.next_to(fix_dot, UP)))

        dot_x = Dot()
        dot_x.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k.get_value() / t.get_value())))
        dot_x_lab = Tex("B")
        dot_x_lab.add_updater(lambda x: x.next_to(dot_x, UP))
        dox_x_with_lab = VGroup(dot_x, dot_x_lab)


        self.play(Create(VGroup(ax, graph, dox_x_with_lab, fix_dot_with_label, x_det, y_det)))
        self.play(t.animate.set_value(8))


        eq2 = MathTex(
            "(","X", "+ \\Delta x)", "\\times", "Y", "= K"
        ).move_to(eq1)

        x_det_brace = BraceBetweenPoints(ax.c2p(4, k.get_value() / t.get_value()),  ax.c2p(t.get_value(), k.get_value() / t.get_value()))
        x_det_brace_lab = x_det_brace.get_tex("\\Delta x")
        self.play(Create(x_det_brace), Create(x_det_brace_lab))
        self.play(TransformMatchingTex(eq1, eq2))

        eq3 = MathTex(
            "(","X", "+ \\Delta x)", "\\times", "(","Y", "- \\Delta y", ")", "= K"
        ).move_to(eq1)

        y_det_brace = BraceBetweenPoints(ax.c2p(4, k.get_value() /4),  ax.c2p(4, k.get_value() / t.get_value()))
        y_det_brace_lab = y_det_brace.get_tex("\\Delta y")
        self.play(Create(y_det_brace), Create(y_det_brace_lab))
        self.play(TransformMatchingTex(eq2, eq3))

        p_v = ValueTracker(5)
        p = Dot()
        p.add_updater(lambda x: x.move_to(ax.c2p(p_v.get_value(), k.get_value() / p_v.get_value())))
        p_lab = Tex("Price")
        p_lab.add_updater(lambda x: x.next_to(p, UP))
        self.play(Create(p))

        def get_rectangle2():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (p_v.get_value(), k.get_value() / p_v.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon

        # 这就是一次正常的v2交易

        self.play(FadeOut(y_det_brace, y_det_brace_lab, x_det_brace, x_det_brace_lab, eq3))

        polygon2 = get_rectangle()
        self.play(Create(polygon1), Create(polygon2))

        polygon3 = always_redraw(get_rectangle2)
        self.play(Create(polygon3))
        self.play(p_v.animate.set_value(7))
        self.play(p_v.animate.set_value(5))

        def get_rectangle3():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (4, k.get_value() / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(GREEN, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon
        i = always_redraw(get_rectangle3)
        self.play(FadeIn(i), FadeOut(polygon1, polygon2, polygon3))

        # 计算利用率
        x_real = always_redraw(lambda : BraceBetweenPoints(ax.c2p(0, k.get_value() / t.get_value()),  ax.c2p(4, k.get_value() / t.get_value()), UP))
        x_real_lab = x_real.get_tex("x_{pool}")
        x_real_lab.add_updater(lambda lab: lab.next_to(x_real, UP))

        x_add = always_redraw(lambda : BraceBetweenPoints(ax.c2p(4, k.get_value() / t.get_value()),  ax.c2p(t.get_value(), k.get_value() / t.get_value())))
        x_add_lab = x_add.get_tex("\\Delta x")
        x_add_lab.add_updater(lambda lab: lab.next_to(x_add, DOWN))

        self.play(Create(x_real), Create(x_add), Create(x_real_lab), Create(x_add_lab))
        usage = MathTex(
            "\\frac{\\Delta x}{x_{pool}}"
        )
        usage.move_to([2,2,0])
        self.play(TransformMatchingTex(Group(x_real_lab, x_add_lab), usage), FadeOut(x_real, x_add))

        # 但是实际情况可能更低
        self.play(ax_value.animate.set_value(20), k.animate.set_value(10), t.animate.set_value(4.5), FadeOut(p))
        
        self.wait(3)