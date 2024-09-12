# file: sty/register.py:32-75
# asked: {"lines": [32, 33, 35, 37, 38, 39, 41, 42, 46, 47, 48, 49, 50, 51, 52, 53, 55, 58, 59, 60, 61, 62, 63, 64, 65, 68, 69, 70, 71, 72, 73, 74, 75], "branches": []}
# gained: {"lines": [32, 33, 35, 37, 38, 39, 41, 42, 46, 47, 48, 49, 50, 51, 52, 53, 55, 58, 59, 60, 61, 62, 63, 64, 65, 68, 69, 70, 71, 72, 73, 74, 75], "branches": []}

import pytest
from sty import renderfunc
from sty.primitive import Register, Style
from sty.rendertype import EightbitFg, RgbFg, Sgr

class FgRegister(Register):
    def __init__(self):
        super().__init__()
        self.renderfuncs[Sgr] = renderfunc.sgr
        self.renderfuncs[EightbitFg] = renderfunc.eightbit_fg
        self.renderfuncs[RgbFg] = renderfunc.rgb_fg
        self.set_eightbit_call(EightbitFg)
        self.set_rgb_call(RgbFg)
        self.black = Style(Sgr(30))
        self.red = Style(Sgr(31))
        self.green = Style(Sgr(32))
        self.yellow = Style(Sgr(33))
        self.blue = Style(Sgr(34))
        self.magenta = Style(Sgr(35))
        self.cyan = Style(Sgr(36))
        self.li_grey = Style(Sgr(37))
        self.rs = Style(Sgr(39))
        self.da_grey = Style(Sgr(90))
        self.li_red = Style(Sgr(91))
        self.li_green = Style(Sgr(92))
        self.li_yellow = Style(Sgr(93))
        self.li_blue = Style(Sgr(94))
        self.li_magenta = Style(Sgr(95))
        self.li_cyan = Style(Sgr(96))
        self.white = Style(Sgr(97))
        self.da_black = Style(EightbitFg(0))
        self.da_red = Style(EightbitFg(88))
        self.da_green = Style(EightbitFg(22))
        self.da_yellow = Style(EightbitFg(58))
        self.da_blue = Style(EightbitFg(18))
        self.da_magenta = Style(EightbitFg(89))
        self.da_cyan = Style(EightbitFg(23))
        self.grey = Style(EightbitFg(249))

@pytest.fixture
def fg_register():
    return FgRegister()

def test_fg_register_initialization(fg_register):
    assert isinstance(fg_register.black, Style)
    assert isinstance(fg_register.red, Style)
    assert isinstance(fg_register.green, Style)
    assert isinstance(fg_register.yellow, Style)
    assert isinstance(fg_register.blue, Style)
    assert isinstance(fg_register.magenta, Style)
    assert isinstance(fg_register.cyan, Style)
    assert isinstance(fg_register.li_grey, Style)
    assert isinstance(fg_register.rs, Style)
    assert isinstance(fg_register.da_grey, Style)
    assert isinstance(fg_register.li_red, Style)
    assert isinstance(fg_register.li_green, Style)
    assert isinstance(fg_register.li_yellow, Style)
    assert isinstance(fg_register.li_blue, Style)
    assert isinstance(fg_register.li_magenta, Style)
    assert isinstance(fg_register.li_cyan, Style)
    assert isinstance(fg_register.white, Style)
    assert isinstance(fg_register.da_black, Style)
    assert isinstance(fg_register.da_red, Style)
    assert isinstance(fg_register.da_green, Style)
    assert isinstance(fg_register.da_yellow, Style)
    assert isinstance(fg_register.da_blue, Style)
    assert isinstance(fg_register.da_magenta, Style)
    assert isinstance(fg_register.da_cyan, Style)
    assert isinstance(fg_register.grey, Style)

def test_fg_register_renderfuncs(fg_register):
    assert fg_register.renderfuncs[Sgr] == renderfunc.sgr
    assert fg_register.renderfuncs[EightbitFg] == renderfunc.eightbit_fg
    assert fg_register.renderfuncs[RgbFg] == renderfunc.rgb_fg

def test_fg_register_calls(fg_register):
    assert fg_register.eightbit_call == renderfunc.eightbit_fg
    assert fg_register.rgb_call == renderfunc.rgb_fg
