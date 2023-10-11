from manim import *
from math import sqrt 

# 限价单和流动性

class Scene4(Scene):

    def construct(self):
        l = 1800 * 2
        price = 1800
        price = round(sqrt(price), 3)
        price_range = [price - 2, price + 3, 0.5]
        
        ax = Axes(
                x_range=[price - 2, price + 3, 0.5],
                y_range=[l - 300, l + 300, 100],
                x_length=6,
                y_length=6,
                tips=False
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

        t = ValueTracker(price + 0.5)
        def point():
            return ax.i2gp(t.get_value(), graph=curve)

        dot = always_redraw(lambda : Dot(point()))
        line = always_redraw(lambda :ax.get_vertical_line(point()))
        hline = always_redraw(lambda :ax.get_horizontal_line(point())) 

        self.add(Group(ax, curve, area, ax_labels, line, hline, dot).shift(LEFT * 3).scale(0.9))

        k = 420
        kt = ValueTracker(42)
        k_ax = Axes(
                x_range=[0, 10],
                y_range=[0, 420, 50],
                x_length=6,
                y_length=6,
                axis_config={"include_tip": False},
            )
        k_curve = k_ax.plot(
                lambda x: k / x,
                color=YELLOW_D,
                x_range=[1, 10.0, 0.01],
                use_smoothing=False,
        )
        p_curve = always_redraw(lambda :k_ax.plot(
            lambda x: kt.get_value() * x,
            color=YELLOW_D,
            x_range=[0, 10.0, 0.01],
            use_smoothing=False,
        )) 

        def p_point():
            return k_ax.i2gp(sqrt(k / kt.get_value()), graph=k_curve)
        p_dot = always_redraw(lambda :Dot(p_point()))
        k_ax_labels = k_ax.get_axis_labels(
            x_label=Tex("$X$"), y_label=Tex("$Y$")
        )

        self.play(Create(VGroup(
            k_ax, k_curve, p_curve, p_dot,
            k_ax.get_graph_label(k_curve, "A", x_val=1.5, direction=UR, color=WHITE, dot=True),
            k_ax.get_graph_label(k_curve, "B", x_val=5, direction=UR, color=WHITE, dot=True), 
            k_ax_labels
        ).scale(0.8).move_to([4, 0, 0])))

        self.wait(1)
        self.play(area.animate.set_color(BLUE_B), kt.animate.set_value(420/1.5/1.5), t.animate.set_value(price + 1))
        self.wait(1)
        self.play(area.animate.set_color(RED_B), kt.animate.set_value(84/5), t.animate.set_value(price - 0.5))
        self.wait(1)
        self.play(area.animate.set_color(interpolate_color(RED_B, BLUE_B, 0.5)), kt.animate.set_value(420/3.25/3.25), t.animate.set_value(price + 0.25))
        # # self.play(area.animate.set_color(BLUE_B), kt.animate.set_value(420/1.25/1.25), t.animate.set_value(price + 2))
        self.wait(1)

        # 所以添加流动性跟当前的价格有关
        arear, areal  = ax.get_area(
            curve,
            x_range=(price - 1.5, price - 1),
            color=(BLUE_B),
            opacity=1,
        ), ax.get_area(
            curve,
            x_range=(price + 1.5, price + 2),
            color=(RED_B),
            opacity=1,
        )

        self.play(
            Create(arear),
            area.animate.set_color(BLUE_B), kt.animate.set_value(420/1.2/1.2), t.animate.set_value(price + 1.25)
        )
        self.wait(1)

        
        
        l1 = ax.get_graph_label(
            curve, "\\Delta Y =L \\Delta \\sqrt{P}}", x_val=price - 1.75, direction=UR, color=WHITE
        ).scale(0.7)

        l12 = ax.get_graph_label(
            curve, "\\frac{\\Delta y}{\\Delta \\sqrt{p}}", x_val=price - 1.75, direction=UR, color=WHITE
        ).scale(0.8)
        self.play(Create(l1))
        self.play(Transform(l1, l12))

        # 对于在右侧添加流动性的情况
        self.play(
            Create(areal),
            area.animate.set_color(RED_B), kt.animate.set_value(84/7), t.animate.set_value(price - 0.75)
        )

        l2 = ax.get_graph_label(
            curve, "\\Delta X =\\frac{L}{\\sqrt{P_a}}", x_val=price + 0.5, direction=UP, color=WHITE
        ).scale(0.7)

        l22 = ax.get_graph_label(
            curve, "\\frac{\\Delta x}{\\Delta \\frac{1}{\\sqrt{p}}}", x_val=price + 1, direction=UR, color=WHITE
        ).scale(0.8)
        self.play(Create(l2))
        self.play(Transform(l2, l22))


        self.play(
            area.animate.set_color(interpolate_color(RED_B, BLUE_B, 0.5)), kt.animate.set_value(420/3.25/3.25), t.animate.set_value(price + 0.25),
            Create(ax.get_graph_label(curve, "min(\\frac{\\Delta y}{\\Delta \\sqrt{p_1}}, \\frac{\\Delta x}{\\Delta \\frac{1}{\\sqrt{p_2}}})", x_val=price + 0.25, direction=UP, color=WHITE
        ).scale(0.8).shift(UP * 1.5)))

        self.wait(3)