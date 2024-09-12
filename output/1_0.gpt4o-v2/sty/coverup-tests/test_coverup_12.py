# file: sty/register.py:124-146
# asked: {"lines": [124, 125, 127, 129, 131, 132, 133, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146], "branches": []}
# gained: {"lines": [124, 125, 127, 129, 131, 132, 133, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146], "branches": []}

import pytest
from sty import renderfunc
from sty.primitive import Register, Style
from sty.rendertype import Sgr

class RsRegister(Register):
    def __init__(self):
        super().__init__()
        self.renderfuncs[Sgr] = renderfunc.sgr
        self.all = Style(Sgr(0))
        self.fg = Style(Sgr(39))
        self.bg = Style(Sgr(49))
        self.rs = Style(Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29))
        self.bold_dim = Style(Sgr(22))
        self.dim_bold = Style(Sgr(22))
        self.i = Style(Sgr(23))
        self.italic = Style(Sgr(23))
        self.u = Style(Sgr(24))
        self.underl = Style(Sgr(24))
        self.blink = Style(Sgr(25))
        self.inverse = Style(Sgr(27))
        self.hidden = Style(Sgr(28))
        self.strike = Style(Sgr(29))

@pytest.fixture
def rs_register():
    return RsRegister()

def test_rs_register_initialization(rs_register):
    assert isinstance(rs_register.all, Style)
    assert isinstance(rs_register.fg, Style)
    assert isinstance(rs_register.bg, Style)
    assert isinstance(rs_register.rs, Style)
    assert isinstance(rs_register.bold_dim, Style)
    assert isinstance(rs_register.dim_bold, Style)
    assert isinstance(rs_register.i, Style)
    assert isinstance(rs_register.italic, Style)
    assert isinstance(rs_register.u, Style)
    assert isinstance(rs_register.underl, Style)
    assert isinstance(rs_register.blink, Style)
    assert isinstance(rs_register.inverse, Style)
    assert isinstance(rs_register.hidden, Style)
    assert isinstance(rs_register.strike, Style)

def test_rs_register_renderfuncs(rs_register):
    assert Sgr in rs_register.renderfuncs
    assert rs_register.renderfuncs[Sgr] == renderfunc.sgr
