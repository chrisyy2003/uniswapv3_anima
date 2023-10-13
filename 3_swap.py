from manim import *
from math import sqrt

class Scene3(Scene):

    def construct(self):
        
        l = 1800 * 2
        price = 1800
        price = round(sqrt(price), 3)
        price_range = [price - 2, price + 3, 0.5]
        
        ax = Axes(
                x_range=price_range,
                y_range=[l - 300, l + 300, 100],
                x_length=6,
                y_length=6,
                axis_config={"include_tip": False},
            )

        ax_labels = ax.get_axis_labels(
            x_label=Tex("$\sqrt{P}$"), y_label=Tex("$L$")
        )
        curve = ax.plot(
            lambda x: l, 
            color=DARK_BLUE,
            x_range=[price - 0.5, price + 1, 0.5],

        )
        area = ax.get_area(
            curve,
            x_range=(price - 0.5, price + 1),
            color=(RED_B, BLUE_B),
            opacity=1,
        )

        t = ValueTracker(price)
        def point():
            return ax.i2gp(t.get_value(), graph=curve)

        dot = always_redraw(lambda : Dot(point()))
        line = always_redraw(lambda :ax.get_vertical_line(point()))

        self.add(ax, curve, area, dot, line, ax_labels)

        # #  之间有一个有趣的关系 从之前得出的公式 我们可以发现 对于价格A

        eqy = MathTex(
                '''
                \\left.\\begin{array}{c}
                \\frac{Y_b}{X_b}=P_b \\\\
                X_b \\times Y_b=L^2
                \\end{array}\\right\\}
                ''',
                "\\Rightarrow Y_b",
                "=L \\sqrt{P_b}}"
            ).move_to([3,2,0])
        self.play(Write(eqy))
        self.wait(1)

        eqy2 = MathTex(
                "Y_b",
                "=L", "\\sqrt{P_b}"
            ).move_to([3,2,0])

        self.play(TransformMatchingTex(eqy, eqy2))
        self.wait(1)


        eqy3 = MathTex(
                "Y_b",
                "=L", "\\sqrt{p_b}"
            ).next_to(eqy2, DOWN)
        self.play(Write(eqy3))

        # 所以可得到 数量和价格之间的关系
        eqy4 = MathTex(
                "Y_a", "-", "Y_b"
                "=L", "(", "\\sqrt{p_a}", "-", "\\sqrt{p_b}", ")"
            ).move_to([3,1,0])
        self.play(TransformMatchingTex(Group(eqy2, eqy3), eqy4))
        eqy5 = MathTex(
                "\\Delta Y"
                "=L", "\\Delta \\sqrt{p}"
            ).move_to([3,1,0])
        self.play(TransformMatchingTex(eqy4, eqy5))
        self.wait(1)


        # 同理得到x的关系
        eqx = MathTex(
                "\\Delta X",
                "=L", "\\Delta \\frac{1}{\\sqrt{p}} "
            ).next_to(eqy5, UP)
        self.play(Write(eqx))
        self.wait(1)

        eq_g = Group(eqx, eqy5)

        # 整体移动
        self.play(
            Group(ax, curve, area, ax_labels, line).animate.shift(LEFT * 2.5),
            eq_g.animate.scale(0.8).move_to([-2.5, 2, 0])
        )
        self.wait(1)


        # 带入数据 举个例子
        self.play(Transform(ax, Axes(
                x_range=[price - 2, price + 3, 0.5],
                y_range=[l - 300, l + 300, 100],
                x_length=6,
                y_length=6,
                y_axis_config={"numbers_to_include": [l]},
                x_axis_config={"numbers_to_include": [42, 43, 0.1]},
                tips=False
            ).shift(LEFT * 2.5).set_z_index(-1)))

        hline = always_redraw(lambda :ax.get_horizontal_line(point())) 
        xlab = always_redraw(lambda : ax.get_graph_label(
            curve, str(t.get_value()), x_val=t.get_value(), direction=UR, color=WHITE
        ))
        self.play(Create(hline), Create(xlab))
        self.wait(1)


        info1 = Tex("ETH = 1800 USDC").move_to([3,3,0]).scale(0.7)
        info2 = Tex("USDC in 1800")
        info2.next_to(info1, DOWN, aligned_edge=LEFT).scale(0.7) # TODO: left
        self.play(Create(info2), Create(info1))
        self.wait(1)


        e = eqy5.copy()
        self.play(e.animate.next_to(info2, DOWN * 3))
  
        e1 = MathTex("\\Delta \\sqrt{P}", " = ", "\\frac{\\Delta Y}{L}").move_to(e).scale(0.8)
        e2 = MathTex("\\Delta \\sqrt{P}", " = ", "\\frac{\\Delta Y}{L}", "=", "\\frac{1800}{3600}").move_to(e).scale(0.8)
        e3 = MathTex("\\Delta \\sqrt{P}", " = ", "\\frac{\\Delta Y}{L}", "=", "\\frac{1800}{3600}", "=", "0.5").move_to(e).scale(0.8)

        self.play(TransformMatchingTex(e, e1))
        self.play(TransformMatchingTex(e1, e2))
        self.play(TransformMatchingTex(e2, e3))
        self.wait(1)


        self.play(t.animate.set_value(price + 0.5))

        ex = eqx.copy()
        ex1 = MathTex(
            "\\Delta X",
            "=L", "\\Delta \\frac{1}{\\sqrt{p}}", "=", "0.988"
        ).next_to(e3, DOWN).scale(0.8)
        self.play(ex.animate.next_to(e3, DOWN))
        self.play(TransformMatchingTex(ex, ex1))

        self.play(Indicate(ex1))

        self.wait(3)