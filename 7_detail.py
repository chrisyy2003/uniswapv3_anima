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


        code = '''uint256 public override feeGrowthGlobal0X128;
uint256 public override feeGrowthGlobal1X128;
uint128 public override liquidity;

mapping(int24 => Tick.Info) public override ticks;
mapping(int16 => uint256) public override tickBitmap;
mapping(bytes32 => Position.Info) public override positions;
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Solidity")
        self.play(Create(rendered_code), FadeOut(m))
        self.play(FadeOut(rendered_code))

        code2 = '''
struct Info {
    uint128 liquidityGross;
    int128 liquidityNet;
    uint256 feeGrowthOutside0X128;
    uint256 feeGrowthOutside1X128;
    bool initialized;
}
'''     
        rendered_code2 = Code(code=code2, tab_width=4, background="window",
                            language="Solidity")
        self.play(Create(rendered_code2))

        pos = Rectangle(
            height=1,
            width=(n_line.n2p(2)-n_line.n2p(0))[0],
            fill_opacity=0.5
        ).move_to(n_line.n2p(-1), aligned_edge=DL).set_z_index(10)
        self.play(Create(pos))

        self.play(rendered_code2.animate.move_to(n_line.n2p(-1), aligned_edge=DOWN).scale(0.4).shift(UP * 1),
                  Create(Vector(DOWN).next_to(n_line.n2p(-1), UP * 3.7).scale(0.8)),
                  rendered_code2.copy().animate.move_to(n_line.n2p(1), aligned_edge=DOWN).scale(0.4).shift(UP * 1),
                  Create(Vector(DOWN).next_to(n_line.n2p(1), UP * 3.7).scale(0.8)),
                  )
        
        # 修改流动性的时候会调用tick 中的一个update 函数
        self.play(pos.animate.become(Rectangle(
            height=0.5,
            width=(n_line.n2p(2)-n_line.n2p(0))[0],
            fill_opacity=0.5
        ).move_to(n_line.n2p(-1), aligned_edge=DL)))

        self.play(pos.animate.become(Rectangle(
            height=1,
            width=(n_line.n2p(2)-n_line.n2p(0))[0],
            fill_opacity=0.5
        ).move_to(n_line.n2p(-1), aligned_edge=DL)))

        t1 = MathTex("{\\rm Liquidity:\;}ticks.update").move_to([0, 3, 0])
        self.play(Create(t1))

        t2 = MathTex("{\\rm Cross:\;}ticks.cross").next_to(t1, DOWN, aligned_edge=LEFT)
        self.play(Create(t2))

        # 穿越的时候会调用 cross 函数


        self.wait(3)