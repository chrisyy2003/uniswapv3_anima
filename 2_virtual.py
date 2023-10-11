from manim import *

class Scene2(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):

        ax_value = ValueTracker(10)

        ax = Axes(
                x_range=[0, ax_value.get_value()],
                y_range=[0, ax_value.get_value()],
                x_length=6,
                y_length=6,
                axis_config={"include_tip": False},
            )

        t = ValueTracker(8)
        k = ValueTracker(25)

        graph = ax.plot(
                lambda x: k.get_value() / x,
                color=YELLOW_D,
                x_range=[k.get_value() / 10, 10.0, 0.01],
                use_smoothing=False,
            )

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
        i = get_rectangle3()
        

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

        base = VGroup(i, ax, graph, dox_x_with_lab, fix_dot_with_label, x_det, y_det)
        self.play(Create(base))

        p_v = ValueTracker(5)
        p = Dot()
        p.add_updater(lambda x: x.move_to(ax.c2p(p_v.get_value(), k.get_value() / p_v.get_value())))
        p_lab = Tex("Price").scale(0.9)
        p_lab.add_updater(lambda x: x.next_to(p, UP))
        self.play(Create(p), Create(p_lab),p_v.animate.set_value(6))

        # 其实在交换的时候，可以发现绿色的流动性并没有参加任何交换，只是将流动性抬高到了这个位置

        eq0 = MathTex(
            "X", "\\times", "Y", "= K"
        ).move_to([3,2,0]).scale(0.8)
        self.play(Create(eq0))

        eq2 = MathTex(
            "(","X_{virtual}", "+ X_{real})", "\\times", "Y", "= K"
        ).move_to([3,2,0]).scale(0.8)
        self.play(TransformMatchingTex(eq0, eq2))

        eq3 = MathTex(
            "(","X_{virtual}", "+ X_{real})", "\\times", "(","Y_{virtual}", "+ Y_{real}", ")", "= K"
        ).move_to([3,2,0]).scale(0.8)
        self.play(TransformMatchingTex(eq2, eq3))


        # virtual具体是多少 由于在这个曲线上, 显然是跟选取的AB两个点相关的，所以我们可以将它表示出来
        
        x_det_brace = BraceBetweenPoints(ax.c2p(0, k.get_value() / t.get_value()), ax.c2p(4, k.get_value() / t.get_value())).scale(0.8)
        x_det_brace_lab = x_det_brace.get_tex("X_{virtual}")
        self.play(Create(x_det_brace), Create(x_det_brace_lab))
        
        y_det_brace = BraceBetweenPoints(ax.c2p(4, 0), ax.c2p(4, k.get_value() / t.get_value())).scale(0.8)
        y_det_brace_lab = y_det_brace.get_tex("Y_{virtual}")
        self.play(Create(y_det_brace), Create(y_det_brace_lab))

        priceA = DashedLine(ax.c2p(0, 0),  ax.c2p(4, k.get_value() / 4))
        labA = Tex("PriceA").next_to(priceA, UP)

        priceB = DashedLine(ax.c2p(0, 0),  ax.c2p(t.get_value(), k.get_value() / t.get_value()))
        labb = Tex("PriceB").next_to(priceB, DOWN)
        self.play(Create(priceB), Create(labb))
        # 同理这是a的价格
        self.play(Create(priceA), Create(labA), FadeOut(priceB), FadeOut(labb))

        eqx1 = MathTex(
                '''
                \\left.\\begin{array}{c}
                \\frac{Y_a}{X_a}=P_a \\\\
                X_a \\times Y_a=L^2
                \\end{array}\\right\\}
                '''
            ).move_to([3,1,0]).scale(0.8)

        eqx2 = MathTex(
                '''
                \\left.\\begin{array}{c}
                \\frac{Y_a}{X_a}=P_a \\\\
                X_a \\times Y_a=L^2
                \\end{array}\\right\\}
                ''',
                "\\Rightarrow X_a"
        ).move_to([3,1,0]).scale(0.8)
        
        eqx3 = MathTex(
                '''
                \\left.\\begin{array}{c}
                \\frac{Y_a}{X_a}=P_a \\\\
                X_a \\times Y_a=L^2
                \\end{array}\\right\\}
                ''',
                "\\Rightarrow X_a",
                "=\\frac{L}{\\sqrt{P_a}}"
        ).move_to([3,1,0]).scale(0.8)
        
        self.play(Write(eqx1))
        self.play(TransformMatchingTex(eqx1, eqx2))
        self.play(TransformMatchingTex(eqx2, eqx3))

        eqxv = MathTex(
            "(","\\frac{L}{\\sqrt{P_a}}", "+ X_{real})", "\\times", "(","Y_{virtual}", "+ Y_{real}", ")", "= K"
        ).move_to([3,2,0]).scale(0.8)
        self.play(TransformMatchingTex(eq3, eqxv))
        self.play(FadeOut(eqx3))

        # 然后同理虚拟y 我们也可以得到B点拿到

        eqy1 = MathTex(
                '''
                \\left.\\begin{array}{c}
                \\frac{Y_b}{X_b}=P_b \\\\
                X_b \\times Y_b=L^2
                \\end{array}\\right\\}
                '''
        ).move_to([3,1,0]).scale(0.8)

        eqy2 = MathTex(
                '''
                \\left.\\begin{array}{c}
                \\frac{Y_b}{X_b}=P_b \\\\
                X_b \\times Y_b=L^2
                \\end{array}\\right\\}
                ''',
                "\\Rightarrow Y_b"
            ).move_to([3,1,0]).scale(0.8)
        
        eqy3 = MathTex(
                '''
                \\left.\\begin{array}{c}
                \\frac{Y_b}{X_b}=P_b \\\\
                X_b \\times Y_b=L^2
                \\end{array}\\right\\}
                ''',
                "\\Rightarrow Y_b",
                "=L \\sqrt{P_b}}"
            ).move_to([3,1,0]).scale(0.8)

        self.play(Write(eqy1))
        self.play(TransformMatchingTex(eqy1, eqy2))
        self.play(TransformMatchingTex(eqy2, eqy3))

        eqyv = MathTex(
            "(","\\frac{L}{\\sqrt{P_a}}", "+ X_{real})", "\\times", "(","L \\sqrt{P_b}}", "+ Y_{real}", ")", "= K"
        ).move_to([3,2,0]).scale(0.8)
        self.play(TransformMatchingTex(eqxv, eqyv))
        self.play(FadeOut(eqy3))


        # 函数视角变化 并且每个人可以选择不同的区间

        ax_lab = ax.get_axis_labels(
            x_label=Tex("$\sqrt{P}$"), y_label=Tex("$L$")
        )
        new_g = ax.plot(
                lambda x: 6, 
                color=YELLOW,
                x_range=[4, 8],
        )
        self.play(
            FadeOut(priceA, x_det_brace, y_det_brace, x_det_brace_lab, y_det_brace_lab, labA, p_lab, p, dox_x_with_lab, fix_dot_with_label, x_det, y_det, i),
            Create(ax_lab, run_time=1), 
            Transform(graph, new_g)
        )

        self.play(Create(ax.get_vertical_line(ax.c2p(8, 6))))
        self.play(Create(ax.get_T_label(x_val=8, graph=new_g, label=Tex("A"))))
        self.play(Create(ax.get_vertical_line(ax.c2p(4, 6))))
        self.play(Create(ax.get_T_label(x_val=4, graph=new_g, label=Tex("B"))))

        # 对于swap操作

        p = Dot()
        p.add_updater(lambda x: x.move_to(ax.c2p(p_v.get_value(), 6)))
        p_l = ax.get_vertical_line(point=ax.c2p(p_v.get_value(), 6))
        self.play(Create(p), Create(p_l))

        self.play(Create(ax.get_T_label(x_val=p_v.get_value(), graph=new_g, label=Tex("Price"))))




        
        self.wait(3)