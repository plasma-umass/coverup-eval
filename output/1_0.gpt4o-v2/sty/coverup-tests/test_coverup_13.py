# file: sty/register.py:78-121
# asked: {"lines": [78, 79, 81, 83, 84, 85, 87, 88, 92, 93, 94, 95, 96, 97, 98, 99, 101, 104, 105, 106, 107, 108, 109, 110, 111, 114, 115, 116, 117, 118, 119, 120, 121], "branches": []}
# gained: {"lines": [78, 79, 81, 83, 84, 85, 87, 88, 92, 93, 94, 95, 96, 97, 98, 99, 101, 104, 105, 106, 107, 108, 109, 110, 111, 114, 115, 116, 117, 118, 119, 120, 121], "branches": []}

import pytest
from sty import renderfunc
from sty.primitive import Register, Style
from sty.rendertype import EightbitBg, RgbBg, Sgr

class BgRegister(Register):
    def __init__(self):
        super().__init__()
        self.renderfuncs[Sgr] = renderfunc.sgr
        self.renderfuncs[EightbitBg] = renderfunc.eightbit_bg
        self.renderfuncs[RgbBg] = renderfunc.rgb_bg
        self.set_eightbit_call(EightbitBg)
        self.set_rgb_call(RgbBg)
        self.black = Style(Sgr(40))
        self.red = Style(Sgr(41))
        self.green = Style(Sgr(42))
        self.yellow = Style(Sgr(43))
        self.blue = Style(Sgr(44))
        self.magenta = Style(Sgr(45))
        self.cyan = Style(Sgr(46))
        self.li_grey = Style(Sgr(47))
        self.rs = Style(Sgr(49))
        self.da_grey = Style(Sgr(100))
        self.li_red = Style(Sgr(101))
        self.li_green = Style(Sgr(102))
        self.li_yellow = Style(Sgr(103))
        self.li_blue = Style(Sgr(104))
        self.li_magenta = Style(Sgr(105))
        self.li_cyan = Style(Sgr(106))
        self.white = Style(Sgr(107))
        self.da_black = Style(EightbitBg(0))
        self.da_red = Style(EightbitBg(88))
        self.da_green = Style(EightbitBg(22))
        self.da_yellow = Style(EightbitBg(58))
        self.da_blue = Style(EightbitBg(18))
        self.da_magenta = Style(EightbitBg(89))
        self.da_cyan = Style(EightbitBg(23))
        self.grey = Style(EightbitBg(249))

@pytest.fixture
def bg_register():
    return BgRegister()

def test_bg_register_initialization(bg_register):
    assert bg_register.renderfuncs[Sgr] == renderfunc.sgr
    assert bg_register.renderfuncs[EightbitBg] == renderfunc.eightbit_bg
    assert bg_register.renderfuncs[RgbBg] == renderfunc.rgb_bg
    assert isinstance(bg_register.black, Style)
    assert isinstance(bg_register.red, Style)
    assert isinstance(bg_register.green, Style)
    assert isinstance(bg_register.yellow, Style)
    assert isinstance(bg_register.blue, Style)
    assert isinstance(bg_register.magenta, Style)
    assert isinstance(bg_register.cyan, Style)
    assert isinstance(bg_register.li_grey, Style)
    assert isinstance(bg_register.rs, Style)
    assert isinstance(bg_register.da_grey, Style)
    assert isinstance(bg_register.li_red, Style)
    assert isinstance(bg_register.li_green, Style)
    assert isinstance(bg_register.li_yellow, Style)
    assert isinstance(bg_register.li_blue, Style)
    assert isinstance(bg_register.li_magenta, Style)
    assert isinstance(bg_register.li_cyan, Style)
    assert isinstance(bg_register.white, Style)
    assert isinstance(bg_register.da_black, Style)
    assert isinstance(bg_register.da_red, Style)
    assert isinstance(bg_register.da_green, Style)
    assert isinstance(bg_register.da_yellow, Style)
    assert isinstance(bg_register.da_blue, Style)
    assert isinstance(bg_register.da_magenta, Style)
    assert isinstance(bg_register.da_cyan, Style)
    assert isinstance(bg_register.grey, Style)
