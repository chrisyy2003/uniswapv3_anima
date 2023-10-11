from manim import *

# 手续费

class Scene6(Scene):

    def construct(self):

        n_line = NumberLine(
            x_range=[0, 10 + 1, 1],
            length=12,
            include_tip=True,
            # include_numbers=True,
        ).shift(DOWN * 2)
        self.play(Create(n_line))

        postion_length = (n_line.n2p(7)-n_line.n2p(2))[0]

        r1 = Rectangle(
            height=1,
            width=postion_length,
            fill_opacity=0.5
        ).move_to(n_line.n2p(3), aligned_edge=DL)

        self.play(Create(r1))

        t = ValueTracker(5)

        pointer = Vector(UP)
        pointer.add_updater(lambda m: m.next_to(n_line.n2p(t.get_value()), DOWN))

        label = MathTex("Price_c")
        label.add_updater(lambda m: m.next_to(pointer, DOWN))

        self.add(pointer, label)

        self.play(t.animate.set_value(4))
        self.play(t.animate.set_value(6))

        r2 = Rectangle(
            height=1,
            width=postion_length,
            fill_opacity=0.5,
        ).move_to(n_line.n2p(5), aligned_edge=DL)

        self.play(Create(r2), r1.animate.shift(UP))

        e1 = MathTex('feeGrowthGlobal').move_to([0, 3, 0])
        e2 = MathTex('liquidity').next_to(e1, DOWN, aligned_edge=LEFT)

        self.play(Create(e1), Create(e2))

        lr = Rectangle(
            height=2,
            width=(n_line.n2p(3)-n_line.n2p(0))[0],
            color=RED_B,
            fill_opacity=0.5
        ).move_to(n_line.n2p(5), aligned_edge=DL).set_z_index(10)
        self.play(Create(lr))

        self.play(TransformMatchingTex(Group(e1,e2), MathTex('feeGrowthGlobal', '+=', '\\frac{\\Delta fee}{liquidity}').move_to(e2))) 

        # 只能计算当前激活的区间，feeGrowthGlobal还包含其他区间累加的fee，因为liquidity是记录激活的
        # 所以v3通过记录区间外的手续费来记录所有的手续费

        e3 = MathTex('feeGrowthOutside').next_to(e2, DOWN * 2)
        self.play(Create(e3))

        n_line.add_labels(dict_values={
            5: MathTex('Tick_{1}'),
            8: MathTex('Tick_{2}'),
            10: MathTex('Tick_{3}')
        })


        lp = Vector(LEFT).move_to(n_line.n2p(4.5), aligned_edge=RIGHT).shift(UP * 0.5)
        rp = Vector(RIGHT).move_to(n_line.n2p(8.5), aligned_edge=LEFT).shift(UP * 0.5)

        self.play(Create(lp), Create(rp))

        self.play(TransformMatchingTex(e3, MathTex('Position', '=', 'feeGrowthGlobal', '-', 'feeGrowthOutside').move_to(e3))) 

        self.play(t.animate.set_value(9))
        self.play(lr.animate.become(Rectangle(
            height=1,
            width=(n_line.n2p(2)-n_line.n2p(0))[0],
            color=RED_B,
            fill_opacity=0.5
        ).move_to(n_line.n2p(8), aligned_edge=DL).set_z_index(10)))
        

        self.play(
            rp.animate.become(Vector(LEFT).move_to(n_line.n2p(9.5), aligned_edge=RIGHT).shift(UP * 0.5)),
            lp.animate.become(Vector(LEFT).move_to(n_line.n2p(7.5), aligned_edge=RIGHT).shift(UP * 0.5)),
        )
        self.play(Indicate(n_line.labels[1]))









        


        self.wait(3)