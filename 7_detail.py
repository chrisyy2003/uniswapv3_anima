from manim import *


class Scene7(Scene):

    def construct(self):
        n_line = NumberLine(
            x_range=[-3, 3, 1],
            length=12,
            include_tip=True,
            include_numbers=True,
        ).shift(DOWN * 2)


        self.play(Create(n_line))

        m = MathTex('p(i) = 1.0001^{i}')
        self.play(Write(m))


        label_dict = {}
        for i in range(-5 ,6):
            label_dict[i] = MathTex(round(1.0001 ** i, 5))

        self.play(n_line.animate.add_labels(dict_values=label_dict, direction=DOWN * 3))


        self.wait(3)