# file: sty/register.py:9-29
# asked: {"lines": [9, 10, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29], "branches": []}
# gained: {"lines": [9, 10, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29], "branches": []}

import pytest
from sty import renderfunc
from sty.primitive import Register, Style
from sty.rendertype import Sgr

class EfRegister(Register):
    def __init__(self):
        super().__init__()
        self.renderfuncs[Sgr] = renderfunc.sgr
        self.b = Style(Sgr(1), value=renderfunc.sgr(1))
        self.bold = Style(Sgr(1), value=renderfunc.sgr(1))
        self.dim = Style(Sgr(2), value=renderfunc.sgr(2))
        self.i = Style(Sgr(3), value=renderfunc.sgr(3))
        self.italic = Style(Sgr(3), value=renderfunc.sgr(3))
        self.u = Style(Sgr(4), value=renderfunc.sgr(4))
        self.underl = Style(Sgr(4), value=renderfunc.sgr(4))
        self.blink = Style(Sgr(5), value=renderfunc.sgr(5))
        self.inverse = Style(Sgr(7), value=renderfunc.sgr(7))
        self.hidden = Style(Sgr(8), value=renderfunc.sgr(8))
        self.strike = Style(Sgr(9), value=renderfunc.sgr(9))
        self.rs = Style(Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29), value=''.join([renderfunc.sgr(i) for i in [22, 23, 24, 25, 27, 28, 29]]))

def test_efregister_initialization():
    ef_register = EfRegister()
    
    assert ef_register.renderfuncs[Sgr] == renderfunc.sgr
    assert ef_register.b == Style(Sgr(1), value=renderfunc.sgr(1))
    assert ef_register.bold == Style(Sgr(1), value=renderfunc.sgr(1))
    assert ef_register.dim == Style(Sgr(2), value=renderfunc.sgr(2))
    assert ef_register.i == Style(Sgr(3), value=renderfunc.sgr(3))
    assert ef_register.italic == Style(Sgr(3), value=renderfunc.sgr(3))
    assert ef_register.u == Style(Sgr(4), value=renderfunc.sgr(4))
    assert ef_register.underl == Style(Sgr(4), value=renderfunc.sgr(4))
    assert ef_register.blink == Style(Sgr(5), value=renderfunc.sgr(5))
    assert ef_register.inverse == Style(Sgr(7), value=renderfunc.sgr(7))
    assert ef_register.hidden == Style(Sgr(8), value=renderfunc.sgr(8))
    assert ef_register.strike == Style(Sgr(9), value=renderfunc.sgr(9))
    assert ef_register.rs == Style(Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29), value=''.join([renderfunc.sgr(i) for i in [22, 23, 24, 25, 27, 28, 29]]))
