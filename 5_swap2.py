from manim import *
# 跨tick交易

class Scene5(Scene):

    def construct(self):

        # pool = ImageMobject('./img/pool.png')
        # self.add(pool)

        price = 1800
        l = 1800 * 2

        ax = Axes(
                x_range=[price - 2, price + 3, 0.5],
                y_range=[l - 300, l + 300, 100],
                x_length=6,
                y_length=6,
                # x_axis_config={"numbers_to_include": np.arange(price - 2, price + 3, 0.5)},
                # y_axis_config={"numbers_to_include": [l]},
                tips=False
            )
        curve1 = ax.plot(lambda x: l - 200, 
            x_range=[price - 0.5, price + 1, 0.5],
        )
        curve2 = ax.plot(lambda x: l - 100, 
            x_range=[price - 0.5, price + 1, 0.5],
        )
        curve3 = ax.plot(lambda x: l, 
            x_range=[price - 0.5, price + 1, 0.5],
        )
        curve4 = ax.plot(lambda x: l - 150, 
            x_range=[price - 0.5, price + 1, 0.5],
        )

        area1 = ax.get_area(curve1, x_range=(price - 1 , price - 0.5), color=(GREEN_C), opacity=1,)
        area2 = ax.get_area(curve2, x_range=(price - 0.5 , price), color=(GREEN_C), opacity=1,)
        area3 = ax.get_area(curve3, x_range=(price , price + 0.5), color=(GREEN_C), opacity=1,)
        area4 = ax.get_area(curve4, x_range=(price - 0.5 , price + 1), color=(GREEN_C), opacity=1,)

        self.play(Create(ax))

        
        t = ValueTracker(price + 0.25)
        def point():
            return ax.i2gp(t.get_value(), graph=curve3)

        dot = always_redraw(lambda : Dot(point()))
        line = always_redraw(lambda :ax.get_vertical_line(point(), stroke_width=6))
        self.play(Create(area1), Create(area2), Create(area3), Create(area4), Create(line), Create(dot))

        tex1 = Tex("1. Check input").scale(0.8).move_to([2,3,0])
        tex2 = Tex("2. Swap within current interval").scale(0.8).next_to(tex1, DOWN, aligned_edge=LEFT)
        tex3 = Tex("3. Still remaining input or output?").scale(0.8).next_to(tex2, DOWN, aligned_edge=LEFT)
        tex4 = Tex("4. Cross next tick").scale(0.8).next_to(tex3, DOWN, aligned_edge=LEFT)
        tex5 = Tex("5. Execute computed swap").scale(0.8).next_to(tex4, DOWN, aligned_edge=LEFT)

        self.play(Create(tex1))
        self.wait(1)
        self.play(Create(tex2))
        self.wait(1)

        self.play(Indicate(line))
        self.wait(1)

        self.play(t.animate.set_value(price + 0.5))

        self.play(Create(tex3))
        self.wait(1)

        self.play(Create(tex4))
        self.wait(1)



        self.play(Indicate(line))
        self.wait(1)

        def point():
            return ax.i2gp(t.get_value(), graph=curve4)
        self.play(t.animate.set_value(price + 0.75))
        self.play(Indicate(tex2))
        self.wait(1)

        self.play(Indicate(tex3))
        self.wait(1)

        self.play(Indicate(tex5))
        self.wait(1)


        # 区间连续


        self.wait(3)

        